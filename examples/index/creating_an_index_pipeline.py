import asyncio

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types import (
    AutoTransformConfigParam,
    # AdvancedModeTransformConfigParam,
    LlamaParseParametersParam,
)
from llama_cloud.types.pipelines import CloudDocumentCreateParam
from llama_cloud.types.pipeline_create_params import (
    EmbeddingConfigOpenAIEmbeddingConfig,
    EmbeddingConfigOpenAIEmbeddingConfigComponent,
)
from llama_cloud.types.data_sink_create_params import (
    ComponentCloudPineconeVectorStore,
    # ComponentCloudQdrantVectorStore,
    # ComponentCloudPostgresVectorStore,
    # ComponentCloudAzureAISearchVectorStore,
    # ComponentCloudAstraDBVectorStore,
    # ComponentCloudMilvusVectorStore,
    # ComponentCloudMongoDBAtlasVectorSearch,
)
from llama_cloud.types.data_source_create_params import (
    ComponentCloudS3DataSource,
    # ComponentCloudAzStorageBlobDataSource,
    # ComponentCloudSharepointDataSource,
    # ComponentCloudOneDriveDataSource,
)


async def create_index() -> None:
    client = AsyncLlamaCloud()

    # Creating an index involves 5 main pieces
    # 1. The data sink (if blank, the default managed vector store will be used)
    # 2. The embedding configuration (if blank, the default embedding config will be used)
    # 3. The data source (if blank, no data will be connected by default, you can always add data later)
    # 4. The parsing parameters when ingesting data (if blank, the default parsing parameters will be used)
    # 5. The transform configuration when processing ingested data (if blank, the default transform configuration will be used)
    pipeline = await client.pipelines.create(
        name="my-first-index",
        project_id="my-project-id",
        data_sink_id=await create_data_sink(),
        embedding_config=EmbeddingConfigOpenAIEmbeddingConfig(
            component=EmbeddingConfigOpenAIEmbeddingConfigComponent(
                api_key="sk-1234",
                model_name="text-embedding-3-small",
            ),
            type="OPENAI_EMBEDDING",
        ),
        llama_parse_parameters=LlamaParseParametersParam(),
        transform_config=AutoTransformConfigParam(chunk_overlap=128, chunk_size=1028),
    )

    print(pipeline.id)

    # Optional: Upload data after creating the index
    documents = await client.pipelines.documents.create(
        pipeline_id=pipeline.id,
        body=[
            CloudDocumentCreateParam(
                text="This is my first document to be indexed.",
                metadata={"source": "generated"},
            )
        ],
    )
    print(f"Uploaded {len(documents)} documents to the index.")

    # Optional: Wait for indexing to complete
    status_resp = await client.pipelines.get_status(pipeline_id=pipeline.id)
    while status_resp.status not in ("NOT_STARTED", "IN_PROGRESS"):
        await asyncio.sleep(5)
        status_resp = await client.pipelines.get_status(pipeline_id=pipeline.id)

    print(f"Indexing completed with status: {status_resp.status}")


async def create_data_sink() -> str:
    client = AsyncLlamaCloud()

    # create a data source
    data_sink = await client.data_sinks.create(
        name="my-pinecone-data-sink",
        component=ComponentCloudPineconeVectorStore(
            api_key="my-pinecone-api-key",
            index_name="my-pinecone-index",
        ),
        sink_type="PINECONE",
    )

    return data_sink.id


async def create_data_source() -> str:
    client = AsyncLlamaCloud()

    # create a data source
    data_source = await client.data_sources.create(
        name="my-s3-data-source",
        component=ComponentCloudS3DataSource(
            bucket="my-bucket",
            aws_access_id="my-access-id",
            prefix="documents/",
        ),
        source_type="S3",
        project_id="my-project-id",
    )

    return data_source.id


if __name__ == "__main__":
    asyncio.run(create_index())
