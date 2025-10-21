# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CloudSharepointDataSourceParam"]


class CloudSharepointDataSourceParam(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to use for authentication."""

    client_secret: Required[str]
    """The client secret to use for authentication."""

    tenant_id: Required[str]
    """The tenant ID to use for authentication."""

    class_name: str

    drive_name: Optional[str]
    """The name of the Sharepoint drive to read from."""

    folder_id: Optional[str]
    """The ID of the Sharepoint folder to read from."""

    folder_path: Optional[str]
    """The path of the Sharepoint folder to read from."""

    get_permissions: Optional[bool]
    """Whether to get permissions for the sharepoint site."""

    required_exts: Optional[SequenceNotStr[str]]
    """The list of required file extensions."""

    site_id: Optional[str]
    """The ID of the SharePoint site to download from."""

    site_name: Optional[str]
    """The name of the SharePoint site to download from."""

    supports_access_control: Literal[True]
