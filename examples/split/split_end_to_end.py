import asyncio

from llama_cloud import AsyncLlamaCloud


async def split_document() -> None:
    """
    Example demonstrating how to split a concatenated PDF into logical document
    sections based on content categories.

    This example uses a PDF containing three concatenated documents:
    - Alan Turing's essay "Intelligent Machinery, A Heretical Theory"
    - ImageNet paper (a research paper)
    - "Attention is All You Need" paper (a research paper)

    The Split API uses AI to:
    1. Analyze each page's content
    2. Classify pages into user-defined categories
    3. Group consecutive pages of the same category into segments
    """
    client = AsyncLlamaCloud()

    # Upload a file to split
    file_obj = await client.files.create(file="../example_files/turing+imagenet+attention.pdf", purpose="split")
    file_id = file_obj.id

    # Split the document and wait for completion
    # Each category needs a name and a description that helps the AI
    # understand what content belongs to that category
    result = await client.beta.split.split(
        categories=[
            {
                "name": "essay",
                "description": "A philosophical or reflective piece of writing that presents personal viewpoints, arguments, or thoughts on a topic without strict formal structure",
            },
            {
                "name": "research_paper",
                "description": "A formal academic document presenting original research, methodology, experiments, results, and conclusions with citations and references",
            },
        ],
        document_input={"type": "file_id", "value": file_id},
        verbose=True,
    )

    # Print the splitting results
    print(f"Split job completed with status: {result.status}")
    print()

    if result.result:
        print(f"📊 Total segments found: {len(result.result.segments)}")
        for i, segment in enumerate(result.result.segments, 1):
            pages = segment.pages
            if len(pages) == 1:
                page_range = f"Page {pages[0]}"
            else:
                page_range = f"Pages {min(pages)}-{max(pages)}"

            print(f"\nSegment {i}:")
            print(f"   Category: {segment.category}")
            print(f"   {page_range} ({len(pages)} pages)")
            print(f"   Confidence: {segment.confidence_category}")


if __name__ == "__main__":
    asyncio.run(split_document())
