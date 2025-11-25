# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["JobItemGetProcessingResultsParams"]


class JobItemGetProcessingResultsParams(TypedDict, total=False):
    job_type: Optional[Literal["parse", "extract", "classify"]]
    """Type of batch processing operation."""

    organization_id: Optional[str]

    project_id: Optional[str]
