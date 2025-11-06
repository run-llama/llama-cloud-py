# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..llama_parse_parameters_param import LlamaParseParametersParam

__all__ = ["ParseConfigurationUpdateParams"]


class ParseConfigurationUpdateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    parameters: Optional[LlamaParseParametersParam]
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """
