# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudAstraDBVectorStore"]


class CloudAstraDBVectorStore(BaseModel):
    api_endpoint: str
    """The Astra DB JSON API endpoint for your database"""

    collection_name: str
    """Collection name to use. If not existing, it will be created"""

    embedding_dimension: int
    """Length of the embedding vectors in use"""

    class_name: Optional[str] = None

    keyspace: Optional[str] = None
    """The keyspace to use. If not provided, 'default_keyspace'"""

    supports_nested_metadata_filters: Optional[Literal[True]] = None
