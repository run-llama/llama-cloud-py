# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ....._types import SequenceNotStr

__all__ = ["SpreadsheetParsingConfigParam"]


class SpreadsheetParsingConfigParam(TypedDict, total=False):
    sheet_names: Optional[SequenceNotStr[str]]
    """The names of the sheets to parse. If empty, all sheets will be parsed."""
