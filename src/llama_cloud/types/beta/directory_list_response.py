# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DirectoryListResponse", "Item"]


class Item(BaseModel):
    id: str
    """Unique identifier for the directory."""

    name: str
    """Human-readable name for the directory."""

    project_id: str
    """Project the directory belongs to."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    data_source_id: Optional[str] = None
    """Optional data source id the directory syncs from. Null if just manual uploads."""

    deleted_at: Optional[datetime] = None
    """Optional timestamp of when the directory was deleted. Null if not deleted."""

    description: Optional[str] = None
    """Optional description shown to users."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class DirectoryListResponse(BaseModel):
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
