# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DirectoryGetResponse"]


class DirectoryGetResponse(BaseModel):
    """API response schema for a directory."""

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
