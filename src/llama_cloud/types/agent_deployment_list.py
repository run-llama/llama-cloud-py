# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentDeploymentList", "Deployment"]


class Deployment(BaseModel):
    id: str
    """Deployment ID. Prefixed with dpl-"""

    base_url: str
    """Base URL of the deployed app"""

    created_at: datetime
    """Timestamp when the app deployment was created"""

    deployment_name: str
    """Identifier of the deployed app"""

    project_id: str
    """Project ID"""

    updated_at: datetime
    """Timestamp when the app deployment was last updated"""

    api_key_id: Optional[str] = None
    """API key ID"""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL of the deployed app"""


class AgentDeploymentList(BaseModel):
    deployments: List[Deployment]
    """List of deployments"""
