# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .api_key_type import APIKeyType

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    key_type: APIKeyType

    project_id: Optional[str]
