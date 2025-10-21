# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .status_enum import StatusEnum

__all__ = ["ParsingJob"]


class ParsingJob(BaseModel):
    id: str

    status: StatusEnum
    """Enum for representing the status of a job"""

    error_code: Optional[str] = None

    error_message: Optional[str] = None
