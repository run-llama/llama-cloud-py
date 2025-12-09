# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentData"]


class AgentData(BaseModel):
    """API Result for a single agent data item"""

    data: Dict[str, object]

    deployment_name: str

    id: Optional[str] = None

    collection: Optional[str] = None

    created_at: Optional[datetime] = None

    project_id: Optional[str] = None

    updated_at: Optional[datetime] = None
