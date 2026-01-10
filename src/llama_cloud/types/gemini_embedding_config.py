# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .gemini_embedding import GeminiEmbedding

__all__ = ["GeminiEmbeddingConfig"]


class GeminiEmbeddingConfig(BaseModel):
    component: Optional[GeminiEmbedding] = None
    """Configuration for the Gemini embedding model."""

    type: Optional[Literal["GEMINI_EMBEDDING"]] = None
    """Type of the embedding model."""
