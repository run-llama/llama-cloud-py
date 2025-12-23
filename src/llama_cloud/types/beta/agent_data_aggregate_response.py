# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["AgentDataAggregateResponse", "Item"]


class Item(BaseModel):
    """API Result for a single group in the aggregate response"""

    group_key: Dict[str, object]

    count: Optional[int] = None

    first_item: Optional[Dict[str, object]] = None


class AgentDataAggregateResponse(BaseModel):
    items: List[Item]
    """The list of items."""

    next_page_token: Optional[str] = None
    """A token, which can be sent as page_token to retrieve the next page.

    If this field is omitted, there are no subsequent pages.
    """

    total_size: Optional[int] = None
    """The total number of items available.

    This is only populated when specifically requested. The value may be an estimate
    and can be used for display purposes only.
    """
