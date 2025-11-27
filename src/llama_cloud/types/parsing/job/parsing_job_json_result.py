# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from typing import Any, List, Dict

__all__ = ["ParsingJobJsonResult"]


class ParsingJobJsonResult(BaseModel):
    job_metadata: object
    """Parsing job metadata , including usage"""

    pages: List[Dict[str, Any]]
    """The json result of the parsing job"""
