# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudAstraDBVectorStore"]


class CloudAstraDBVectorStore(TypedDict, total=False):
    """Cloud AstraDB Vector Store.

    This class is used to store the configuration for an AstraDB vector store, so that it can be
    created and used in LlamaCloud.

    Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'
    """

    token: Required[str]
    """The Astra DB Application Token to use"""

    api_endpoint: Required[str]
    """The Astra DB JSON API endpoint for your database"""

    collection_name: Required[str]
    """Collection name to use. If not existing, it will be created"""

    embedding_dimension: Required[int]
    """Length of the embedding vectors in use"""

    class_name: str

    keyspace: Optional[str]
    """The keyspace to use. If not provided, 'default_keyspace'"""

    supports_nested_metadata_filters: Literal[True]
