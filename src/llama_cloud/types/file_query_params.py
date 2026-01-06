# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FileQueryParams", "Filter"]


class FileQueryParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    filter: Optional[Filter]
    """Filter parameters for file queries."""

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
    """Filter parameters for file queries."""

    data_source_id: Optional[str]
    """Filter by data source ID"""

    external_file_id: Optional[str]
    """Filter by external file ID"""

    file_ids: Optional[SequenceNotStr[str]]
    """Filter by specific file IDs"""

    file_name: Optional[str]
    """Filter by file name"""

    only_manually_uploaded: Optional[bool]
    """Filter only manually uploaded files (data_source_id is null)"""

    project_id: Optional[str]
    """Filter by project ID"""
