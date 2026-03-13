import asyncio
from typing import Optional

from pydantic import Field, BaseModel

from llama_cloud import AsyncLlamaCloud


class Models(BaseModel):
    model_names: Optional[list[str]] = Field(description="List of models mentioned.")


async def extract_document() -> None:
    client = AsyncLlamaCloud()

    # Upload a file for extraction
    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="extract",
    )

    # Run extraction end-to-end (creates job, polls until complete)
    result = await client.extract.run(
        type="file_id",
        value=file_obj.id,
        config={
            "extract_options": {
                "data_schema": Models.model_json_schema(),
            },
        },
        verbose=True,
    )

    print("Status:", result.status)
    print("Result:", result.extract_result)


if __name__ == "__main__":
    asyncio.run(extract_document())
