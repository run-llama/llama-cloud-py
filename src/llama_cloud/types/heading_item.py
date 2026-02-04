# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = ["HeadingItem"]


class HeadingItem(BaseModel):
    level: int
    """Heading level (1-6)"""

    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Heading text content"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["heading"]] = None
    """Heading item type"""
