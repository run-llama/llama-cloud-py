# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudPineconeVectorStore"]


class CloudPineconeVectorStore(BaseModel):
    """Cloud Pinecone Vector Store.

    This class is used to store the configuration for a Pinecone vector store, so that it can be
    created and used in LlamaCloud.

    Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion
    """

    index_name: str

    class_name: Optional[str] = None

    insert_kwargs: Optional[Dict[str, object]] = None

    namespace: Optional[str] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None
