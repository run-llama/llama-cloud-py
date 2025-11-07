# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .spreadsheet_parsing_config_param import SpreadsheetParsingConfigParam

__all__ = ["SpreadsheetCreateParams"]


class SpreadsheetCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    organization_id: Optional[str]

    project_id: Optional[str]

    config: SpreadsheetParsingConfigParam
    """Configuration for the parsing job"""
