# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ExtractListParams"]


class ExtractListParams(TypedDict, total=False):
    configuration_id: Optional[str]
    """Filter by configuration ID"""

    document_input_type: Optional[str]
    """Filter by document input type (file_id or parse_job_id)"""

    document_input_value: Optional[str]
    """Filter by document input value"""

    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page"""

    page_token: Optional[str]
    """Token for pagination"""

    project_id: Optional[str]

    status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]]
    """Filter by status"""
