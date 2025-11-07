# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "DataSinkUpdateParams",
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


class DataSinkUpdateParams(TypedDict, total=False):
    sink_type: Required[
        Literal["PINECONE", "POSTGRES", "QDRANT", "AZUREAI_SEARCH", "MONGODB_ATLAS", "MILVUS", "ASTRA_DB"]
    ]

    component: Optional[Component]
    """Component that implements the data sink"""

    name: Optional[str]
    """The name of the data sink."""


class ComponentCloudPineconeVectorStore(TypedDict, total=False):
    api_key: Required[str]
    """The API key for authenticating with Pinecone"""

    index_name: Required[str]

    class_name: str

    insert_kwargs: Optional[Dict[str, object]]

    namespace: Optional[str]

    supports_nested_metadata_filters: Literal[True]


class ComponentCloudPostgresVectorStoreHnswSettings(TypedDict, total=False):
    distance_method: Literal["l2", "ip", "cosine", "l1", "hamming", "jaccard"]
    """The distance method to use."""

    ef_construction: int
    """The number of edges to use during the construction phase."""

    ef_search: int
    """The number of edges to use during the search phase."""

    m: int
    """The number of bi-directional links created for each new element."""

    vector_type: Literal["vector", "half_vec", "bit", "sparse_vec"]
    """The type of vector to use."""


class ComponentCloudPostgresVectorStore(TypedDict, total=False):
    database: Required[str]

    embed_dim: Required[int]

    host: Required[str]

    password: Required[str]

    port: Required[int]

    schema_name: Required[str]

    table_name: Required[str]

    user: Required[str]

    class_name: str

    hnsw_settings: Optional[ComponentCloudPostgresVectorStoreHnswSettings]
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool]

    perform_setup: bool

    supports_nested_metadata_filters: bool


class ComponentCloudQdrantVectorStore(TypedDict, total=False):
    api_key: Required[str]

    collection_name: Required[str]

    url: Required[str]

    class_name: str

    client_kwargs: Dict[str, object]

    max_retries: int

    supports_nested_metadata_filters: Literal[True]


class ComponentCloudAzureAISearchVectorStore(TypedDict, total=False):
    search_service_api_key: Required[str]

    search_service_endpoint: Required[str]

    class_name: str

    client_id: Optional[str]

    client_secret: Optional[str]

    embedding_dimension: Optional[int]

    filterable_metadata_field_keys: Optional[Dict[str, object]]

    index_name: Optional[str]

    search_service_api_version: Optional[str]

    supports_nested_metadata_filters: Literal[True]

    tenant_id: Optional[str]


class ComponentCloudMongoDBAtlasVectorSearch(TypedDict, total=False):
    collection_name: Required[str]

    db_name: Required[str]

    mongodb_uri: Required[str]

    class_name: str

    embedding_dimension: Optional[int]

    fulltext_index_name: Optional[str]

    supports_nested_metadata_filters: bool

    vector_index_name: Optional[str]


class ComponentCloudMilvusVectorStore(TypedDict, total=False):
    uri: Required[str]

    token: Optional[str]

    class_name: str

    collection_name: Optional[str]

    embedding_dimension: Optional[int]

    supports_nested_metadata_filters: bool


class ComponentCloudAstraDBVectorStore(TypedDict, total=False):
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
