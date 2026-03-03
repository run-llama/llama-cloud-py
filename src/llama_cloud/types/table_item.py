# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = ["TableItem", "ParseConcern"]


class ParseConcern(BaseModel):
    details: str
    """Human-readable details about the concern"""

    type: str
    """Type of parse concern (e.g.

    header_value_type_mismatch, inconsistent_row_cell_count)
    """


class TableItem(BaseModel):
    csv: str
    """CSV representation of the table"""

    html: str
    """HTML representation of the table"""

    md: str
    """Markdown representation preserving formatting"""

    rows: List[List[Union[str, float, None]]]
    """Table data as array of arrays (string, number, or null)"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    merged_from_pages: Optional[List[int]] = None
    """
    List of page numbers with tables that were merged into this table (e.g., [1, 2,
    3, 4])
    """

    merged_into_page: Optional[int] = None
    """Populated when merged into another table.

    Page number where the full merged table begins (used on empty tables).
    """

    parse_concerns: Optional[List[ParseConcern]] = None
    """
    Quality concerns detected during table extraction, indicating the table may have
    issues
    """

    type: Optional[Literal["table"]] = None
    """Table item type"""
