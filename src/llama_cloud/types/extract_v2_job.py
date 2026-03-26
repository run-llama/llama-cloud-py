# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from .._models import BaseModel
from .extract_job_metadata import ExtractJobMetadata
from .extract_configuration import ExtractConfiguration

__all__ = ["ExtractV2Job"]


class ExtractV2Job(BaseModel):
    """An extraction job."""

    id: str
    """Unique job identifier (job_id)"""

    created_at: datetime
    """Creation timestamp"""

    document_input_value: str
    """File ID or parse job ID that was extracted"""

    project_id: str
    """Project this job belongs to"""

    status: str
    """Current job status.

    - `PENDING` — queued, not yet started
    - `RUNNING` — actively processing
    - `COMPLETED` — finished successfully
    - `FAILED` — terminated with an error
    - `CANCELLED` — cancelled by user
    """

    updated_at: datetime
    """Last update timestamp"""

    configuration: Optional[ExtractConfiguration] = None
    """Extract configuration combining parse and extract settings."""

    configuration_id: Optional[str] = None
    """Saved extract configuration ID used for this job, if any"""

    error_message: Optional[str] = None
    """Error details when status is FAILED"""

    extract_metadata: Optional[ExtractJobMetadata] = None
    """Extraction metadata."""

    extract_result: Union[
        Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]],
        List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]],
        None,
    ] = None
    """Extracted data conforming to the data_schema.

    Returns a single object for per_doc, or an array for per_page / per_table_row.
    """
