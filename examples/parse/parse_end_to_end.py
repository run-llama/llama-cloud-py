import asyncio

from llama_cloud import AsyncLlamaCloud


async def parse_document() -> None:
    client = AsyncLlamaCloud()

    # Upload and parse a document
    result = await client.parsing.parse(
        upload_file="../example_files/attention_is_all_you_need.pdf",
        tier="agentic",
        version="latest",
        expand=["text", "markdown", "items"],
    )

    print(result.text)
    print(result.markdown)

    if result.items:
        print(result.items.pages[0])


if __name__ == "__main__":
    asyncio.run(parse_document())
