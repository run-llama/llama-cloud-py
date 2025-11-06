# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileUploadFromURLParams"]


class FileUploadFromURLParams(TypedDict, total=False):
    url: Required[str]
    """URL of the file to download"""

    organization_id: Optional[str]

    project_id: Optional[str]

    follow_redirects: bool
    """Whether to follow redirects when downloading the file"""

    name: Optional[str]
    """Name that will be used for created file.

    If possible, always include the file extension in the name.
    """

    proxy_url: Optional[str]
    """URL of the proxy server to use for downloading the file"""

    request_headers: Optional[Dict[str, str]]
    """Headers to include in the request when downloading the file"""

    resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Resource information for the file"""

    verify_ssl: bool
    """Whether to verify the SSL certificate when downloading the file"""
