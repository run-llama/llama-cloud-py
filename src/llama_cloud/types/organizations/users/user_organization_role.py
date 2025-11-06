# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...role import Role
from ...._models import BaseModel

__all__ = ["UserOrganizationRole"]


class UserOrganizationRole(BaseModel):
    id: str
    """Unique identifier"""

    organization_id: str
    """The organization's ID."""

    role: Role
    """The role."""

    user_id: str
    """The user's ID."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    project_ids: Optional[List[str]] = None
    """The project ID scope."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
