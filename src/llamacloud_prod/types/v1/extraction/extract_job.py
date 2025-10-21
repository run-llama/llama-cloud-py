# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..file import File
from ...._models import BaseModel
from ..status_enum import StatusEnum
from .extract_agent import ExtractAgent

__all__ = ["ExtractJob"]


class ExtractJob(BaseModel):
    id: str
    """The id of the extraction job"""

    extraction_agent: ExtractAgent
    """The agent that the job was run on."""

    file: File
    """The file that the extract was extracted from"""

    status: StatusEnum
    """The status of the extraction job"""

    error: Optional[str] = None
    """The error that occurred during extraction"""
