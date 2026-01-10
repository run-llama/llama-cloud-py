# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudPineconeVectorStore"]


class CloudPineconeVectorStore(TypedDict, total=False):
    """Cloud Pinecone Vector Store.

    This class is used to store the configuration for a Pinecone vector store, so that it can be
    created and used in LlamaCloud.

    Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion
    """

    api_key: Required[str]
    """The API key for authenticating with Pinecone"""

    index_name: Required[str]

    class_name: str

    insert_kwargs: Optional[Dict[str, object]]

    namespace: Optional[str]

    supports_nested_metadata_filters: Literal[True]
