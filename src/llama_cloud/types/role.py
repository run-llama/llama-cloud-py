# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Role", "Permission"]


class Permission(BaseModel):
    id: str
    """Unique identifier"""

    access: bool
    """Whether the permission is granted or not."""

    description: Optional[str] = None
    """A description for the permission."""

    name: str
    """A name for the permission."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class Role(BaseModel):
    id: str
    """Unique identifier"""

    name: str
    """A name for the role."""

    permissions: List[Permission]
    """The actual permissions of the role."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
