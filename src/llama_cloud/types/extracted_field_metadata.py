# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["ExtractedFieldMetadata"]


class ExtractedFieldMetadata(BaseModel):
    """Metadata for extracted fields including document, page, and row level info."""

    document_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Per-field metadata keyed by field name from your schema.

    Scalar fields (e.g. `vendor`) map to a FieldMetadataEntry with citation and
    confidence. Array fields (e.g. `items`) map to a list where each element
    contains per-sub-field FieldMetadataEntry objects, indexed by array position.
    Nested objects contain sub-field entries recursively.
    """

    page_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]]] = None
    """Per-page metadata when extraction_target is per_page"""

    row_metadata: Optional[List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]]] = None
    """Per-row metadata when extraction_target is per_table_row"""
