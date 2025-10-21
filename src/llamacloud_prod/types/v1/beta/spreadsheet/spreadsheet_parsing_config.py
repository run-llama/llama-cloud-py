# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["SpreadsheetParsingConfig"]


class SpreadsheetParsingConfig(BaseModel):
    sheet_names: Optional[List[str]] = None
    """The names of the sheets to parse. If empty, all sheets will be parsed."""
