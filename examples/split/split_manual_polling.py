import asyncio

from llama_cloud import AsyncLlamaCloud


async def split_document() -> None:
    """
    Low-level example showing the individual steps:
    1. Create the split job
    2. Poll for completion
    3. Get the result

    This example demonstrates using allow_uncategorized to capture pages
    that don't match any defined category.
    """
    client = AsyncLlamaCloud()

    # Upload a file to split
    file_obj = await client.files.create(file="../example_files/turing+imagenet+attention.pdf", purpose="split")
    file_id = file_obj.id

    # Create the split job with only 'essay' category defined
    # Research papers will be grouped as 'uncategorized'
    job = await client.beta.split.create(
        categories=[
            {
                "name": "essay",
                "description": "A philosophical or reflective piece of writing that presents personal viewpoints",
            },
        ],
        document_input={"type": "file_id", "value": file_id},
        splitting_strategy={"allow_uncategorized": True},
    )

    print(f"Created split job: {job.id}")
    print(f"Initial status: {job.status}")

    # Wait for completion using the wait_for_completion method
    completed_job = await client.beta.split.wait_for_completion(
        job.id,
        polling_interval=1.0,
        verbose=True,
    )

    print(f"Final status: {completed_job.status}")

    if completed_job.result:
        print("\nDocument segments:")
        for segment in completed_job.result.segments:
            print(f"  Category: {segment.category}, Pages: {segment.pages}")


if __name__ == "__main__":
    asyncio.run(split_document())
