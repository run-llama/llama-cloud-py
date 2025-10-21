# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .batch import Batch
from ...._models import BaseModel

__all__ = ["BatchListResponse"]


class BatchListResponse(BaseModel):
    data: List[Batch]
    """List of batches"""

    limit: int
    """Pagination limit"""

    offset: int
    """Pagination offset"""

    total_count: int
    """Total number of batches"""
