# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .cohere_embedding_param import CohereEmbeddingParam

__all__ = ["CohereEmbeddingConfigParam"]


class CohereEmbeddingConfigParam(TypedDict, total=False):
    component: CohereEmbeddingParam
    """Configuration for the Cohere embedding model."""

    type: Literal["COHERE_EMBEDDING"]
    """Type of the embedding model."""
