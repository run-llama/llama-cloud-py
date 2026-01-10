# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["OpenAIEmbeddingParam"]


class OpenAIEmbeddingParam(TypedDict, total=False):
    additional_kwargs: Dict[str, object]
    """Additional kwargs for the OpenAI API."""

    api_base: Optional[str]
    """The base URL for OpenAI API."""

    api_key: Optional[str]
    """The OpenAI API key."""

    api_version: Optional[str]
    """The version for OpenAI API."""

    class_name: str

    default_headers: Optional[Dict[str, str]]
    """The default headers for API requests."""

    dimensions: Optional[int]
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: int
    """The batch size for embedding calls."""

    max_retries: int
    """Maximum number of retries."""

    model_name: str
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    reuse_client: bool
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: float
    """Timeout for each request."""
