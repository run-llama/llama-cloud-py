# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ClassifyListParams"]


class ClassifyListParams(TypedDict, total=False):
    configuration_id: Optional[str]
    """Filter by configuration ID"""

    job_ids: Optional[SequenceNotStr[str]]
    """Filter by specific job IDs"""

    organization_id: Optional[str]

    page_size: Optional[int]
    """Number of items per page"""

    page_token: Optional[str]
    """Token for pagination"""

    project_id: Optional[str]

    status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]]
    """Filter by job status"""
