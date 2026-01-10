# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CohereEmbeddingParam"]


class CohereEmbeddingParam(TypedDict, total=False):
    api_key: Required[Optional[str]]
    """The Cohere API key."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    embedding_type: str
    """Embedding type. If not provided float embedding_type is used when needed."""

    input_type: Optional[str]
    """Model Input type.

    If not provided, search_document and search_query are used when needed.
    """

    model_name: str
    """The modelId of the Cohere model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    truncate: str
    """Truncation type - START/ END/ NONE"""
