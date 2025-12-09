# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..file import File
from ..._models import BaseModel
from .extract_config import ExtractConfig

__all__ = ["ExtractRun"]


class ExtractRun(BaseModel):
    """Schema for an extraction run."""

    id: str
    """The id of the extraction run"""

    config: ExtractConfig
    """The config used for extraction"""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """The schema used for extraction"""

    extraction_agent_id: str
    """The id of the extraction agent"""

    from_ui: bool
    """Whether this extraction run was triggered from the UI"""

    project_id: str
    """The id of the project that the extraction run belongs to"""

    status: Literal["CREATED", "PENDING", "SUCCESS", "ERROR"]
    """The status of the extraction run"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    data: Union[
        Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]],
        List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]],
        None,
    ] = None
    """The data extracted from the file"""

    error: Optional[str] = None
    """The error that occurred during extraction"""

    extraction_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """The metadata extracted from the file"""

    file: Optional[File] = None
    """Schema for a file."""

    file_id: Optional[str] = None
    """The id of the file that the extract was extracted from"""

    job_id: Optional[str] = None
    """The id of the job that the extraction run belongs to"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
