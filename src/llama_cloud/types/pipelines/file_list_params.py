# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    data_source_id: Optional[str]

    file_name_contains: Optional[str]

    limit: Optional[int]

    offset: Optional[int]

    only_manually_uploaded: bool

    order_by: Optional[str]
