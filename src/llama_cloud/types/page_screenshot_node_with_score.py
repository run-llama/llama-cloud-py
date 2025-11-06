# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .files.page_screenshot_metadata import PageScreenshotMetadata

__all__ = ["PageScreenshotNodeWithScore"]


class PageScreenshotNodeWithScore(BaseModel):
    node: PageScreenshotMetadata

    score: float
    """The score of the screenshot node"""

    class_name: Optional[str] = None
