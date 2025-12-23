# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ExtractConfigParam"]


class ExtractConfigParam(TypedDict, total=False):
    """Configuration parameters for the extraction agent."""

    chunk_mode: Literal["PAGE", "SECTION"]
    """The mode to use for chunking the document."""

    citation_bbox: bool
    """Whether to fetch citation bounding boxes for the extraction.

    Only available in PREMIUM mode. Deprecated: this is now synonymous with
    cite_sources.
    """

    cite_sources: bool
    """Whether to cite sources for the extraction."""

    confidence_scores: bool
    """Whether to fetch confidence scores for the extraction."""

    extract_model: Union[
        Literal[
            "openai-gpt-4-1",
            "openai-gpt-4-1-mini",
            "openai-gpt-4-1-nano",
            "openai-gpt-5",
            "openai-gpt-5-mini",
            "gemini-2.0-flash",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "openai-gpt-4o",
            "openai-gpt-4o-mini",
        ],
        str,
        None,
    ]
    """The extract model to use for data extraction.

    If not provided, uses the default for the extraction mode.
    """

    extraction_mode: Literal["FAST", "BALANCED", "PREMIUM", "MULTIMODAL"]
    """The extraction mode specified (FAST, BALANCED, MULTIMODAL, PREMIUM)."""

    extraction_target: Literal["PER_DOC", "PER_PAGE", "PER_TABLE_ROW"]
    """The extraction target specified."""

    high_resolution_mode: bool
    """Whether to use high resolution mode for the extraction."""

    invalidate_cache: bool
    """Whether to invalidate the cache for the extraction."""

    multimodal_fast_mode: bool
    """DEPRECATED: Whether to use fast mode for multimodal extraction."""

    num_pages_context: Optional[int]
    """Number of pages to pass as context on long document extraction."""

    page_range: Optional[str]
    """
    Comma-separated list of page numbers or ranges to extract from (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10').
    """

    parse_model: Optional[
        Literal[
            "openai-gpt-4o",
            "openai-gpt-4o-mini",
            "openai-gpt-4-1",
            "openai-gpt-4-1-mini",
            "openai-gpt-4-1-nano",
            "openai-gpt-5",
            "openai-gpt-5-mini",
            "openai-gpt-5-nano",
            "openai-text-embedding-3-large",
            "openai-text-embedding-3-small",
            "openai-whisper-1",
            "anthropic-sonnet-3.5",
            "anthropic-sonnet-3.5-v2",
            "anthropic-sonnet-3.7",
            "anthropic-sonnet-4.0",
            "anthropic-sonnet-4.5",
            "anthropic-haiku-3.5",
            "anthropic-haiku-4.5",
            "gemini-2.5-flash",
            "gemini-3.0-pro",
            "gemini-2.5-pro",
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
            "gemini-2.5-flash-lite",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
        ]
    ]
    """Public model names."""

    priority: Optional[Literal["low", "medium", "high", "critical"]]
    """The priority for the request.

    This field may be ignored or overwritten depending on the organization tier.
    """

    system_prompt: Optional[str]
    """The system prompt to use for the extraction."""

    use_reasoning: bool
    """Whether to use reasoning for the extraction."""
