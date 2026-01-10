# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .split_category_param import SplitCategoryParam
from .split_document_input_param import SplitDocumentInputParam

__all__ = ["SplitCreateParams", "SplittingStrategy"]


class SplitCreateParams(TypedDict, total=False):
    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split the document into."""

    document_input: Required[SplitDocumentInputParam]
    """Document to be split."""

    organization_id: Optional[str]

    project_id: Optional[str]

    splitting_strategy: SplittingStrategy
    """Strategy for splitting the document."""


class SplittingStrategy(TypedDict, total=False):
    """Strategy for splitting the document."""

    allow_uncategorized: bool
    """
    Whether to allow pages that don't match any category to be grouped as
    'uncategorized'. If False, all pages must be assigned to a defined category.
    """
