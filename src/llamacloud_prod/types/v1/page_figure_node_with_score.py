# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .files.page_figure_metadata import PageFigureMetadata

__all__ = ["PageFigureNodeWithScore"]


class PageFigureNodeWithScore(BaseModel):
    node: PageFigureMetadata

    score: float
    """The score of the figure node"""

    class_name: Optional[str] = None
