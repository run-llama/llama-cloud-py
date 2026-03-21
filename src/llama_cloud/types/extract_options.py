# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractOptions"]


class ExtractOptions(BaseModel):
    """Extract-specific configuration options."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """JSON schema for structured extraction"""

    cite_sources: Optional[bool] = None
    """Include citations in results"""

    confidence_scores: Optional[bool] = None
    """Include confidence scores in results"""

    extract_version: Optional[str] = None
    """Extraction algorithm version to use (e.g., '2026-01-08', 'latest')"""

    extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]] = None
    """Extraction scope: per_doc, per_page, or per_table_row"""

    lang: Optional[str] = None
    """Language of the document"""

    max_pages: Optional[int] = None
    """Maximum number of pages to process"""

    system_prompt: Optional[str] = None
    """Custom system prompt for extraction"""

    target_pages: Optional[str] = None
    """
    Comma-separated list of page numbers or ranges to process (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10')
    """

    tier: Optional[Literal["cost_effective", "agentic"]] = None
    """Extraction tier: cost_effective (5 credits/page) or agentic (15 credits/page)"""
