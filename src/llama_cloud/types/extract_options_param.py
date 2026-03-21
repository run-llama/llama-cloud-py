# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractOptionsParam"]


class ExtractOptionsParam(TypedDict, total=False):
    """Extract-specific configuration options."""

    data_schema: Required[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """JSON schema for structured extraction"""

    cite_sources: bool
    """Include citations in results"""

    confidence_scores: bool
    """Include confidence scores in results"""

    extract_version: str
    """Extraction algorithm version to use (e.g., '2026-01-08', 'latest')"""

    extraction_target: Literal["per_doc", "per_page", "per_table_row"]
    """Extraction scope: per_doc, per_page, or per_table_row"""

    lang: str
    """Language of the document"""

    max_pages: Optional[int]
    """Maximum number of pages to process"""

    system_prompt: Optional[str]
    """Custom system prompt for extraction"""

    target_pages: Optional[str]
    """
    Comma-separated list of page numbers or ranges to process (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10')
    """

    tier: Literal["cost_effective", "agentic"]
    """Extraction tier: cost_effective (5 credits/page) or agentic (15 credits/page)"""
