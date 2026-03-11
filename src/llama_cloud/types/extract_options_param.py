# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractOptionsParam"]


class ExtractOptionsParam(TypedDict, total=False):
    """Extract-specific configuration options."""

    data_schema: Required[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """JSON schema used for extraction"""

    cite_sources: bool
    """Include citations in results"""

    confidence_scores: bool
    """Include confidence scores in results"""

    extract_version: str
    """Extraction algorithm version to use (e.g., '2026-01-08', 'latest')"""

    extraction_target: Literal["per_doc", "per_page", "per_table_row"]
    """Extraction scope: per_doc, per_page, or per_table_row"""

    system_prompt: Optional[str]
    """Custom system prompt for extraction"""

    tier: Literal["cost_effective", "agentic"]
    """Extraction tier: cost_effective (10 credits) or agentic (20 credits)"""
