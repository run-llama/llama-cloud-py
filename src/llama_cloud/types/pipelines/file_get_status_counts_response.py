# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["FileGetStatusCountsResponse"]


class FileGetStatusCountsResponse(BaseModel):
    counts: Dict[str, int]
    """The counts of files by status"""

    total_count: int
    """The total number of files"""

    data_source_id: Optional[str] = None
    """The ID of the data source that the files belong to"""

    only_manually_uploaded: Optional[bool] = None
    """Whether to only count manually uploaded files"""

    pipeline_id: Optional[str] = None
    """The ID of the pipeline that the files belong to"""
