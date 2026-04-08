# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SplitDocumentInput"]


class SplitDocumentInput(BaseModel):
    """Document input specification for beta API."""

    type: str
    """Type of document input. Valid values are: file_id"""

    value: str
    """Document identifier."""
