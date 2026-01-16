# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ParseConfigurationListParams"]


class ParseConfigurationListParams(TypedDict, total=False):
    creator: Optional[str]

    name: Optional[str]

    organization_id: Optional[str]

    page_size: Optional[int]

    page_token: Optional[str]

    project_id: Optional[str]

    version: Optional[str]
