import asyncio

from llama_cloud import AsyncLlamaCloud


async def parse_document() -> None:
    client = AsyncLlamaCloud()

    # Upload a file and parse
    file_obj = await client.files.create(file="../example_files/attention_is_all_you_need.pdf", purpose="parse")

    # Upload and parse a document
    parse_job = await client.parsing.create(
        file_id=file_obj.id,
        tier="agentic",
        version="latest",
    )

    result = await client.parsing.get(parse_job.id, expand=["text", "markdown", "items"])
    while result.job.status in ("PENDING", "RUNNING"):
        print(f"Job status: {result.job.status}. Waiting...")
        await asyncio.sleep(3)
        result = await client.parsing.get(parse_job.id, expand=["text", "markdown", "items"])

    print(result.text)
    print(result.markdown)

    if result.items:
        print(result.items.pages[0])


if __name__ == "__main__":
    asyncio.run(parse_document())
