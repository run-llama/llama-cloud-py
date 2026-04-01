# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..status_enum import StatusEnum

__all__ = ["SheetListParams"]


class SheetListParams(TypedDict, total=False):
    created_at_on_or_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or after this timestamp (inclusive)"""

    created_at_on_or_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include items created at or before this timestamp (inclusive)"""

    include_results: bool

    job_ids: Optional[SequenceNotStr[str]]
    """Filter by specific job IDs"""

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    status: Optional[StatusEnum]
    """Filter by job status"""
