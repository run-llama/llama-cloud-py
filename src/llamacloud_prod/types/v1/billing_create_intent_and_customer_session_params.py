# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingCreateIntentAndCustomerSessionParams"]


class BillingCreateIntentAndCustomerSessionParams(TypedDict, total=False):
    plan_name: Required[
        Literal[
            "free",
            "llama_parse",
            "enterprise",
            "unknown",
            "free_contract",
            "pro",
            "enterprise_contract",
            "enterprise_poc",
            "free_v1",
            "starter_v1",
            "pro_v1",
        ]
    ]

    organization_id: Optional[str]
