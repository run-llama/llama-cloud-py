# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .azure_openai_embedding_param import AzureOpenAIEmbeddingParam

__all__ = ["AzureOpenAIEmbeddingConfigParam"]


class AzureOpenAIEmbeddingConfigParam(TypedDict, total=False):
    component: AzureOpenAIEmbeddingParam
    """Configuration for the Azure OpenAI embedding model."""

    type: Literal["AZURE_EMBEDDING"]
    """Type of the embedding model."""
