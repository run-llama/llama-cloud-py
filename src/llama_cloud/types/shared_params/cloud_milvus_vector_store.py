# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudMilvusVectorStore"]


class CloudMilvusVectorStore(TypedDict, total=False):
    """Cloud Milvus Vector Store."""

    uri: Required[str]

    token: Optional[str]

    class_name: str

    collection_name: Optional[str]

    embedding_dimension: Optional[int]

    supports_nested_metadata_filters: bool
