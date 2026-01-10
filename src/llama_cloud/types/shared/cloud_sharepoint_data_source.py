# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudSharepointDataSource"]


class CloudSharepointDataSource(BaseModel):
    client_id: str
    """The client ID to use for authentication."""

    tenant_id: str
    """The tenant ID to use for authentication."""

    class_name: Optional[str] = None

    drive_name: Optional[str] = None
    """The name of the Sharepoint drive to read from."""

    exclude_path_patterns: Optional[List[str]] = None
    """List of regex patterns for file paths to exclude.

    Files whose paths (including filename) match any pattern will be excluded.
    Example: ['/temp/', '/backup/', '\\..git/', '\\..tmp$', '^~']
    """

    folder_id: Optional[str] = None
    """The ID of the Sharepoint folder to read from."""

    folder_path: Optional[str] = None
    """The path of the Sharepoint folder to read from."""

    get_permissions: Optional[bool] = None
    """Whether to get permissions for the sharepoint site."""

    include_path_patterns: Optional[List[str]] = None
    """List of regex patterns for file paths to include.

    Full paths (including filename) must match at least one pattern to be included.
    Example: ['/reports/', '/docs/.*\\..pdf$', '^Report.*\\..pdf$']
    """

    required_exts: Optional[List[str]] = None
    """The list of required file extensions."""

    site_id: Optional[str] = None
    """The ID of the SharePoint site to download from."""

    site_name: Optional[str] = None
    """The name of the SharePoint site to download from."""

    supports_access_control: Optional[Literal[True]] = None
