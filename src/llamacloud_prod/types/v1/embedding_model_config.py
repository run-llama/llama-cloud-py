# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .cohere_embedding_config import CohereEmbeddingConfig
from .gemini_embedding_config import GeminiEmbeddingConfig
from .openai_embedding_config import OpenAIEmbeddingConfig
from .bedrock_embedding_config import BedrockEmbeddingConfig
from .vertex_ai_embedding_config import VertexAIEmbeddingConfig
from .azure_openai_embedding_config import AzureOpenAIEmbeddingConfig
from .hugging_face_inference_api_embedding_config import HuggingFaceInferenceAPIEmbeddingConfig

__all__ = ["EmbeddingModelConfig", "EmbeddingConfig"]

EmbeddingConfig: TypeAlias = Annotated[
    Union[
        AzureOpenAIEmbeddingConfig,
        BedrockEmbeddingConfig,
        CohereEmbeddingConfig,
        GeminiEmbeddingConfig,
        HuggingFaceInferenceAPIEmbeddingConfig,
        OpenAIEmbeddingConfig,
        VertexAIEmbeddingConfig,
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
