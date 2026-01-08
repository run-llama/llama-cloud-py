# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ImageListPageScreenshotsResponse", "ImageListPageScreenshotsResponseItem"]


class ImageListPageScreenshotsResponseItem(BaseModel):
    file_id: str
    """The ID of the file that the page screenshot was taken from"""

    image_size: int
    """The size of the image in bytes"""

    page_index: int
    """The index of the page for which the screenshot is taken (0-indexed)"""

    metadata: Optional[Dict[str, object]] = None
    """Metadata for the screenshot"""


ImageListPageScreenshotsResponse: TypeAlias = List[ImageListPageScreenshotsResponseItem]
