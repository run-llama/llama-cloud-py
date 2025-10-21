# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SchemaGenerateParams"]


class SchemaGenerateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    file_id: Optional[str]
    """Optional file ID to analyze for schema generation"""

    prompt: Optional[str]
    """Natural language description of the data structure to extract"""
