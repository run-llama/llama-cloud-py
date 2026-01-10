# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .openai_embedding import OpenAIEmbedding

__all__ = ["OpenAIEmbeddingConfig"]


class OpenAIEmbeddingConfig(BaseModel):
    component: Optional[OpenAIEmbedding] = None
    """Configuration for the OpenAI embedding model."""

    type: Optional[Literal["OPENAI_EMBEDDING"]] = None
    """Type of the embedding model."""
