# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ParsingJobStructuredResult"]


class ParsingJobStructuredResult(BaseModel):
    """Response schema for parsing job structured result."""

    job_metadata: object
    """Parsing job metadata, including usage"""

    structured: object
    """The json result of the structured parsing job"""
