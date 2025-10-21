# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .api_key_type import APIKeyType

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """Unique identifier"""

    redacted_api_key: str

    user_id: str

    created_at: Optional[datetime] = None
    """Creation datetime"""

    key_type: Optional[APIKeyType] = None

    name: Optional[str] = None

    project_id: Optional[str] = None

    updated_at: Optional[datetime] = None
    """Update datetime"""
