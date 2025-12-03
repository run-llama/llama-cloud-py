import asyncio

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types.parsing.job import ParsingJobJsonResult, ParsingJobTextResult, ParsingJobMarkdownResult


async def get_json() -> None:
    client = AsyncLlamaCloud()

    # Upload and wait for completion
    result = await client.parsing.parse(
        # The file to parse
        file="../example_files/attention_is_all_you_need.pdf",
        parse_mode="parse_page_with_agent",
        model="openai-gpt-4-1-mini",
        high_res_ocr=True,
        adaptive_long_table=True,
        outlined_table_extraction=True,
        precise_bounding_box=True,
        result_type="json",
    )

    # Print various formats of the parsed result
    assert isinstance(result, ParsingJobJsonResult)
    print(result.pages)  # JSON result
    print(result.pages[0]["text"])
    print(result.pages[0]["markdown"])
    print(result.pages[0]["images"][0])


async def get_markdown() -> None:
    client = AsyncLlamaCloud()

    # Upload and wait for completion
    result = await client.parsing.parse(
        # The file to parse
        file="../example_files/attention_is_all_you_need.pdf",
        parse_mode="parse_page_with_agent",
        model="openai-gpt-4-1-mini",
        high_res_ocr=True,
        adaptive_long_table=True,
        outlined_table_extraction=True,
        precise_bounding_box=True,
        result_type="markdown",
    )

    # Print various formats of the parsed result
    assert isinstance(result, ParsingJobMarkdownResult)
    print(result.markdown)  # Markdown result


async def get_text() -> None:
    client = AsyncLlamaCloud()

    # Upload and wait for completion
    result = await client.parsing.parse(
        # The file to parse
        file="../example_files/attention_is_all_you_need.pdf",
        parse_mode="parse_page_with_agent",
        model="openai-gpt-4-1-mini",
        high_res_ocr=True,
        adaptive_long_table=True,
        outlined_table_extraction=True,
        precise_bounding_box=True,
        result_type="text",
    )

    # Print various formats of the parsed result
    assert isinstance(result, ParsingJobTextResult)
    print(result.text)  # text result


if __name__ == "__main__":
    asyncio.run(get_json())
    # get_markdown()
    # get_text()
