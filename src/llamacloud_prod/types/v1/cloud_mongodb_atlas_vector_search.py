# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudMongoDBAtlasVectorSearch"]


class CloudMongoDBAtlasVectorSearch(BaseModel):
    collection_name: str

    db_name: str

    class_name: Optional[str] = None

    embedding_dimension: Optional[int] = None

    fulltext_index_name: Optional[str] = None

    supports_nested_metadata_filters: Optional[bool] = None

    vector_index_name: Optional[str] = None
