# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PresignedURL"]


class PresignedURL(BaseModel):
    """Schema for a presigned URL."""

    expires_at: datetime
    """The time at which the presigned URL expires"""

    url: str
    """A presigned URL for IO operations against a private file"""

    form_fields: Optional[Dict[str, str]] = None
    """Form fields for a presigned POST request"""
