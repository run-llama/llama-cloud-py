# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .split_category_param import SplitCategoryParam
from .split_document_input_param import SplitDocumentInputParam

__all__ = ["SplitCreateParams", "SplittingStrategy"]


class SplitCreateParams(TypedDict, total=False):
    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split documents into."""

    document_input: Required[SplitDocumentInputParam]
    """Document to be split."""

    organization_id: Optional[str]

    project_id: Optional[str]

    splitting_strategy: SplittingStrategy
    """Strategy for splitting documents."""


class SplittingStrategy(TypedDict, total=False):
    """Strategy for splitting documents."""

    allow_uncategorized: Literal["include", "forbid", "omit"]
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """
