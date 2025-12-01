import asyncio

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types import RetrieverPipelineParam, PresetRetrievalParamsParam


async def retrieve_from_existing_index_pipeline() -> None:
    client = AsyncLlamaCloud()

    # Retrieve directly from the index pipeline
    results = await client.pipelines.retrieve(
        pipeline_id="your-existing-pipeline-id",
        query="What are the key concepts of the document?",
        dense_similarity_top_k=20,
        sparse_similarity_top_k=20,
        alpha=0.5,
        enable_reranking=True,
        rerank_top_n=5,
    )

    for n in results.retrieval_nodes:
        print(f"Score: {n.score}, Text: {n.node.text}")

    # Create a named retrieval configuration for reuse
    # Can combine one or more pipelines in a single retriever
    retriver = await client.retrievers.create(
        name="my-retriever",
        pipelines=[
            RetrieverPipelineParam(
                name="my-pipeline-retriever",
                description="Contains information about XYZ",
                pipeline_id="your-existing-pipeline-id",
                preset_retrieval_parameters=PresetRetrievalParamsParam(
                    dense_similarity_top_k=20,
                    sparse_similarity_top_k=20,
                    alpha=0.5,
                    enable_reranking=True,
                    rerank_top_n=5,
                ),
            )
        ],
    )

    # Use the retriever to search across its pipelines
    combined_results = await client.retrievers.retriever.search(
        retriever_id=retriver.id,
        query="Summarize the main points of the document.",
        # "full" or "routing" -- decides whether to use all pipelines or route to a specific one
        mode="full",
        # Set the top-n of all pipelines in the retriever
        rerank_top_n=3,
    )

    for n in combined_results.nodes or []:
        print(f"Score: {n.score}, Text: {n.node.text}")


if __name__ == "__main__":
    asyncio.run(retrieve_from_existing_index_pipeline())
