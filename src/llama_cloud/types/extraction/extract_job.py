# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..file import File
from ..._models import BaseModel
from .extract_agent import ExtractAgent

__all__ = ["ExtractJob"]


class ExtractJob(BaseModel):
    """Schema for an extraction job."""

    id: str
    """The id of the extraction job"""

    extraction_agent: ExtractAgent
    """The agent that the job was run on."""

    status: Literal["PENDING", "SUCCESS", "ERROR", "PARTIAL_SUCCESS", "CANCELLED"]
    """The status of the extraction job"""

    error: Optional[str] = None
    """The error that occurred during extraction"""

    file: Optional[File] = None
    """Schema for a file."""

    file_id: Optional[str] = None
    """The id of the file that the extract was extracted from"""
