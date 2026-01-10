# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AzureOpenAIEmbedding"]


class AzureOpenAIEmbedding(BaseModel):
    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the OpenAI API."""

    api_base: Optional[str] = None
    """The base URL for Azure deployment."""

    api_key: Optional[str] = None
    """The OpenAI API key."""

    api_version: Optional[str] = None
    """The version for Azure OpenAI API."""

    azure_deployment: Optional[str] = None
    """The Azure deployment to use."""

    azure_endpoint: Optional[str] = None
    """The Azure endpoint to use."""

    class_name: Optional[str] = None

    default_headers: Optional[Dict[str, str]] = None
    """The default headers for API requests."""

    dimensions: Optional[int] = None
    """The number of dimensions on the output embedding vectors.

    Works only with v3 embedding models.
    """

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    max_retries: Optional[int] = None
    """Maximum number of retries."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The name of the OpenAI embedding model."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    reuse_client: Optional[bool] = None
    """Reuse the OpenAI client between requests.

    When doing anything with large volumes of async API calls, setting this to false
    can improve stability.
    """

    timeout: Optional[float] = None
    """Timeout for each request."""
