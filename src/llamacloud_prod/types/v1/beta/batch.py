# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ..llama_parse_parameters import LlamaParseParameters

__all__ = ["Batch"]


class Batch(BaseModel):
    id: str
    """Unique identifier for the batch"""

    completion_window: int
    """The time frame within which the batch should be processed"""

    input_id: str
    """The ID of the input file for the batch."""

    input_type: str
    """The type of input file. Currently only 'datasource' is supported."""

    organization_id: str
    """The ID of the organization to which the batch belongs"""

    pipeline_id: str
    """The ID of the pipeline to which the batch belongs"""

    project_id: str
    """The ID of the project to which the batch belongs"""

    status: str
    """The current status of the batch"""

    tool: str
    """The tool to be used for all requests in the batch."""

    user_id: str
    """The ID of the user who created the batch"""

    created_at: Optional[datetime] = None
    """The Unix timestamp (in seconds) for when the batch was created"""

    external_id: Optional[str] = None
    """A developer-provided ID for the batch.

    This ID will be returned in the response.
    """

    output_id: Optional[str] = None
    """The ID of the output file for the batch."""

    output_type: Optional[str] = None
    """The type of output file. Currently only 'datasource' is supported."""

    tool_data: Optional[LlamaParseParameters] = None
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """

    updated_at: Optional[datetime] = None
    """The Unix timestamp (in seconds) for when the batch was last updated"""
