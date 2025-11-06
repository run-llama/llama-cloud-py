# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .users.user_organization_role import UserOrganizationRole

__all__ = ["UserOrganization"]


class UserOrganization(BaseModel):
    id: str
    """Unique identifier"""

    organization_id: str
    """The organization's ID."""

    roles: List[UserOrganizationRole]
    """The roles of the user in the organization."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    email: Optional[str] = None
    """The user's email address."""

    invited_by_user_email: Optional[str] = None
    """The email address of the user who added the user to the organization."""

    invited_by_user_id: Optional[str] = None
    """The user ID of the user who added the user to the organization."""

    pending: Optional[bool] = None
    """Whether the user's membership is pending account signup."""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    user_id: Optional[str] = None
    """The user's ID."""
