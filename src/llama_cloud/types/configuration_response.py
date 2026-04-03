# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .untyped_parameters import UntypedParameters
from .parse_v2_parameters import ParseV2Parameters
from .split_v1_parameters import SplitV1Parameters
from .extract_v2_parameters import ExtractV2Parameters
from .classify_v2_parameters import ClassifyV2Parameters

__all__ = ["ConfigurationResponse", "Parameters"]

Parameters: TypeAlias = Annotated[
    Union[SplitV1Parameters, ExtractV2Parameters, ClassifyV2Parameters, ParseV2Parameters, UntypedParameters],
    PropertyInfo(discriminator="product_type"),
]


class ConfigurationResponse(BaseModel):
    """Response schema for a single product configuration."""

    id: str
    """Unique configuration ID."""

    name: str
    """Configuration name."""

    parameters: Parameters
    """Product-specific configuration parameters."""

    product_type: Literal["split_v1", "extract_v2", "classify_v2", "parse_v2", "unknown"]
    """Product type."""

    version: str
    """Version identifier (datetime string)."""

    created_at: Optional[datetime] = None
    """Creation timestamp."""

    updated_at: Optional[datetime] = None
    """Last update timestamp."""
