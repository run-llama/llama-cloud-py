# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["GeminiEmbeddingParam"]


class GeminiEmbeddingParam(TypedDict, total=False):
    api_base: Optional[str]
    """API base to access the model. Defaults to None."""

    api_key: Optional[str]
    """API key to access the model. Defaults to None."""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    model_name: str
    """The modelId of the Gemini model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    task_type: Optional[str]
    """The task for embedding model."""

    title: Optional[str]
    """
    Title is only applicable for retrieval_document tasks, and is used to represent
    a document title. For other tasks, title is invalid.
    """

    transport: Optional[str]
    """Transport to access the model. Defaults to None."""
