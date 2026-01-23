# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload"""

    purpose: Required[str]
    """The intended purpose of the file.

    Valid values: 'user_data', 'parse', 'extract', 'split', 'classify', 'sheet',
    'agent_app'
    """

    organization_id: Optional[str]

    project_id: Optional[str]

    external_file_id: Optional[str]
    """The ID of the file in the external system"""
