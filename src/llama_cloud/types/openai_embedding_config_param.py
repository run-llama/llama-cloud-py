# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .openai_embedding_param import OpenAIEmbeddingParam

__all__ = ["OpenAIEmbeddingConfigParam"]


class OpenAIEmbeddingConfigParam(TypedDict, total=False):
    component: OpenAIEmbeddingParam
    """Configuration for the OpenAI embedding model."""

    type: Literal["OPENAI_EMBEDDING"]
    """Type of the embedding model."""
