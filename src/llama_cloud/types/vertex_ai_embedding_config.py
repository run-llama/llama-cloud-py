# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .vertex_text_embedding import VertexTextEmbedding

__all__ = ["VertexAIEmbeddingConfig"]


class VertexAIEmbeddingConfig(BaseModel):
    component: Optional[VertexTextEmbedding] = None
    """Configuration for the VertexAI embedding model."""

    type: Optional[Literal["VERTEXAI_EMBEDDING"]] = None
    """Type of the embedding model."""
