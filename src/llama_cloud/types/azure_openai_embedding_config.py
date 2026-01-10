# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .azure_openai_embedding import AzureOpenAIEmbedding

__all__ = ["AzureOpenAIEmbeddingConfig"]


class AzureOpenAIEmbeddingConfig(BaseModel):
    component: Optional[AzureOpenAIEmbedding] = None
    """Configuration for the Azure OpenAI embedding model."""

    type: Optional[Literal["AZURE_EMBEDDING"]] = None
    """Type of the embedding model."""
