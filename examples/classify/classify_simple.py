import asyncio

from llama_cloud import AsyncLlamaCloud
from llama_cloud.types.classifier import ClassifierRuleParam


async def classify_document():
    client = AsyncLlamaCloud()

    # Upload a file
    file_obj = await client.files.upload(upload_file="../example_files/attention_is_all_you_need.pdf")
    file_id = file_obj.id

    # Upload and wait for completion
    result = await client.classifier.classify(
        file_ids=[file_id],
        rules=[
            ClassifierRuleParam(
                type="ACADEMIC_PAPER",
                description="Classify whether the document is an academic paper.",
            ),
            ClassifierRuleParam(
                type="OTHER",
                description="Classify whether the document is from any other source besides academic papers.",
            ),
        ],
    )

    # Print the classification results
    for item in result.items:
        assert item.result is not None
        print(f"Classified type: {item.result.type}")
        print(f"Confidence: {item.result.confidence}")
        print(f"Reasoning: {item.result.reasoning}")


if __name__ == "__main__":
    asyncio.run(classify_document())
