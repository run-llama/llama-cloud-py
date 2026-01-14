import re
import asyncio

import httpx

from llama_cloud import AsyncLlamaCloud


def is_page_screenshot(image_name: str) -> bool:
    return re.match(r"^page_(\d+)\.jpg$", image_name) is not None


async def parse_document() -> None:
    client = AsyncLlamaCloud()

    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="parse",
    )

    # Upload and parse a document, requdesting image content metadata
    result = await client.parsing.parse(
        file_id=file_obj.id,
        tier="agentic",
        version="latest",
        output_options={
            "images_to_save": ["screenshot"],
        },
        expand=["images_content_metadata"],
    )

    if result.images_content_metadata:
        for image in result.images_content_metadata.images:
            if image.presigned_url is None or not is_page_screenshot(image.filename):
                continue

            print(f"Downloading {image.filename}, {image.size_bytes} bytes")
            with open(f"{image.filename}", "wb") as img_file:
                async with httpx.AsyncClient() as http_client:
                    response = await http_client.get(image.presigned_url)
                    img_file.write(response.content)


if __name__ == "__main__":
    asyncio.run(parse_document())
