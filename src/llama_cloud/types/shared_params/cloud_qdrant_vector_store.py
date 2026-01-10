# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudQdrantVectorStore"]


class CloudQdrantVectorStore(TypedDict, total=False):
    """Cloud Qdrant Vector Store.

    This class is used to store the configuration for a Qdrant vector store, so that it can be
    created and used in LlamaCloud.

    Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client
    """

    api_key: Required[str]

    collection_name: Required[str]

    url: Required[str]

    class_name: str

    client_kwargs: Dict[str, object]

    max_retries: int

    supports_nested_metadata_filters: Literal[True]
