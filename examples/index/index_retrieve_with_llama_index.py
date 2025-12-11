import asyncio

from llama_cloud.lib.index import LlamaCloudIndex
from llama_cloud.types.pipeline_create_params import (
    EmbeddingConfigOpenAIEmbeddingConfig,
    EmbeddingConfigOpenAIEmbeddingConfigComponent,
)


async def indexing_and_retrieval_with_llama_index_from_files() -> None:
    index = await LlamaCloudIndex.acreate_index(
        name="my-llama-index",
        project_id="my-project-id",
        embedding_config=EmbeddingConfigOpenAIEmbeddingConfig(
            component=EmbeddingConfigOpenAIEmbeddingConfigComponent(
                api_key="sk-1234",
                model_name="text-embedding-3-small",
            ),
            type="OPENAI_EMBEDDING",
        ),
        llama_parse_parameters={"parse_mode": "parse_document_with_agent", "model": "openai-gpt-4-1-mini"},
        transform_config={"chunk_overlap": 128, "chunk_size": 1028},
    )

    # Index documents from files
    file_id = await index.aupload_file("../example_files/attention_is_all_you_need.pdf", wait_for_ingestion=True)

    # If not waiting for ingestion above, you can wait once you've uploaded all files
    await index.await_for_completion(file_ids=[file_id])


if __name__ == "__main__":
    asyncio.run(indexing_and_retrieval_with_llama_index_from_files())
