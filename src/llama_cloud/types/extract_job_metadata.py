# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .extract_job_usage import ExtractJobUsage
from .extracted_field_metadata import ExtractedFieldMetadata

__all__ = ["ExtractJobMetadata"]


class ExtractJobMetadata(BaseModel):
    """Extraction metadata."""

    field_metadata: Optional[ExtractedFieldMetadata] = None
    """Metadata for extracted fields including document, page, and row level info."""

    parse_job_id: Optional[str] = None
    """Reference to the ParseJob ID used for parsing"""

    parse_tier: Optional[str] = None
    """Parse tier used for parsing the document"""

    usage: Optional[ExtractJobUsage] = None
    """Extraction usage metrics."""
