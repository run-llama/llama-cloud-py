"""Extract V2: end-to-end example with Pydantic schema."""

from __future__ import annotations

import asyncio

from pydantic import BaseModel, Field

from llama_cloud import AsyncLlamaCloud


class InvoiceSchema(BaseModel):
    vendor_name: str = Field(description="Name of the vendor or merchant")
    total_amount: float = Field(description="Total amount charged")
    date: str | None = Field(default=None, description="Invoice or payment date")


async def main() -> None:
    client = AsyncLlamaCloud()

    # Upload a file
    file_obj = await client.files.create(
        file="test-files/receipt/noisebridge_receipt.pdf",
        purpose="extract",
    )

    # Create an extraction job with a Pydantic-derived schema
    job = await client.extract.create(
        document_input_value=file_obj.id,
        configuration={
            "tier": "cost_effective",
            "data_schema": InvoiceSchema.model_json_schema(),
            "extraction_target": "per_doc",
        },
    )
    print(f"Job created: {job.id}")

    # Wait for completion
    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        await asyncio.sleep(3)
        job = await client.extract.get(job.id)
        print(f"  status: {job.status}")

    # Validate result with Pydantic
    if job.extract_result:
        invoice = InvoiceSchema.model_validate(job.extract_result)
        print(f"\nVendor: {invoice.vendor_name}")
        print(f"Total: ${invoice.total_amount:.2f}")
        print(f"Date: {invoice.date}")


if __name__ == "__main__":
    asyncio.run(main())
