# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudQdrantVectorStore"]


class CloudQdrantVectorStore(BaseModel):
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

    collection_name: str

    url: str

    class_name: Optional[str] = None

    client_kwargs: Optional[Dict[str, object]] = None

    max_retries: Optional[int] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None
