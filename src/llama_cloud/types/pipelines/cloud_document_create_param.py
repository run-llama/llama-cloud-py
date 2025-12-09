# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CloudDocumentCreateParam"]


class CloudDocumentCreateParam(TypedDict, total=False):
    """Create a new cloud document."""

    metadata: Required[Dict[str, object]]

    text: Required[str]

    id: Optional[str]

    excluded_embed_metadata_keys: SequenceNotStr[str]

    excluded_llm_metadata_keys: SequenceNotStr[str]

    page_positions: Optional[Iterable[int]]
    """indices in the CloudDocument.text where a new page begins.

    e.g. Second page starts at index specified by page_positions[1].
    """
