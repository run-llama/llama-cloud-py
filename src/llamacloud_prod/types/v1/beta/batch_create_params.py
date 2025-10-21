# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..llama_parse_parameters_param import LlamaParseParametersParam

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """A developer-provided ID for the batch.

    This ID will be returned in the response.
    """

    input_id: Required[str]
    """The ID of the input file for the batch."""

    input_type: Required[str]
    """The type of input file. Currently only 'datasource' is supported."""

    body_project_id: Required[Annotated[str, PropertyInfo(alias="project_id")]]
    """The ID of the project to which the batch belongs"""

    tool: Required[str]
    """The tool to be used for all requests in the batch."""

    organization_id: Optional[str]

    query_project_id: Annotated[Optional[str], PropertyInfo(alias="project_id")]

    completion_window: int
    """The time frame within which the batch should be processed.

    Currently only 24h is supported.
    """

    output_id: Optional[str]
    """The ID of the output file for the batch."""

    output_type: Optional[str]
    """The type of output file. Currently only 'datasource' is supported."""

    tool_data: Optional[LlamaParseParametersParam]
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """
