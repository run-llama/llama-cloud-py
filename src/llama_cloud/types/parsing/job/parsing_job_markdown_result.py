# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ParsingJobMarkdownResult"]


class ParsingJobMarkdownResult(BaseModel):
    """Response schema for parsing job markdown result."""

    job_metadata: object
    """Parsing job metadata, including usage"""

    markdown: str
    """The markdown result of the parsing job"""
