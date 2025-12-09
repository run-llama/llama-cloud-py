# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AgentDataAggregateParams", "Filter"]


class AgentDataAggregateParams(TypedDict, total=False):
    deployment_name: Required[str]
    """The agent deployment's name to aggregate data for"""

    organization_id: Optional[str]

    project_id: Optional[str]

    collection: str
    """The logical agent data collection to aggregate data for"""

    count: Optional[bool]
    """Whether to count the number of items in each group"""

    filter: Optional[Dict[str, Filter]]
    """A filter object or expression that filters resources listed in the response."""

    first: Optional[bool]
    """Whether to return the first item in each group (Sorted by created_at)"""

    group_by: Optional[SequenceNotStr[str]]
    """The fields to group by.

    If empty, the entire dataset is grouped on. e.g. if left out, can be used for
    simple count operations
    """

    offset: Optional[int]
    """The offset to start from. If not provided, the first page is returned"""

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
    """API request model for a filter comparison operation."""

    eq: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    gt: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    gte: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    includes: Annotated[SequenceNotStr[Union[float, str, Union[str, datetime], None]], PropertyInfo(format="iso8601")]

    lt: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]
