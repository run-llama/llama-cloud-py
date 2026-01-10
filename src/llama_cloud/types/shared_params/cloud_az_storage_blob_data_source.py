# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudAzStorageBlobDataSource"]


class CloudAzStorageBlobDataSource(TypedDict, total=False):
    account_url: Required[str]
    """The Azure Storage Blob account URL to use for authentication."""

    container_name: Required[str]
    """The name of the Azure Storage Blob container to read from."""

    account_key: Optional[str]
    """The Azure Storage Blob account key to use for authentication."""

    account_name: Optional[str]
    """The Azure Storage Blob account name to use for authentication."""

    blob: Optional[str]
    """The blob name to read from."""

    class_name: str

    client_id: Optional[str]
    """The Azure AD client ID to use for authentication."""

    client_secret: Optional[str]
    """The Azure AD client secret to use for authentication."""

    prefix: Optional[str]
    """The prefix of the Azure Storage Blob objects to read from."""

    supports_access_control: bool

    tenant_id: Optional[str]
    """The Azure AD tenant ID to use for authentication."""
