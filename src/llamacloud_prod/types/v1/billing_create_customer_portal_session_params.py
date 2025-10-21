# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BillingCreateCustomerPortalSessionParams"]


class BillingCreateCustomerPortalSessionParams(TypedDict, total=False):
    return_url: Required[str]

    organization_id: Optional[str]
