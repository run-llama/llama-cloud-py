# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectGetUsageParams"]


class ProjectGetUsageParams(TypedDict, total=False):
    get_current_invoice_total: bool

    organization_id: Optional[str]
