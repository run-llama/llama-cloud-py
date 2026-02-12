# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BatchListParams"]


class BatchListParams(TypedDict, total=False):
    directory_id: Optional[str]
    """Filter by directory ID"""

    job_type: Optional[Literal["parse", "extract", "classify"]]
    """Filter by job type (PARSE, EXTRACT, CLASSIFY)"""

    limit: int
    """Maximum number of jobs to return"""

    offset: int
    """Number of jobs to skip for pagination"""

    organization_id: Optional[str]

    project_id: Optional[str]

    status: Optional[Literal["pending", "running", "dispatched", "completed", "failed", "cancelled"]]
    """Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)"""
