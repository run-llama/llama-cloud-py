# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParsingListResponse"]


class ParsingListResponse(BaseModel):
    """Response schema for a parse job."""

    id: str
    """Unique identifier for the parse job"""

    parameters: Dict[str, object]
    """Job-specific parameters as JSON"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["pending", "running", "completed", "failed", "cancelled"]
    """
    Current status of the job (e.g., pending, running, completed, failed, cancelled)
    """

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
