# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ParseConfigurationQueryParams", "Filter"]


class ParseConfigurationQueryParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    filter: Optional[Filter]
    """Filter parameters for parse configuration queries."""

    order_by: Optional[str]
    """A comma-separated list of fields to order by, sorted in ascending order.

    Use 'field_name desc' to specify descending order.
    """

    page_size: Optional[int]
    """The maximum number of items to return.

    The service may return fewer than this value. If unspecified, a default page
    size will be used. The maximum value is typically 1000; values above this will
    be coerced to the maximum.
    """

    page_token: Optional[str]
    """A page token, received from a previous list call.

    Provide this to retrieve the subsequent page.
    """


class Filter(TypedDict, total=False):
    creator: Optional[str]
    """Filter by creator"""

    name: Optional[str]
    """Filter by name"""

    parse_config_ids: Optional[SequenceNotStr[str]]
    """Filter by specific parse configuration IDs"""

    source_id: Optional[str]
    """Filter by source ID"""

    source_type: Optional[str]
    """Filter by source type"""

    version: Optional[str]
    """Filter by version"""
