# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BillingCreateIntentAndCustomerSessionResponse"]


class BillingCreateIntentAndCustomerSessionResponse(BaseModel):
    client_secret: str

    customer_session_client_secret: Optional[str] = None
