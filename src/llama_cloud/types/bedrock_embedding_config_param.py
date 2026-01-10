# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .bedrock_embedding_param import BedrockEmbeddingParam

__all__ = ["BedrockEmbeddingConfigParam"]


class BedrockEmbeddingConfigParam(TypedDict, total=False):
    component: BedrockEmbeddingParam
    """Configuration for the Bedrock embedding model."""

    type: Literal["BEDROCK_EMBEDDING"]
    """Type of the embedding model."""
