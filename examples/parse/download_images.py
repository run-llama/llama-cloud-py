import re
import asyncio

from llama_cloud import AsyncLlamaCloud


def is_page_screenshot(name: str) -> bool:
    return bool(re.match(r"^page_\d+\.(png|jpg|jpeg)$", name))


async def main():
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

    # Get the images from the json result
    json_data = await client.parsing.job.result.get_json(job_id=job.id)
    for page in json_data.pages:
        for image in page["images"]:
            # Only download page screenshots for now
            if not is_page_screenshot(image["name"]):
                continue

            image_resp = await client.parsing.job.result.get_image(name=image["name"], job_id=job.id)
            await image_resp.write_to_file(f"./downloaded_{image['name']}")
            print(f"Downloaded image: {image['name']}")


if __name__ == "__main__":
    asyncio.run(main())
