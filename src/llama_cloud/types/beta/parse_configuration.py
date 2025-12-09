# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..llama_parse_parameters import LlamaParseParameters

__all__ = ["ParseConfiguration"]


class ParseConfiguration(BaseModel):
    """Parse configuration schema."""

    id: str
    """Unique identifier for the parse configuration"""

    created_at: datetime
    """Creation timestamp"""

    name: str
    """Name of the parse configuration"""

    parameters: LlamaParseParameters
    """LlamaParseParameters configuration"""

    source_id: str
    """ID of the source"""

    source_type: str
    """Type of the source (e.g., 'project')"""

    updated_at: datetime
    """Last update timestamp"""

    version: str
    """Version of the configuration"""

    creator: Optional[str] = None
    """Creator of the configuration"""
