# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["AgentDataAggregateResponse"]


class AgentDataAggregateResponse(BaseModel):
    """API Result for a single group in the aggregate response"""

    group_key: Dict[str, object]

    count: Optional[int] = None

    first_item: Optional[Dict[str, object]] = None
