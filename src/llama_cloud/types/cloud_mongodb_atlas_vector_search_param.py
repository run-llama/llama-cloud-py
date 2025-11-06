# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudMongoDBAtlasVectorSearchParam"]


class CloudMongoDBAtlasVectorSearchParam(TypedDict, total=False):
    collection_name: Required[str]

    db_name: Required[str]

    mongodb_uri: Required[str]

    class_name: str

    embedding_dimension: Optional[int]

    fulltext_index_name: Optional[str]

    supports_nested_metadata_filters: bool

    vector_index_name: Optional[str]
