# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pipelines.pipeline_file import PipelineFile

__all__ = ["PipelineRetrieveFiles2Response"]


class PipelineRetrieveFiles2Response(BaseModel):
    files: List[PipelineFile]
    """The files to list"""

    limit: int
    """The limit of the files"""

    offset: int
    """The offset of the files"""

    total_count: int
    """The total number of files"""
