# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SheetsParsingConfig"]


class SheetsParsingConfig(BaseModel):
    extraction_range: Optional[str] = None
    """A1 notation of the range to extract a single region from.

    If None, the entire sheet is used.
    """

    generate_additional_metadata: Optional[bool] = None
    """
    Whether to generate additional metadata (title, description) for each extracted
    region.
    """

    include_hidden_cells: Optional[bool] = None
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[List[str]] = None
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    use_experimental_processing: Optional[bool] = None
    """Enables experimental processing. Accuracy may be impacted."""
