# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudNotionPageDataSource"]


class CloudNotionPageDataSource(TypedDict, total=False):
    integration_token: Required[str]
    """The integration token to use for authentication."""

    class_name: str

    database_ids: Optional[str]
    """The Notion Database Id to read content from."""

    page_ids: Optional[str]
    """The Page ID's of the Notion to read from."""

    supports_access_control: bool
