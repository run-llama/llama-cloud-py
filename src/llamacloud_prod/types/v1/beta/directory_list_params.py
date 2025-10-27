# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DirectoryListParams"]


class DirectoryListParams(TypedDict, total=False):
    data_source_id: Optional[str]

    include_deleted: bool

    name: Optional[str]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]
