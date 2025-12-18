# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ParsingGetParams"]


class ParsingGetParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """List of fields to include in response.

    Supported values: text, markdown, items. Example: ?expand=text&expand=markdown
    """

    organization_id: Optional[str]

    project_id: Optional[str]
