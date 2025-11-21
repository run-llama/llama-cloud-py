# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .sheets_parsing_config_param import SheetsParsingConfigParam

__all__ = ["SheetCreateParams"]


class SheetCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    organization_id: Optional[str]

    project_id: Optional[str]

    config: SheetsParsingConfigParam
    """Configuration for the parsing job"""
