# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CloudOneDriveDataSource"]


class CloudOneDriveDataSource(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to use for authentication."""

    client_secret: Required[str]
    """The client secret to use for authentication."""

    tenant_id: Required[str]
    """The tenant ID to use for authentication."""

    user_principal_name: Required[str]
    """The user principal name to use for authentication."""

    class_name: str

    folder_id: Optional[str]
    """The ID of the OneDrive folder to read from."""

    folder_path: Optional[str]
    """The path of the OneDrive folder to read from."""

    required_exts: Optional[SequenceNotStr[str]]
    """The list of required file extensions."""

    supports_access_control: Literal[True]
