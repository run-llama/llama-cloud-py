# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "EmbeddingModelConfig",
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


class EmbeddingConfigAzureOpenAIEmbeddingConfigComponent(BaseModel):
    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the OpenAI API."""

    api_base: Optional[str] = None
    """The base URL for Azure deployment."""

    api_key: Optional[str] = None
    """The OpenAI API key."""

    api_version: Optional[str] = None
    """The version for Azure OpenAI API."""

    azure_deployment: Optional[str] = None
    """The Azure deployment to use."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint to use."""

    class_name: Optional[str] = None

    default_headers: Optional[Dict[str, str]] = None
    """The default headers for API requests."""

    dimensions: Optional[int] = None
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    max_retries: Optional[int] = None
    """Maximum number of retries."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    reuse_client: Optional[bool] = None
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: Optional[float] = None
    """Timeout for each request."""


class EmbeddingConfigAzureOpenAIEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigAzureOpenAIEmbeddingConfigComponent] = None
    """Configuration for the Azure OpenAI embedding model."""

    type: Optional[Literal["AZURE_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigCohereEmbeddingConfigComponent(BaseModel):
    api_key: Optional[str] = None
    """The Cohere API key."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    embedding_type: Optional[str] = None
    """Embedding type. If not provided float embedding_type is used when needed."""

    input_type: Optional[str] = None
    """Model Input type.

    If not provided, search_document and search_query are used when needed.
    """

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Cohere model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    truncate: Optional[str] = None
    """Truncation type - START/ END/ NONE"""


class EmbeddingConfigCohereEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigCohereEmbeddingConfigComponent] = None
    """Configuration for the Cohere embedding model."""

    type: Optional[Literal["COHERE_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigGeminiEmbeddingConfigComponent(BaseModel):
    api_base: Optional[str] = None
    """API base to access the model. Defaults to None."""

    api_key: Optional[str] = None
    """API key to access the model. Defaults to None."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Gemini model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    task_type: Optional[str] = None
    """The task for embedding model."""

    title: Optional[str] = None
    """
    Title is only applicable for retrieval_document tasks, and is used to represent
    a document title. For other tasks, title is invalid.
    """

    transport: Optional[str] = None
    """Transport to access the model. Defaults to None."""


class EmbeddingConfigGeminiEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigGeminiEmbeddingConfigComponent] = None
    """Configuration for the Gemini embedding model."""

    type: Optional[Literal["GEMINI_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfigComponent(BaseModel):
    token: Union[str, bool, None] = None
    """Hugging Face token.

    Will default to the locally saved token. Pass token=False if you don’t want to
    send your token to the server.
    """

    class_name: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None
    """Additional cookies to send to the server."""

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    headers: Optional[Dict[str, str]] = None
    """Additional headers to send to the server.

    By default only the authorization and user-agent headers are sent. Values in
    this dictionary will override the default values.
    """

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Hugging Face model name. If None, the task will be used."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    pooling: Optional[Literal["cls", "mean", "last"]] = None
    """Enum of possible pooling choices with pooling behaviors."""

    query_instruction: Optional[str] = None
    """Instruction to prepend during query embedding."""

    task: Optional[str] = None
    """
    Optional task to pick Hugging Face's recommended model, used when model_name is
    left as default of None.
    """

    text_instruction: Optional[str] = None
    """Instruction to prepend during text embedding."""

    timeout: Optional[float] = None
    """The maximum number of seconds to wait for a response from the server.

    Loading a new model in Inference API can take up to several minutes. Defaults to
    None, meaning it will loop until the server is available.
    """


class EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfigComponent] = None
    """Configuration for the HuggingFace Inference API embedding model."""

    type: Optional[Literal["HUGGINGFACE_API_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigOpenAIEmbeddingConfigComponent(BaseModel):
    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the OpenAI API."""

    api_base: Optional[str] = None
    """The base URL for OpenAI API."""

    api_key: Optional[str] = None
    """The OpenAI API key."""

    api_version: Optional[str] = None
    """The version for OpenAI API."""

    class_name: Optional[str] = None

    default_headers: Optional[Dict[str, str]] = None
    """The default headers for API requests."""

    dimensions: Optional[int] = None
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    max_retries: Optional[int] = None
    """Maximum number of retries."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    reuse_client: Optional[bool] = None
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: Optional[float] = None
    """Timeout for each request."""


class EmbeddingConfigOpenAIEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigOpenAIEmbeddingConfigComponent] = None
    """Configuration for the OpenAI embedding model."""

    type: Optional[Literal["OPENAI_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigVertexAIEmbeddingConfigComponent(BaseModel):
    client_email: Optional[str] = None
    """The client email for the VertexAI credentials."""

    location: str
    """The default location to use when making API calls."""

    private_key: Optional[str] = None
    """The private key for the VertexAI credentials."""

    private_key_id: Optional[str] = None
    """The private key ID for the VertexAI credentials."""

    project: str
    """The default GCP project to use when making Vertex API calls."""

    token_uri: Optional[str] = None
    """The token URI for the VertexAI credentials."""

    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the Vertex."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    embed_mode: Optional[Literal["default", "classification", "clustering", "similarity", "retrieval"]] = None
    """The embedding mode to use."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the VertexAI model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""


class EmbeddingConfigVertexAIEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigVertexAIEmbeddingConfigComponent] = None
    """Configuration for the VertexAI embedding model."""

    type: Optional[Literal["VERTEXAI_EMBEDDING"]] = None
    """Type of the embedding model."""


class EmbeddingConfigBedrockEmbeddingConfigComponent(BaseModel):
    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the bedrock client."""

    aws_access_key_id: Optional[str] = None
    """AWS Access Key ID to use"""

    aws_secret_access_key: Optional[str] = None
    """AWS Secret Access Key to use"""

    aws_session_token: Optional[str] = None
    """AWS Session Token to use"""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    max_retries: Optional[int] = None
    """The maximum number of API retries."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Bedrock model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    profile_name: Optional[str] = None
    """The name of aws profile to use. If not given, then the default profile is used."""

    region_name: Optional[str] = None
    """AWS region name to use. Uses region configured in AWS CLI if not passed"""

    timeout: Optional[float] = None
    """The timeout for the Bedrock API request in seconds.

    It will be used for both connect and read timeouts.
    """


class EmbeddingConfigBedrockEmbeddingConfig(BaseModel):
    component: Optional[EmbeddingConfigBedrockEmbeddingConfigComponent] = None
    """Configuration for the Bedrock embedding model."""

    type: Optional[Literal["BEDROCK_EMBEDDING"]] = None
    """Type of the embedding model."""


EmbeddingConfig: TypeAlias = Annotated[
    Union[
        EmbeddingConfigAzureOpenAIEmbeddingConfig,
        EmbeddingConfigCohereEmbeddingConfig,
        EmbeddingConfigGeminiEmbeddingConfig,
        EmbeddingConfigHuggingFaceInferenceAPIEmbeddingConfig,
        EmbeddingConfigOpenAIEmbeddingConfig,
        EmbeddingConfigVertexAIEmbeddingConfig,
        EmbeddingConfigBedrockEmbeddingConfig,
    ],
    PropertyInfo(discriminator="type"),
]


class EmbeddingModelConfig(BaseModel):
    id: str
    """Unique identifier"""

    embedding_config: EmbeddingConfig
    """The embedding configuration for the embedding model config."""

    name: str
    """The name of the embedding model config."""

    project_id: str

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
