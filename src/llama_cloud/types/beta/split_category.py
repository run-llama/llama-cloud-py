# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SplitCategory"]


class SplitCategory(BaseModel):
    """Category definition for document splitting."""

    name: str
    """Name of the category."""

    description: Optional[str] = None
    """Optional description of what content belongs in this category."""
