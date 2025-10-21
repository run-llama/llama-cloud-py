# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: str
    """Unique identifier"""

    name: str
    """A name for the organization."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    feature_flags: Optional[Dict[str, object]] = None
    """Feature flags for the organization."""

    parse_plan_level: Optional[Literal["DEFAULT", "PREMIUM"]] = None
    """Whether the organization is a Parse Premium customer."""

    stripe_customer_id: Optional[str] = None
    """The Stripe customer ID for the organization."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
