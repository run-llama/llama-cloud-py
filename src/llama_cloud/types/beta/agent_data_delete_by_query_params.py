# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AgentDataDeleteByQueryParams", "Filter"]


class AgentDataDeleteByQueryParams(TypedDict, total=False):
    deployment_name: Required[str]
    """The agent deployment's name to delete data for"""

    organization_id: Optional[str]

    project_id: Optional[str]

    collection: str
    """The logical agent data collection to delete from"""

    filter: Optional[Dict[str, Filter]]
    """Optional filters to select which items to delete"""


class Filter(TypedDict, total=False):
    """API request model for a filter comparison operation."""

    eq: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    gt: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    gte: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    includes: Annotated[SequenceNotStr[Union[float, str, Union[str, datetime], None]], PropertyInfo(format="iso8601")]

    lt: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[float, str, Union[str, datetime], None], PropertyInfo(format="iso8601")]
