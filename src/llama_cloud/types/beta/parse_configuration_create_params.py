# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..llama_parse_parameters_param import LlamaParseParametersParam

__all__ = ["ParseConfigurationCreateParams"]


class ParseConfigurationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the parse configuration"""

    parameters: Required[LlamaParseParametersParam]
    """LlamaParseParameters configuration"""

    version: Required[str]
    """Version of the configuration"""

    organization_id: Optional[str]

    project_id: Optional[str]

    creator: Optional[str]
    """Creator of the configuration"""

    source_id: Optional[str]
    """ID of the source"""

    source_type: Optional[str]
    """Type of the source (e.g., 'project')"""
