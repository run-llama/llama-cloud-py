# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["PageScreenshotNodeWithScore", "Node"]


class Node(BaseModel):
    file_id: str
    """The ID of the file that the page screenshot was taken from"""

    image_size: int
    """The size of the image in bytes"""

    page_index: int
    """The index of the page for which the screenshot is taken (0-indexed)"""

    metadata: Optional[Dict[str, object]] = None
    """Metadata for the screenshot"""


class PageScreenshotNodeWithScore(BaseModel):
    """Page screenshot metadata with score"""

    node: Node

    score: float
    """The score of the screenshot node"""

    class_name: Optional[str] = None
