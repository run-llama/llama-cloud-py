# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from ..._types import SequenceNotStr
from ..._compat import PYDANTIC_V1

__all__ = ["MetadataFiltersParam", "Filter", "FilterMetadataFilter"]


class FilterMetadataFilter(TypedDict, total=False):
    key: Required[str]

    value: Required[Union[float, str, SequenceNotStr[str], Iterable[float], Iterable[int], None]]

    operator: Literal[
        "==",
        ">",
        "<",
        "!=",
        ">=",
        "<=",
        "in",
        "nin",
        "any",
        "all",
        "text_match",
        "text_match_insensitive",
        "contains",
        "is_empty",
    ]
    """Vector store filter operator."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Filter = TypeAliasType("Filter", Union[FilterMetadataFilter, "MetadataFiltersParam"])
else:
    Filter: TypeAlias = Union[FilterMetadataFilter, "MetadataFiltersParam"]


class MetadataFiltersParam(TypedDict, total=False):
    filters: Required[Iterable[Filter]]

    condition: Optional[Literal["and", "or", "not"]]
    """Vector store filter conditions to combine different filters."""
