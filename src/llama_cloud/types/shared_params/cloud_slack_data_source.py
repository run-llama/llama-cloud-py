# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudSlackDataSource"]


class CloudSlackDataSource(TypedDict, total=False):
    slack_token: Required[str]
    """Slack Bot Token."""

    channel_ids: Optional[str]
    """Slack Channel."""

    channel_patterns: Optional[str]
    """Slack Channel name pattern."""

    class_name: str

    earliest_date: Optional[str]
    """Earliest date."""

    earliest_date_timestamp: Optional[float]
    """Earliest date timestamp."""

    latest_date: Optional[str]
    """Latest date."""

    latest_date_timestamp: Optional[float]
    """Latest date timestamp."""

    supports_access_control: bool
