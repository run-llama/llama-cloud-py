# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .untyped_parameters_param import UntypedParametersParam
from .parse_v2_parameters_param import ParseV2ParametersParam
from .split_v1_parameters_param import SplitV1ParametersParam
from .extract_v2_parameters_param import ExtractV2ParametersParam
from .classify_v2_parameters_param import ClassifyV2ParametersParam

__all__ = ["ConfigurationUpdateParams", "Parameters"]


class ConfigurationUpdateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    name: Optional[str]
    """Updated name (omit to leave unchanged)."""

    parameters: Optional[Parameters]
    """Updated parameters (omit to leave unchanged)."""


Parameters: TypeAlias = Union[
    SplitV1ParametersParam,
    ExtractV2ParametersParam,
    ClassifyV2ParametersParam,
    ParseV2ParametersParam,
    UntypedParametersParam,
]
