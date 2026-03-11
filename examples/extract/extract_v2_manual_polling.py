"""Extract V2 — manual polling with create() + wait_for_completion().

Demonstrates finer-grained control over the extraction workflow:
create the job, optionally inspect it, then poll for completion
with custom backoff settings.
"""
from __future__ import annotations

import asyncio
from typing import Optional

from pydantic import Field, BaseModel

from llama_cloud import AsyncLlamaCloud


class Models(BaseModel):
    model_names: Optional[list[str]] = Field(description="List of models mentioned.")


async def main() -> None:
    client = AsyncLlamaCloud()

    # Upload a file for extraction
    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="extract",
    )

    # Step 1: Create the extraction job
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

    # Step 2: Optionally inspect the job before waiting
    fetched = await client.extract.get(job_id=job.id)
    print(f"Current status: {fetched.status}")

    # Step 3: Wait for completion with custom polling settings
    completed = await client.extract.wait_for_completion(
        job.id,
        polling_interval=2.0,
        backoff="linear",
        verbose=True,
    )

    print("Status:", completed.status)
    print("Result:", completed.extract_result)

    # Step 4: List recent extract jobs
    page = client.extract.list()
    async for j in page:
        print(f"  Job {j.id}: {j.status}")
        break  # just show the first one


if __name__ == "__main__":
    asyncio.run(main())
