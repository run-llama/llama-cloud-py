# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .gemini_embedding_param import GeminiEmbeddingParam

__all__ = ["GeminiEmbeddingConfigParam"]


class GeminiEmbeddingConfigParam(TypedDict, total=False):
    component: GeminiEmbeddingParam
    """Configuration for the Gemini embedding model."""

    type: Literal["GEMINI_EMBEDDING"]
    """Type of the embedding model."""
