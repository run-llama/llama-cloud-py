# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileGeneratePresignedURLResponse"]


class FileGeneratePresignedURLResponse(BaseModel):
    """Schema for a presigned URL with a file ID."""

    expires_at: datetime
    """The time at which the presigned URL expires"""

    file_id: str
    """The ID of the file associated with the presigned URL"""

    url: str
    """A presigned URL for IO operations against a private file"""

    form_fields: Optional[Dict[str, str]] = None
    """Form fields for a presigned POST request"""
