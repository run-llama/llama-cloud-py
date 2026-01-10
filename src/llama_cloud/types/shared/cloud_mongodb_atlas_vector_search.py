# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudMongoDBAtlasVectorSearch"]


class CloudMongoDBAtlasVectorSearch(BaseModel):
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

    collection_name: str

    db_name: str

    class_name: Optional[str] = None

    embedding_dimension: Optional[int] = None

    fulltext_index_name: Optional[str] = None

    supports_nested_metadata_filters: Optional[bool] = None

    vector_index_name: Optional[str] = None
