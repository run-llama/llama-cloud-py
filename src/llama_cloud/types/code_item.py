# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = ["CodeItem"]


class CodeItem(BaseModel):
    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Code content"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    language: Optional[str] = None
    """Programming language identifier"""

    type: Optional[Literal["code"]] = None
    """Code block item type"""
