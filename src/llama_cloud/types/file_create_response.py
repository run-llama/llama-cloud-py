# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    """Schema for a file in the v2 API."""

    id: str
    """Unique identifier"""

    name: str

    project_id: str
    """The ID of the project that the file belongs to"""

    expires_at: Optional[datetime] = None
    """The expiration date for the file. Files past this date can be deleted."""

    external_file_id: Optional[str] = None
    """The ID of the file in the external system"""

    file_type: Optional[str] = None
    """File type (e.g. pdf, docx, etc.)"""

    last_modified_at: Optional[datetime] = None
    """The last modified time of the file"""

    purpose: Optional[str] = None
    """
    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract',
    'split', 'classify', 'sheet', 'agent_app')
    """
