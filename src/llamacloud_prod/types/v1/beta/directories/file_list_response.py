# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["FileListResponse", "Item"]


class Item(BaseModel):
    id: str
    """Unique identifier for the directory file."""

    directory_id: str
    """Directory the file belongs to."""

    display_name: str
    """Display name for the file."""

    project_id: str
    """Project the directory file belongs to."""

    unique_id: str
    """Unique identifier for the file in the directory"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    data_source_id: Optional[str] = None
    """Optional data source credential associated with the file."""

    deleted_at: Optional[datetime] = None
    """Soft delete marker when the file is removed upstream or by user action."""

    file_id: Optional[str] = None
    """File ID for the storage location."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class FileListResponse(BaseModel):
    items: List[Item]
    """The list of items."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page.

    If this field is omitted, there are no subsequent pages.
    """

    total_size: Optional[int] = None
    """The total number of items available.

    This is only populated when specifically requested. The value may be an estimate
    and can be used for display purposes only.
    """
