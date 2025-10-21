# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["V1GetJobsParams"]


class V1GetJobsParams(TypedDict, total=False):
    job_name: Optional[str]

    limit: int

    offset: int

    organization_id: Optional[str]

    project_id: Optional[str]

    sort: Optional[str]
