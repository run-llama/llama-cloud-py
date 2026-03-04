# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ClassifyResult"]


class ClassifyResult(BaseModel):
    """Result of classifying a document."""

    confidence: float
    """Confidence score (0.0-1.0)"""

    reasoning: str
    """Explanation of classification decision"""

    type: Optional[str] = None
    """Document type that matches, or None"""
