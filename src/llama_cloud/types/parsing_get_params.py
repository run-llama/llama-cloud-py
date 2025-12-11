# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ParsingGetParams"]


class ParsingGetParams(TypedDict, total=False):
    include_json_output: bool
    """Include JSON output result in response"""

    include_markdown: bool
    """Include markdown result in response"""

    include_structured: bool
    """Include structured JSON result in response"""

    include_text: bool
    """Include plain text result in response"""

    organization_id: Optional[str]

    project_id: Optional[str]
