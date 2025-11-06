# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .extract_run import ExtractRun

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    items: List[ExtractRun]
    """The list of extraction runs"""

    limit: int
    """The maximum number of extraction runs returned"""

    skip: int
    """The number of extraction runs skipped"""

    total: int
    """The total number of extraction runs"""
