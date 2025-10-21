# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..api_key_type import APIKeyType

__all__ = ["APIKeyAPIKeysParams"]


class APIKeyAPIKeysParams(TypedDict, total=False):
    key_type: APIKeyType

    name: Optional[str]

    project_id: Optional[str]
    """The project ID to associate with the API key."""
