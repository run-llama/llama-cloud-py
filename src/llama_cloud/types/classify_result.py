# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ClassifyResult"]


class ClassifyResult(BaseModel):
    """Result of classifying a document."""

    confidence: float
    """Confidence score between 0.0 and 1.0"""

    reasoning: str
    """Why the document matched (or didn't match) the returned rule"""

    type: Optional[str] = None
    """Matched rule type, or null if no rule matched"""
