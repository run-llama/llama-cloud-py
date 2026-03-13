# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .extract_options import ExtractOptions
from .beta.split_category import SplitCategory

__all__ = [
    "ExtractGenerateSchemaResponse",
    "Parameters",
    "ParametersSplitV1Parameters",
    "ParametersSplitV1ParametersSplittingStrategy",
    "ParametersExtractV2Parameters",
    "ParametersClassifyV2Parameters",
    "ParametersClassifyV2ParametersRule",
    "ParametersParseV2Parameters",
]


class ParametersSplitV1ParametersSplittingStrategy(BaseModel):
    """Strategy for splitting documents."""

    allow_uncategorized: Optional[Literal["include", "forbid", "omit"]] = None
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """


class ParametersSplitV1Parameters(BaseModel):
    """Typed parameters for a *split v1* product configuration."""

    categories: List[SplitCategory]
    """Categories to split documents into."""

    product_type: Literal["split_v1"]
    """Product type."""

    splitting_strategy: Optional[ParametersSplitV1ParametersSplittingStrategy] = None
    """Strategy for splitting documents."""


class ParametersExtractV2Parameters(BaseModel):
    """Typed parameters for an *extract v2* product configuration."""

    extract_options: ExtractOptions
    """Extract-specific configuration options including the data schema"""

    product_type: Literal["extract_v2"]
    """Product type."""

    parse_config_id: Optional[str] = None
    """Parse config ID used for extraction"""

    parse_tier: Optional[str] = None
    """Parse tier to use for extraction (e.g. fast, cost_effective, agentic)."""


class ParametersClassifyV2ParametersRule(BaseModel):
    """A rule for classifying documents."""

    description: str
    """Natural language description of what to classify"""

    type: str
    """Document type to assign when rule matches"""


class ParametersClassifyV2Parameters(BaseModel):
    """Typed parameters for a *classify v2* product configuration."""

    product_type: Literal["classify_v2"]
    """Product type."""

    rules: List[ParametersClassifyV2ParametersRule]
    """Classification rules to apply (at least one required)"""

    mode: Optional[Literal["FAST"]] = None
    """Classification execution mode"""


class ParametersParseV2Parameters(BaseModel):
    """Typed parameters for a *parse v2* product configuration.

    Parse configs have a flexible parameter set (tier, version, plus
    various parsing options), so extra fields are permitted.
    """

    product_type: Literal["parse_v2"]
    """Product type."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Parameters: TypeAlias = Annotated[
    Union[
        ParametersSplitV1Parameters,
        ParametersExtractV2Parameters,
        ParametersClassifyV2Parameters,
        ParametersParseV2Parameters,
    ],
    PropertyInfo(discriminator="product_type"),
]


class ExtractGenerateSchemaResponse(BaseModel):
    """Request body for creating a product configuration."""

    name: str
    """Human-readable name for this configuration."""

    parameters: Parameters
    """Product-specific configuration parameters."""
