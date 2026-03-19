# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from .._models import BaseModel
from .extract_job_metadata import ExtractJobMetadata

__all__ = ["ExtractV2Job"]


class ExtractV2Job(BaseModel):
    """An extraction job."""

    id: str
    """Unique job identifier (job_id)"""

    created_at: datetime
    """Creation timestamp"""

    document_input_value: str
    """File ID or Parse Job ID used for this job"""

    parameters: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """Job configuration parameters (includes parse_config_id, extract_options)"""

    project_id: str
    """Project this job belongs to"""

    status: str
    """Current status: PENDING, THROTTLED, RUNNING, COMPLETED, FAILED, CANCELLED"""

    updated_at: datetime
    """Last update timestamp"""

    configuration_id: Optional[str] = None
    """Extract configuration ID (ProductConfiguration) used for this job (if any)"""

    error_message: Optional[str] = None
    """Error message if failed"""

    extract_metadata: Optional[ExtractJobMetadata] = None
    """Extraction metadata."""

    extract_result: Union[
        Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]],
        List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]],
        None,
    ] = None
    """Extracted data (object or array depending on extraction_target)"""
