# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudMongoDBAtlasVectorSearch"]


class CloudMongoDBAtlasVectorSearch(TypedDict, total=False):
    """Cloud MongoDB Atlas Vector Store.

    This class is used to store the configuration for a MongoDB Atlas vector store,
    so that it can be created and used in LlamaCloud.

    Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index
    """

    collection_name: Required[str]

    db_name: Required[str]

    mongodb_uri: Required[str]

    class_name: str

    embedding_dimension: Optional[int]

    fulltext_index_name: Optional[str]

    supports_nested_metadata_filters: bool

    vector_index_name: Optional[str]
