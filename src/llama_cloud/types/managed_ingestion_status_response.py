# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ManagedIngestionStatusResponse", "Error"]


class Error(BaseModel):
    job_id: str
    """ID of the job that failed."""

    message: str
    """List of errors that occurred during ingestion."""

    step: Literal[
        "MANAGED_INGESTION", "DATA_SOURCE", "FILE_UPDATER", "PARSE", "TRANSFORM", "INGESTION", "METADATA_UPDATE"
    ]
    """Name of the job that failed."""


class ManagedIngestionStatusResponse(BaseModel):
    status: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", "ERROR", "PARTIAL_SUCCESS", "CANCELLED"]
    """Status of the ingestion."""

    deployment_date: Optional[datetime] = None
    """Date of the deployment."""

    effective_at: Optional[datetime] = None
    """When the status is effective"""

    error: Optional[List[Error]] = None
    """List of errors that occurred during ingestion."""

    job_id: Optional[str] = None
    """ID of the latest job."""
