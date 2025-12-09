# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["CloudDocument"]


class CloudDocument(BaseModel):
    """Cloud document stored in S3."""

    id: str

    metadata: Dict[str, object]

    text: str

    excluded_embed_metadata_keys: Optional[List[str]] = None

    excluded_llm_metadata_keys: Optional[List[str]] = None

    page_positions: Optional[List[int]] = None
    """indices in the CloudDocument.text where a new page begins.

    e.g. Second page starts at index specified by page_positions[1].
    """

    status_metadata: Optional[Dict[str, object]] = None
