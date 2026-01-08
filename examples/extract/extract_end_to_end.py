from __future__ import annotations

import asyncio
from typing import Optional

from pydantic import Field, BaseModel

from llama_cloud import AsyncLlamaCloud


class Models(BaseModel):
    model_names: Optional[list[str]] = Field(description="List of models mentioned.")


async def extract_stateless() -> None:
    client = AsyncLlamaCloud()

    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="extract",
    )
    file_id = file_obj.id

    # Stateless one-shot extraction
    result = await client.extraction.extract(
        file_id=file_id,
        config={
            "chunk_mode": "PAGE",
            "cite_sources": True,
            "extraction_target": "PER_DOC",
            "extraction_mode": "PREMIUM",
        },
        data_schema=Models.model_json_schema(),
    )

    extracted_model = Models.model_validate(result.data)
    print("Extracted model names:", extracted_model.model_names)


async def extract_with_agent() -> None:
    client = AsyncLlamaCloud()

    file_obj = await client.files.create(
        file="../example_files/attention_is_all_you_need.pdf",
        purpose="extract",
    )
    file_id = file_obj.id

    # Create an extraction agent
    agent = await client.extraction.extraction_agents.create(
        config={
            "chunk_mode": "PAGE",
            "cite_sources": True,
            "extraction_target": "PER_DOC",
            "extraction_mode": "BALANCED",
        },
        data_schema=Models.model_json_schema(),
        name="My Extraction Agent",
    )

    # Use the extraction agent
    result = await client.extraction.jobs.extract(
        extraction_agent_id=agent.id,
        file_id=file_id,
    )

    extracted_model = Models.model_validate(result.data)
    print("Extracted model names with agent:", extracted_model.model_names)


if __name__ == "__main__":
    asyncio.run(extract_stateless())
    # asyncio.run(extract_with_agent())
