# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileAddParams"]


class FileAddParams(TypedDict, total=False):
    file_id: Required[str]
    """File ID for the storage location (required)."""

    organization_id: Optional[str]

    project_id: Optional[str]

    display_name: Optional[str]
    """Display name for the file. If not provided, will use the file's name."""

    unique_id: Optional[str]
    """Unique identifier for the file in the directory.

    If not provided, will use the file's external_file_id or name.
    """
