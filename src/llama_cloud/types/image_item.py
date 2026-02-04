# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = ["ImageItem"]


class ImageItem(BaseModel):
    caption: str
    """Image caption"""

    md: str
    """Markdown representation preserving formatting"""

    url: str
    """URL to the image"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["image"]] = None
    """Image item type"""
