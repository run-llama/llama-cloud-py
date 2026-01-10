# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FailureHandlingConfig"]


class FailureHandlingConfig(TypedDict, total=False):
    """
    Configuration for handling different types of failures during data source processing.
    """

    skip_list_failures: bool
    """Whether to skip failed batches/lists and continue processing"""
