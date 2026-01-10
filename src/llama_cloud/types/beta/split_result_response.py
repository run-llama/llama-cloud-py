# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .split_segment_response import SplitSegmentResponse

__all__ = ["SplitResultResponse"]


class SplitResultResponse(BaseModel):
    """Result of a completed split job."""

    segments: List[SplitSegmentResponse]
    """List of document segments."""
