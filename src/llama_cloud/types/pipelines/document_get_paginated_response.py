# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .cloud_document import CloudDocument

__all__ = ["DocumentGetPaginatedResponse"]


class DocumentGetPaginatedResponse(BaseModel):
    documents: List[CloudDocument]
    """The documents to list"""

    limit: int
    """The limit of the documents"""

    offset: int
    """The offset of the documents"""

    total_count: int
    """The total number of documents"""
