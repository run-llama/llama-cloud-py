# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .sparse_model_config_param import SparseModelConfigParam
from .auto_transform_config_param import AutoTransformConfigParam
from .llama_parse_parameters_param import LlamaParseParametersParam
from .pipeline_metadata_config_param import PipelineMetadataConfigParam
from .advanced_mode_transform_config_param import AdvancedModeTransformConfigParam

__all__ = [
    "PipelineUpdateParams",
    "DataSink",
    "DataSinkComponent",
    "DataSinkComponentCloudPineconeVectorStore",
    "DataSinkComponentCloudPostgresVectorStore",
    "DataSinkComponentCloudPostgresVectorStoreHnswSettings",
    "DataSinkComponentCloudQdrantVectorStore",
    "DataSinkComponentCloudAzureAISearchVectorStore",
    "DataSinkComponentCloudMongoDBAtlasVectorSearch",
    "DataSinkComponentCloudMilvusVectorStore",
    "DataSinkComponentCloudAstraDBVectorStore",
    "EmbeddingConfig",
    "EmbeddingConfigAzureOpenAIEmbeddingConfig",
    "EmbeddingConfigAzureOpenAIEmbeddingConfigComponent",
    "EmbeddingConfigCohereEmbeddingConfig",
    "EmbeddingConfigCohereEmbeddingConfigComponent",
    "EmbeddingConfigGeminiEmbeddingConfig",
    "EmbeddingConfigGeminiEmbeddingConfigComponent",
    "EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfig",
    "EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfigComponent",
    "EmbeddingConfigOpenAIEmbeddingConfig",
    "EmbeddingConfigOpenAIEmbeddingConfigComponent",
    "EmbeddingConfigVertexAIEmbeddingConfig",
    "EmbeddingConfigVertexAIEmbeddingConfigComponent",
    "EmbeddingConfigBedrockEmbeddingConfig",
    "EmbeddingConfigBedrockEmbeddingConfigComponent",
    "TransformConfig",
]


class PipelineUpdateParams(TypedDict, total=False):
    data_sink: Optional[DataSink]
    """Schema for creating a data sink."""

    data_sink_id: Optional[str]
    """Data sink ID.

    When provided instead of data_sink, the data sink will be looked up by ID.
    """

    embedding_config: Optional[EmbeddingConfig]

    embedding_model_config_id: Optional[str]
    """Embedding model config ID.

    When provided instead of embedding_config, the embedding model config will be
    looked up by ID.
    """

    llama_parse_parameters: Optional[LlamaParseParametersParam]
    """
    Settings that can be configured for how to use LlamaParse to parse files within
    a LlamaCloud pipeline.
    """

    managed_pipeline_id: Optional[str]
    """The ID of the ManagedPipeline this playground pipeline is linked to."""

    metadata_config: Optional[PipelineMetadataConfigParam]
    """Metadata configuration for the pipeline."""

    name: Optional[str]

    preset_retrieval_parameters: Optional["PresetRetrievalParamsParam"]
    """
    Schema for the search params for an retrieval execution that can be preset for a
    pipeline.
    """

    sparse_model_config: Optional[SparseModelConfigParam]
    """Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for sparse retrieval
    in managed data sinks.
    """

    status: Optional[str]
    """Status of the pipeline deployment."""

    transform_config: Optional[TransformConfig]
    """Configuration for the transformation."""


class DataSinkComponentCloudPineconeVectorStore(TypedDict, total=False):
    """Cloud Pinecone Vector Store.

    This class is used to store the configuration for a Pinecone vector store, so that it can be
    created and used in LlamaCloud.

    Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion
    """

    api_key: Required[str]
    """The API key for authenticating with Pinecone"""

    index_name: Required[str]

    class_name: str

    insert_kwargs: Optional[Dict[str, object]]

    namespace: Optional[str]

    supports_nested_metadata_filters: Literal[True]


class DataSinkComponentCloudPostgresVectorStoreHnswSettings(TypedDict, total=False):
    """HNSW settings for PGVector."""

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


class DataSinkComponentCloudPostgresVectorStore(TypedDict, total=False):
    database: Required[str]

    embed_dim: Required[int]

    host: Required[str]

    password: Required[str]

    port: Required[int]

    schema_name: Required[str]

    table_name: Required[str]

    user: Required[str]

    class_name: str

    hnsw_settings: Optional[DataSinkComponentCloudPostgresVectorStoreHnswSettings]
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool]

    perform_setup: bool

    supports_nested_metadata_filters: bool


class DataSinkComponentCloudQdrantVectorStore(TypedDict, total=False):
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


class DataSinkComponentCloudAzureAISearchVectorStore(TypedDict, total=False):
    """Cloud Azure AI Search Vector Store."""

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


class DataSinkComponentCloudMongoDBAtlasVectorSearch(TypedDict, total=False):
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

    collection_name: Required[str]

    db_name: Required[str]

    mongodb_uri: Required[str]

    class_name: str

    embedding_dimension: Optional[int]

    fulltext_index_name: Optional[str]

    supports_nested_metadata_filters: bool

    vector_index_name: Optional[str]


class DataSinkComponentCloudMilvusVectorStore(TypedDict, total=False):
    """Cloud Milvus Vector Store."""

    uri: Required[str]

    token: Optional[str]

    class_name: str

    collection_name: Optional[str]

    embedding_dimension: Optional[int]

    supports_nested_metadata_filters: bool


class DataSinkComponentCloudAstraDBVectorStore(TypedDict, total=False):
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


DataSinkComponent: TypeAlias = Union[
    Dict[str, object],
    DataSinkComponentCloudPineconeVectorStore,
    DataSinkComponentCloudPostgresVectorStore,
    DataSinkComponentCloudQdrantVectorStore,
    DataSinkComponentCloudAzureAISearchVectorStore,
    DataSinkComponentCloudMongoDBAtlasVectorSearch,
    DataSinkComponentCloudMilvusVectorStore,
    DataSinkComponentCloudAstraDBVectorStore,
]


class DataSink(TypedDict, total=False):
    """Schema for creating a data sink."""

    component: Required[DataSinkComponent]
    """Component that implements the data sink"""

    name: Required[str]
    """The name of the data sink."""

    sink_type: Required[
        Literal["PINECONE", "POSTGRES", "QDRANT", "AZUREAI_SEARCH", "MONGODB_ATLAS", "MILVUS", "ASTRA_DB"]
    ]


class EmbeddingConfigAzureOpenAIEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the Azure OpenAI embedding model."""

    additional_kwargs: Dict[str, object]
    """Additional kwargs for the OpenAI API."""

    api_base: str
    """The base URL for Azure deployment."""

    api_key: Optional[str]
    """The OpenAI API key."""

    api_version: str
    """The version for Azure OpenAI API."""

    azure_deployment: Optional[str]
    """The Azure deployment to use."""

    azure_endpoint: Optional[str]
    """The Azure endpoint to use."""

    class_name: str

    default_headers: Optional[Dict[str, str]]
    """The default headers for API requests."""

    dimensions: Optional[int]
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: int
    """The batch size for embedding calls."""

    max_retries: int
    """Maximum number of retries."""

    model_name: str
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    reuse_client: bool
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: float
    """Timeout for each request."""


class EmbeddingConfigAzureOpenAIEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigAzureOpenAIEmbeddingConfigComponent
    """Configuration for the Azure OpenAI embedding model."""

    type: Literal["AZURE_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigCohereEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the Cohere embedding model."""

    api_key: Required[Optional[str]]
    """The Cohere API key."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    embedding_type: str
    """Embedding type. If not provided float embedding_type is used when needed."""

    input_type: Optional[str]
    """Model Input type.

    If not provided, search_document and search_query are used when needed.
    """

    model_name: str
    """The modelId of the Cohere model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    truncate: str
    """Truncation type - START/ END/ NONE"""


class EmbeddingConfigCohereEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigCohereEmbeddingConfigComponent
    """Configuration for the Cohere embedding model."""

    type: Literal["COHERE_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigGeminiEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the Gemini embedding model."""

    api_base: Optional[str]
    """API base to access the model. Defaults to None."""

    api_key: Optional[str]
    """API key to access the model. Defaults to None."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    model_name: str
    """The modelId of the Gemini model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    task_type: Optional[str]
    """The task for embedding model."""

    title: Optional[str]
    """
    Title is only applicable for retrieval_document tasks, and is used to represent
    a document title. For other tasks, title is invalid.
    """

    transport: Optional[str]
    """Transport to access the model. Defaults to None."""


class EmbeddingConfigGeminiEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigGeminiEmbeddingConfigComponent
    """Configuration for the Gemini embedding model."""

    type: Literal["GEMINI_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the HuggingFace Inference API embedding model."""

    token: Union[str, bool, None]
    """Hugging Face token.

    Will default to the locally saved token. Pass token=False if you don’t want to
    send your token to the server.
    """

    class_name: str

    cookies: Optional[Dict[str, str]]
    """Additional cookies to send to the server."""

    embed_batch_size: int
    """The batch size for embedding calls."""

    headers: Optional[Dict[str, str]]
    """Additional headers to send to the server.

    By default only the authorization and user-agent headers are sent. Values in
    this dictionary will override the default values.
    """

    model_name: Optional[str]
    """Hugging Face model name. If None, the task will be used."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    pooling: Optional[Literal["cls", "mean", "last"]]
    """Enum of possible pooling choices with pooling behaviors."""

    query_instruction: Optional[str]
    """Instruction to prepend during query embedding."""

    task: Optional[str]
    """
    Optional task to pick Hugging Face's recommended model, used when model_name is
    left as default of None.
    """

    text_instruction: Optional[str]
    """Instruction to prepend during text embedding."""

    timeout: Optional[float]
    """The maximum number of seconds to wait for a response from the server.

    Loading a new model in Inference API can take up to several minutes. Defaults to
    None, meaning it will loop until the server is available.
    """


class EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfigComponent
    """Configuration for the HuggingFace Inference API embedding model."""

    type: Literal["HUGGINGFACE_API_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigOpenAIEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the OpenAI embedding model."""

    additional_kwargs: Dict[str, object]
    """Additional kwargs for the OpenAI API."""

    api_base: Optional[str]
    """The base URL for OpenAI API."""

    api_key: Optional[str]
    """The OpenAI API key."""

    api_version: Optional[str]
    """The version for OpenAI API."""

    class_name: str

    default_headers: Optional[Dict[str, str]]
    """The default headers for API requests."""

    dimensions: Optional[int]
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: int
    """The batch size for embedding calls."""

    max_retries: int
    """Maximum number of retries."""

    model_name: str
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    reuse_client: bool
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: float
    """Timeout for each request."""


class EmbeddingConfigOpenAIEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigOpenAIEmbeddingConfigComponent
    """Configuration for the OpenAI embedding model."""

    type: Literal["OPENAI_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigVertexAIEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the VertexAI embedding model."""

    client_email: Required[Optional[str]]
    """The client email for the VertexAI credentials."""

    location: Required[str]
    """The default location to use when making API calls."""

    private_key: Required[Optional[str]]
    """The private key for the VertexAI credentials."""

    private_key_id: Required[Optional[str]]
    """The private key ID for the VertexAI credentials."""

    project: Required[str]
    """The default GCP project to use when making Vertex API calls."""

    token_uri: Required[Optional[str]]
    """The token URI for the VertexAI credentials."""

    additional_kwargs: Dict[str, object]
    """Additional kwargs for the Vertex."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    embed_mode: Literal["default", "classification", "clustering", "similarity", "retrieval"]
    """The embedding mode to use."""

    model_name: str
    """The modelId of the VertexAI model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""


class EmbeddingConfigVertexAIEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigVertexAIEmbeddingConfigComponent
    """Configuration for the VertexAI embedding model."""

    type: Literal["VERTEXAI_EMBEDDING"]
    """Type of the embedding model."""


class EmbeddingConfigBedrockEmbeddingConfigComponent(TypedDict, total=False):
    """Configuration for the Bedrock embedding model."""

    additional_kwargs: Dict[str, object]
    """Additional kwargs for the bedrock client."""

    aws_access_key_id: Optional[str]
    """AWS Access Key ID to use"""

    aws_secret_access_key: Optional[str]
    """AWS Secret Access Key to use"""

    aws_session_token: Optional[str]
    """AWS Session Token to use"""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    max_retries: int
    """The maximum number of API retries."""

    model_name: str
    """The modelId of the Bedrock model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    profile_name: Optional[str]
    """The name of aws profile to use. If not given, then the default profile is used."""

    region_name: Optional[str]
    """AWS region name to use. Uses region configured in AWS CLI if not passed"""

    timeout: float
    """The timeout for the Bedrock API request in seconds.

    It will be used for both connect and read timeouts.
    """


class EmbeddingConfigBedrockEmbeddingConfig(TypedDict, total=False):
    component: EmbeddingConfigBedrockEmbeddingConfigComponent
    """Configuration for the Bedrock embedding model."""

    type: Literal["BEDROCK_EMBEDDING"]
    """Type of the embedding model."""


EmbeddingConfig: TypeAlias = Union[
    EmbeddingConfigAzureOpenAIEmbeddingConfig,
    EmbeddingConfigCohereEmbeddingConfig,
    EmbeddingConfigGeminiEmbeddingConfig,
    EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfig,
    EmbeddingConfigOpenAIEmbeddingConfig,
    EmbeddingConfigVertexAIEmbeddingConfig,
    EmbeddingConfigBedrockEmbeddingConfig,
]

TransformConfig: TypeAlias = Union[AutoTransformConfigParam, AdvancedModeTransformConfigParam]

from .preset_retrieval_params_param import PresetRetrievalParamsParam
