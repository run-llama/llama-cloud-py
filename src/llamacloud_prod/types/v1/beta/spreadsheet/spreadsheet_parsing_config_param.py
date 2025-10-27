# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ....._types import SequenceNotStr

__all__ = ["SpreadsheetParsingConfigParam"]


class SpreadsheetParsingConfigParam(TypedDict, total=False):
    extraction_range: Optional[str]
    """A1 notation of the range to extract a single table from.

    If None, the entire sheet is used.
    """

    include_hidden_cells: bool
    """Whether to include hidden cells when extracting tables from the spreadsheet."""

    sheet_names: Optional[SequenceNotStr[str]]
    """The names of the sheets to extract tables from.

    If empty, the default sheet is extracted.
    """
