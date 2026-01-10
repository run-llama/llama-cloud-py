# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .vertex_text_embedding_param import VertexTextEmbeddingParam

__all__ = ["VertexAIEmbeddingConfigParam"]


class VertexAIEmbeddingConfigParam(TypedDict, total=False):
    component: VertexTextEmbeddingParam
    """Configuration for the VertexAI embedding model."""

    type: Literal["VERTEXAI_EMBEDDING"]
    """Type of the embedding model."""
