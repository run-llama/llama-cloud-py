# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ParsingJobTextResult"]


class ParsingJobTextResult(BaseModel):
    """Response schema for parsing job text result."""

    job_metadata: object
    """Parsing job metadata, including usage"""

    text: str
    """The text result of the parsing job"""
