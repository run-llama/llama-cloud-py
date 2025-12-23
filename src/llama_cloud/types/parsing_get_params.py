# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ParsingGetParams"]


class ParsingGetParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """List of fields to include in response.

    Supported values: text, markdown, items, text_content_metadata,
    markdown_content_metadata, items_content_metadata. Example:
    ?expand=text&expand=markdown&expand=text_content_metadata
    """

    organization_id: Optional[str]

    project_id: Optional[str]
