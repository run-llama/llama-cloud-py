# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AgentDataDeleteByQueryResponse"]


class AgentDataDeleteByQueryResponse(BaseModel):
    """API response for bulk delete operation"""

    deleted_count: int
