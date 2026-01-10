# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudAzStorageBlobDataSource"]


class CloudAzStorageBlobDataSource(BaseModel):
    account_url: str
    """The Azure Storage Blob account URL to use for authentication."""

    container_name: str
    """The name of the Azure Storage Blob container to read from."""

    account_name: Optional[str] = None
    """The Azure Storage Blob account name to use for authentication."""

    blob: Optional[str] = None
    """The blob name to read from."""

    class_name: Optional[str] = None

    client_id: Optional[str] = None
    """The Azure AD client ID to use for authentication."""

    prefix: Optional[str] = None
    """The prefix of the Azure Storage Blob objects to read from."""

    supports_access_control: Optional[bool] = None

    tenant_id: Optional[str] = None
    """The Azure AD tenant ID to use for authentication."""
