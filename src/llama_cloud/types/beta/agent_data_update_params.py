# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentDataUpdateParams"]


class AgentDataUpdateParams(TypedDict, total=False):
    data: Required[Dict[str, object]]

    organization_id: Optional[str]

    project_id: Optional[str]
