# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .cohere_embedding_config_param import CohereEmbeddingConfigParam
from .gemini_embedding_config_param import GeminiEmbeddingConfigParam
from .openai_embedding_config_param import OpenAIEmbeddingConfigParam
from .bedrock_embedding_config_param import BedrockEmbeddingConfigParam
from .vertex_ai_embedding_config_param import VertexAIEmbeddingConfigParam
from .azure_openai_embedding_config_param import AzureOpenAIEmbeddingConfigParam
from .hugging_face_inference_api_embedding_config_param import HuggingFaceInferenceAPIEmbeddingConfigParam

__all__ = ["EmbeddingModelConfigUpdateParams", "EmbeddingConfig"]


class EmbeddingModelConfigUpdateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    embedding_config: Optional[EmbeddingConfig]
    """The embedding configuration for the embedding model config."""

    name: Optional[str]
    """The name of the embedding model config."""


EmbeddingConfig: TypeAlias = Union[
    AzureOpenAIEmbeddingConfigParam,
    BedrockEmbeddingConfigParam,
    CohereEmbeddingConfigParam,
    GeminiEmbeddingConfigParam,
    HuggingFaceInferenceAPIEmbeddingConfigParam,
    OpenAIEmbeddingConfigParam,
    VertexAIEmbeddingConfigParam,
]
