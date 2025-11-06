# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name that will be used for created file.

    If possible, always include the file extension in the name.
    """

    organization_id: Optional[str]

    project_id: Optional[str]

    data_source_id: Optional[str]
    """The ID of the data source that the file belongs to"""

    external_file_id: Optional[str]
    """The ID of the file in the external system"""

    file_size: Optional[int]
    """Size of the file in bytes"""

    last_modified_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The last modified time of the file"""

    permission_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Permission information for the file"""

    resource_info: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Resource information for the file"""
