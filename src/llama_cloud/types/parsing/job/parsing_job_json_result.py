# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, Dict, List

from ...._models import BaseModel

__all__ = ["ParsingJobJsonResult"]


class ParsingJobJsonResult(BaseModel):
    """Response schema for parsing job JSON result."""

    job_metadata: object
    """Parsing job metadata, including usage"""

    pages: List[Dict[str, Any]]
    """The json result of the parsing job"""
