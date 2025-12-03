# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["SchemaGenerateSchemaParams"]


class SchemaGenerateSchemaParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None]
    """Optional schema to validate, refine, or extend during generation"""

    file_id: Optional[str]
    """Optional file ID to analyze for schema generation"""

    prompt: Optional[str]
    """Natural language description of the data structure to extract"""
