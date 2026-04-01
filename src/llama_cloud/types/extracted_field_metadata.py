# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["ExtractedFieldMetadata"]


class ExtractedFieldMetadata(BaseModel):
    """Metadata for extracted fields including document, page, and row level info."""

    document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Document-level metadata (citations, confidence) keyed by field name"""

    page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]]] = None
    """Per-page metadata when extraction_target is per_page"""

    row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]]] = None
    """Per-row metadata when extraction_target is per_table_row"""
