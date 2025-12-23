# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ParsingListParams"]


class ParsingListParams(TypedDict, total=False):
    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page"""

    page_token: Optional[str]
    """Token for pagination"""

    project_id: Optional[str]

    status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]]
    """Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)"""
