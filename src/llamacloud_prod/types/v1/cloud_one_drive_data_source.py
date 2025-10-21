# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudOneDriveDataSource"]


class CloudOneDriveDataSource(BaseModel):
    client_id: str
    """The client ID to use for authentication."""

    tenant_id: str
    """The tenant ID to use for authentication."""

    user_principal_name: str
    """The user principal name to use for authentication."""

    class_name: Optional[str] = None

    folder_id: Optional[str] = None
    """The ID of the OneDrive folder to read from."""

    folder_path: Optional[str] = None
    """The path of the OneDrive folder to read from."""

    required_exts: Optional[List[str]] = None
    """The list of required file extensions."""

    supports_access_control: Optional[Literal[True]] = None
