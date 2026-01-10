# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SplitDocumentInputParam"]


class SplitDocumentInputParam(TypedDict, total=False):
    """Document input specification."""

    type: Required[str]
    """Type of document input. Valid values are: file_id"""

    value: Required[str]
    """Document identifier."""
