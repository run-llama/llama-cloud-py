# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["SpreadsheetParsingConfig"]


class SpreadsheetParsingConfig(BaseModel):
    extraction_range: Optional[str] = None
    """A1 notation of the range to extract a single table from.

    If None, the entire sheet is used.
    """

    include_hidden_cells: Optional[bool] = None
    """Whether to include hidden cells when extracting tables from the spreadsheet."""

    sheet_names: Optional[List[str]] = None
    """The names of the sheets to extract tables from.

    If empty, the default sheet is extracted.
    """
