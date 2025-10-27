# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ..status_enum import StatusEnum
from .classifier_rule import ClassifierRule
from .classify_parsing_configuration import ClassifyParsingConfiguration

__all__ = ["ClassifyJob"]


class ClassifyJob(BaseModel):
    id: str
    """Unique identifier"""

    project_id: str
    """The ID of the project"""

    rules: List[ClassifierRule]
    """The rules to classify the files"""

    status: StatusEnum
    """The status of the classify job"""

    user_id: str
    """The ID of the user"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    effective_at: Optional[datetime] = None

    error_message: Optional[str] = None
    """Error message for the latest job attempt, if any."""

    job_record_id: Optional[str] = None
    """The job record ID associated with this status, if any."""

    parsing_configuration: Optional[ClassifyParsingConfiguration] = None
    """The configuration for the parsing job"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
