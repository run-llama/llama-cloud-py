# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BaseConnectionValidation"]


class BaseConnectionValidation(BaseModel):
    message: str

    success: bool
