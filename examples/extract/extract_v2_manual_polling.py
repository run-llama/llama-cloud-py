"""Extract V2: manual polling with citations and confidence."""

from __future__ import annotations

import asyncio
import json

from llama_cloud import AsyncLlamaCloud


async def main() -> None:
    client = AsyncLlamaCloud()

    # Upload a file
    file_obj = await client.files.create(
        file="test-files/receipt/noisebridge_receipt.pdf",
        purpose="extract",
    )

    schema = {
        "type": "object",
        "properties": {
            "vendor": {"type": "string", "description": "Vendor name"},
            "total": {"type": "number", "description": "Total amount"},
            "date_paid": {"type": "string", "description": "Payment date"},
        },
    }

    # Create job with citations and confidence enabled
    job = await client.extract.create(
        document_input_value=file_obj.id,
        configuration={
            "tier": "agentic",
            "data_schema": schema,
            "extraction_target": "per_doc",
            "cite_sources": True,
            "confidence_scores": True,
        },
    )
    print(f"Job created: {job.id}")

    # Poll until terminal status
    while job.status not in ("COMPLETED", "FAILED", "CANCELLED"):
        await asyncio.sleep(3)
        job = await client.extract.get(job.id)
        print(f"  status: {job.status}")

    if job.status != "COMPLETED":
        print(f"Job failed: {job.error_message}")
        return

    # Show result
    print(f"\nResult:\n{json.dumps(job.extract_result, indent=2)}")

    # Fetch metadata (citations + confidence)
    detailed = await client.extract.get(job.id, expand=["extract_metadata"])
    if detailed.extract_metadata and detailed.extract_metadata.field_metadata:
        doc_meta = detailed.extract_metadata.field_metadata.document_metadata
        if doc_meta:
            print("\nPer-field citations:")
            for field_name, meta in doc_meta.items():
                if isinstance(meta, dict):
                    citations = meta.get("citation", [])
                    confidence = meta.get("confidence")
                    if citations:
                        c = citations[0]
                        print(f"  {field_name}: page={c.get('page')}, confidence={confidence}")


if __name__ == "__main__":
    asyncio.run(main())
