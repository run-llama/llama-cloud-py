# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudMilvusVectorStore"]


class CloudMilvusVectorStore(BaseModel):
    """Cloud Milvus Vector Store."""

    uri: str

    class_name: Optional[str] = None

    collection_name: Optional[str] = None

    embedding_dimension: Optional[int] = None

    supports_nested_metadata_filters: Optional[bool] = None
