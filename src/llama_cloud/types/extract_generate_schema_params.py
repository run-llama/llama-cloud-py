# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["ExtractGenerateSchemaParams"]


class ExtractGenerateSchemaParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    data_schema: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Optional schema to validate, refine, or extend"""

    file_id: Optional[str]
    """Optional file ID to analyze for schema generation"""

    name: Optional[str]
    """Name for the generated configuration (auto-generated if omitted)"""

    prompt: Optional[str]
    """Natural language description of the data structure to extract"""
