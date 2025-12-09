# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .parse_configuration import ParseConfiguration

__all__ = ["ParseConfigurationQueryResponse"]


class ParseConfigurationQueryResponse(BaseModel):
    """Response schema for paginated parse configuration queries."""

    items: List[ParseConfiguration]
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
