# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .configurable_data_sink_names import ConfigurableDataSinkNames
from .cloud_milvus_vector_store_param import CloudMilvusVectorStoreParam
from .cloud_qdrant_vector_store_param import CloudQdrantVectorStoreParam
from .cloud_astra_db_vector_store_param import CloudAstraDBVectorStoreParam
from .cloud_pinecone_vector_store_param import CloudPineconeVectorStoreParam
from .cloud_postgres_vector_store_param import CloudPostgresVectorStoreParam
from .cloud_mongodb_atlas_vector_search_param import CloudMongoDBAtlasVectorSearchParam
from .cloud_azure_ai_search_vector_store_param import CloudAzureAISearchVectorStoreParam

__all__ = ["DataSinkUpdateParams", "Component"]


class DataSinkUpdateParams(TypedDict, total=False):
    sink_type: Required[ConfigurableDataSinkNames]

    component: Optional[Component]
    """Component that implements the data sink"""

    name: Optional[str]
    """The name of the data sink."""


Component: TypeAlias = Union[
    Dict[str, object],
    CloudPineconeVectorStoreParam,
    CloudPostgresVectorStoreParam,
    CloudQdrantVectorStoreParam,
    CloudAzureAISearchVectorStoreParam,
    CloudMongoDBAtlasVectorSearchParam,
    CloudMilvusVectorStoreParam,
    CloudAstraDBVectorStoreParam,
]
