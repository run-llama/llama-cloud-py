# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SheetsParsingConfigParam"]


class SheetsParsingConfigParam(TypedDict, total=False):
    """Configuration for spreadsheet parsing and region extraction"""

    extraction_range: Optional[str]
    """A1 notation of the range to extract a single region from.

    If None, the entire sheet is used.
    """

    flatten_hierarchical_tables: bool
    """
    Return a flattened dataframe when a detected table is recognized as
    hierarchical.
    """

    generate_additional_metadata: bool
    """
    Whether to generate additional metadata (title, description) for each extracted
    region.
    """

    include_hidden_cells: bool
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[SequenceNotStr[str]]
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    table_merge_sensitivity: Literal["strong", "weak"]
    """Influences how likely similar-looking regions are merged into a single table.

    Useful for spreadsheets that either have sparse tables (strong merging) or many
    distinct tables close together (weak merging).
    """

    use_experimental_processing: bool
    """Enables experimental processing. Accuracy may be impacted."""
