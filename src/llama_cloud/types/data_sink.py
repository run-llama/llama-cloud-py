# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "DataSink",
    "Component",
    "ComponentCloudPineconeVectorStore",
    "ComponentCloudPostgresVectorStore",
    "ComponentCloudPostgresVectorStoreHnswSettings",
    "ComponentCloudQdrantVectorStore",
    "ComponentCloudAzureAISearchVectorStore",
    "ComponentCloudMongoDBAtlasVectorSearch",
    "ComponentCloudMilvusVectorStore",
    "ComponentCloudAstraDBVectorStore",
]


class ComponentCloudPineconeVectorStore(BaseModel):
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


class ComponentCloudPostgresVectorStoreHnswSettings(BaseModel):
    """HNSW settings for PGVector."""

    distance_method: Optional[Literal["l2", "ip", "cosine", "l1", "hamming", "jaccard"]] = None
    """The distance method to use."""

    ef_construction: Optional[int] = None
    """The number of edges to use during the construction phase."""

    ef_search: Optional[int] = None
    """The number of edges to use during the search phase."""

    m: Optional[int] = None
    """The number of bi-directional links created for each new element."""

    vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]] = None
    """The type of vector to use."""


class ComponentCloudPostgresVectorStore(BaseModel):
    database: str

    embed_dim: int

    host: str

    port: int

    schema_name: str

    table_name: str

    user: str

    class_name: Optional[str] = None

    hnsw_settings: Optional[ComponentCloudPostgresVectorStoreHnswSettings] = None
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool] = None

    perform_setup: Optional[bool] = None

    supports_nested_metadata_filters: Optional[bool] = None


class ComponentCloudQdrantVectorStore(BaseModel):
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


class ComponentCloudAzureAISearchVectorStore(BaseModel):
    """Cloud Azure AI Search Vector Store."""

    search_service_endpoint: str

    class_name: Optional[str] = None

    client_id: Optional[str] = None

    embedding_dimension: Optional[int] = None

    filterable_metadata_field_keys: Optional[Dict[str, object]] = None

    index_name: Optional[str] = None

    search_service_api_version: Optional[str] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None

    tenant_id: Optional[str] = None


class ComponentCloudMongoDBAtlasVectorSearch(BaseModel):
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


class ComponentCloudMilvusVectorStore(BaseModel):
    """Cloud Milvus Vector Store."""

    uri: str

    class_name: Optional[str] = None

    collection_name: Optional[str] = None

    embedding_dimension: Optional[int] = None

    supports_nested_metadata_filters: Optional[bool] = None


class ComponentCloudAstraDBVectorStore(BaseModel):
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


Component: TypeAlias = Union[
    Dict[str, object],
    ComponentCloudPineconeVectorStore,
    ComponentCloudPostgresVectorStore,
    ComponentCloudQdrantVectorStore,
    ComponentCloudAzureAISearchVectorStore,
    ComponentCloudMongoDBAtlasVectorSearch,
    ComponentCloudMilvusVectorStore,
    ComponentCloudAstraDBVectorStore,
]


class DataSink(BaseModel):
    """Schema for a data sink."""

    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data sink"""

    name: str
    """The name of the data sink."""

    project_id: str

    sink_type: Literal["PINECONE", "POSTGRES", "QDRANT", "AZUREAI_SEARCH", "MONGODB_ATLAS", "MILVUS", "ASTRA_DB"]

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
