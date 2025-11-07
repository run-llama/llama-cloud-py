# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "EmbeddingModelConfigUpsertParams",
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
]


class EmbeddingModelConfigUpsertParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    embedding_config: Optional[EmbeddingConfig]
    """The embedding configuration for the embedding model config."""

    name: Optional[str]
    """The name of the embedding model config."""


class EmbeddingConfigAzureOpenAIEmbeddingConfigComponent(TypedDict, total=False):
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
