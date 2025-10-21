# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .batch import Batch
from ...._models import BaseModel
from ..managed_ingestion_status_response import ManagedIngestionStatusResponse

__all__ = ["BatchRetrieveResponse", "BatchItem", "BatchItemTask"]


class BatchItemTask(BaseModel):
    created_at: datetime
    """The date and time when the file was parsed."""

    data_path: str
    """The path to the data file."""

    input_path: str
    """The path to the input file."""

    status: str
    """The status of the parse task."""

    ended_at: Optional[datetime] = None
    """The date and time when the file parse ended."""

    started_at: Optional[datetime] = None
    """The date and time when the file parse started."""


class BatchItem(BaseModel):
    id: str
    """Unique identifier for the batch item"""

    batch_id: str
    """The ID of the batch to which the item belongs"""

    input_file: str
    """The input file associated with the batch item"""

    status: str
    """The current status of the batch item"""

    created_at: Optional[datetime] = None
    """The Unix timestamp (in seconds) for when the batch item was created"""

    output_file: Optional[str] = None
    """The output file associated with the batch item"""

    status_updated_at: Optional[datetime] = None
    """The Unix timestamp (in seconds) for when the batch item status was last updated"""

    task: Optional[BatchItemTask] = None
    """Worker Task for that item"""

    updated_at: Optional[datetime] = None
    """The Unix timestamp (in seconds) for when the batch item was last updated"""


class BatchRetrieveResponse(BaseModel):
    batch: Batch

    batch_items: List[BatchItem]

    ingestion_status: ManagedIngestionStatusResponse
