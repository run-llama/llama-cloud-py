# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SplitCategoryParam"]


class SplitCategoryParam(TypedDict, total=False):
    """Category definition for document splitting."""

    name: Required[str]
    """Name of the category."""

    description: Optional[str]
    """Optional description of what content belongs in this category."""
