# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .classify_result import ClassifyResult
from .classify_configuration import ClassifyConfiguration

__all__ = ["ClassifyListResponse"]


class ClassifyListResponse(BaseModel):
    """Response for a classify job."""

    id: str
    """Unique identifier"""

    configuration: ClassifyConfiguration
    """Classification configuration"""

    document_input_type: Literal["url", "file_id", "parse_job_id"]
    """Type of document input"""

    document_input_value: str
    """Document identifier"""

    project_id: str
    """Project ID"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]
    """Job status"""

    user_id: str
    """User ID"""

    configuration_id: Optional[str] = None
    """Product configuration ID"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    parse_job_id: Optional[str] = None
    """Associated parse job ID"""

    result: Optional[ClassifyResult] = None
    """Result of classifying a document."""

    transaction_id: Optional[str] = None
    """Idempotency key"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
