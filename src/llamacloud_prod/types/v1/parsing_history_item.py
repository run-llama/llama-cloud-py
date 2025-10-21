# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ParsingHistoryItem"]


class ParsingHistoryItem(BaseModel):
    day: str

    file_name: str

    job_id: str

    original_file_name: str

    user_id: str

    expired: Optional[bool] = None

    images: Optional[float] = None

    pages: Optional[float] = None

    time: Optional[float] = None
