# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SplitCreateParams", "Category", "DocumentInput", "SplittingStrategy"]


class SplitCreateParams(TypedDict, total=False):
    categories: Required[Iterable[Category]]
    """Categories to split the document into."""

    document_input: Required[DocumentInput]
    """Document to be split."""

    organization_id: Optional[str]

    project_id: Optional[str]

    splitting_strategy: SplittingStrategy
    """Strategy for splitting the document."""


class Category(TypedDict, total=False):
    """Category definition for document splitting."""

    name: Required[str]
    """Name of the category."""

    description: Optional[str]
    """Optional description of what content belongs in this category."""


class DocumentInput(TypedDict, total=False):
    """Document to be split."""

    type: Required[str]
    """Type of document input. Valid values are: file_id"""

    value: Required[str]
    """Document identifier."""


class SplittingStrategy(TypedDict, total=False):
    """Strategy for splitting the document."""

    allow_uncategorized: bool
    """
    Whether to allow pages that don't match any category to be grouped as
    'uncategorized'. If False, all pages must be assigned to a defined category.
    """
