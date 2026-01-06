# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ImageGetPageFigureParams"]


class ImageGetPageFigureParams(TypedDict, total=False):
    id: Required[str]

    page_index: Required[int]

    organization_id: Optional[str]

    project_id: Optional[str]
