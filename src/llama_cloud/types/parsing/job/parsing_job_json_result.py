# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ParsingJobJsonResult"]


class ParsingJobJsonResult(BaseModel):
    """Response schema for parsing job JSON result."""

    job_metadata: object
    """Parsing job metadata, including usage"""

    pages: object
    """The json result of the parsing job"""
