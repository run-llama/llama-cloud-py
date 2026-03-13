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

    # Create the extraction job
    job = await client.extract.create(
        type="file_id",
        value=file_obj.id,
        config={
            "extract_options": {
                "data_schema": Models.model_json_schema(),
            },
        },
    )
    print(f"Created job {job.id} with status: {job.status}")

    # Wait for completion with custom polling settings
    completed = await client.extract.wait_for_completion(
        job.id,
        polling_interval=2.0,
        verbose=True,
    )

    print("Status:", completed.status)
    print("Result:", completed.extract_result)


if __name__ == "__main__":
    asyncio.run(extract_document())
