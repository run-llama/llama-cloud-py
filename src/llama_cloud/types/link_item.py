# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = ["LinkItem"]


class LinkItem(BaseModel):
    md: str
    """Markdown representation preserving formatting"""

    text: str
    """Display text of the link"""

    url: str
    """URL of the link"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["link"]] = None
    """Link item type"""
