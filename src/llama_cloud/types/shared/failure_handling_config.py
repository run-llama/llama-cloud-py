# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FailureHandlingConfig"]


class FailureHandlingConfig(BaseModel):
    """
    Configuration for handling different types of failures during data source processing.
    """

    skip_list_failures: Optional[bool] = None
    """Whether to skip failed batches/lists and continue processing"""
