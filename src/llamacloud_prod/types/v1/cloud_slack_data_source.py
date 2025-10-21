# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudSlackDataSource"]


class CloudSlackDataSource(BaseModel):
    channel_ids: Optional[str] = None
    """Slack Channel."""

    channel_patterns: Optional[str] = None
    """Slack Channel name pattern."""

    class_name: Optional[str] = None

    earliest_date: Optional[str] = None
    """Earliest date."""

    earliest_date_timestamp: Optional[float] = None
    """Earliest date timestamp."""

    latest_date: Optional[str] = None
    """Latest date."""

    latest_date_timestamp: Optional[float] = None
    """Latest date timestamp."""

    supports_access_control: Optional[bool] = None
