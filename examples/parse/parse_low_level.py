import asyncio

from llama_cloud import AsyncLlamaCloud


async def main() -> None:
    client = AsyncLlamaCloud()

    # Or, upload without directly waiting
    job = await client.parsing.upload_file(
        # The file to parse
        file="../example_files/attention_is_all_you_need.pdf",
        parse_mode="parse_page_with_agent",
        model="openai-gpt-4-1-mini",
        high_res_ocr=True,
        adaptive_long_table=True,
        outlined_table_extraction=True,
        precise_bounding_box=True,
    )

    # Poll for completion
    while True:
        job_result = await client.parsing.job.get(job_id=job.id)
        if job_result.status != "PENDING":
            break
        print(f"Job status: {job_result.status}. Waiting...")
        await asyncio.sleep(3)

    # Get the result you want
    text = await client.parsing.job.result.get_text(job_id=job.id)
    print(text)

    markdown = await client.parsing.job.result.get_markdown(job_id=job.id)
    print(markdown)

    json_data = await client.parsing.job.result.get_json(job_id=job.id)
    print(json_data.pages[0].keys())


if __name__ == "__main__":
    asyncio.run(main())
