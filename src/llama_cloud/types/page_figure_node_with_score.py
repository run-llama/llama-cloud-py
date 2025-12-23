# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["PageFigureNodeWithScore", "Node"]


class Node(BaseModel):
    confidence: float
    """The confidence of the figure"""

    figure_name: str
    """The name of the figure"""

    figure_size: int
    """The size of the figure in bytes"""

    file_id: str
    """The ID of the file that the figure was taken from"""

    page_index: int
    """The index of the page for which the figure is taken (0-indexed)"""

    is_likely_noise: Optional[bool] = None
    """Whether the figure is likely to be noise"""

    metadata: Optional[Dict[str, object]] = None
    """Metadata for the figure"""


class PageFigureNodeWithScore(BaseModel):
    """Page figure metadata with score"""

    node: Node

    score: float
    """The score of the figure node"""

    class_name: Optional[str] = None
