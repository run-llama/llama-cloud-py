# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .untyped_parameters import UntypedParameters
from .parse_v2_parameters import ParseV2Parameters
from .split_v1_parameters import SplitV1Parameters
from .extract_v2_parameters import ExtractV2Parameters
from .classify_v2_parameters import ClassifyV2Parameters

__all__ = ["ConfigurationCreate", "Parameters"]

Parameters: TypeAlias = Annotated[
    Union[SplitV1Parameters, ExtractV2Parameters, ClassifyV2Parameters, ParseV2Parameters, UntypedParameters],
    PropertyInfo(discriminator="product_type"),
]


class ConfigurationCreate(BaseModel):
    """Request body for creating a product configuration."""

    name: str
    """Human-readable name for this configuration."""

    parameters: Parameters
    """Product-specific configuration parameters."""
