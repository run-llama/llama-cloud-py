# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SplitGetResponse", "Category", "DocumentInput", "Result", "ResultSegment"]


class Category(BaseModel):
    """Category definition for document splitting."""

    name: str
    """Name of the category."""

    description: Optional[str] = None
    """Optional description of what content belongs in this category."""


class DocumentInput(BaseModel):
    """Document that was split."""

    type: str
    """Type of document input. Valid values are: file_id"""

    value: str
    """Document identifier."""


class ResultSegment(BaseModel):
    """A segment of the split document."""

    category: str
    """Category name this split belongs to."""

    confidence_category: str
    """Categorical confidence level. Valid values are: high, medium, low."""

    pages: List[int]
    """1-indexed page numbers in this split."""


class Result(BaseModel):
    """Result of a completed split job."""

    segments: List[ResultSegment]
    """List of document segments."""


class SplitGetResponse(BaseModel):
    """A document split job."""

    id: str
    """Unique identifier for the split job."""

    categories: List[Category]
    """Categories used for splitting."""

    document_input: DocumentInput
    """Document that was split."""

    project_id: str
    """Project ID this job belongs to."""

    status: str
    """Current status of the job.

    Valid values are: pending, processing, completed, failed.
    """

    user_id: str
    """User ID who created this job."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if the job failed."""

    result: Optional[Result] = None
    """Result of a completed split job."""

    updated_at: Optional[datetime] = None
    """Update datetime"""
