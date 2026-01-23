# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .b_box import BBox
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["ListItem", "Item", "ItemTextItem"]


class ItemTextItem(BaseModel):
    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Text content"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType("Item", Union[ItemTextItem, "ListItem"])
else:
    Item: TypeAlias = Union[ItemTextItem, "ListItem"]


class ListItem(BaseModel):
    items: List[Item]
    """List of nested text or list items"""

    md: str
    """Markdown representation preserving formatting"""

    ordered: bool
    """Whether the list is ordered or unordered"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["list"]] = None
    """List item type"""
