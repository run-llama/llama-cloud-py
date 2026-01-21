# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParsingListResponse"]


class ParsingListResponse(BaseModel):
    """Response schema for a parse job."""

    id: str
    """Unique identifier for the parse job"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """
    Current status of the job (e.g., pending, running, completed, failed, cancelled)
    """

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    name: Optional[str] = None
    """User friendly name"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
