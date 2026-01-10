# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GeminiEmbedding"]


class GeminiEmbedding(BaseModel):
    api_base: Optional[str] = None
    """API base to access the model. Defaults to None."""

    api_key: Optional[str] = None
    """API key to access the model. Defaults to None."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Gemini model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    task_type: Optional[str] = None
    """The task for embedding model."""

    title: Optional[str] = None
    """
    Title is only applicable for retrieval_document tasks, and is used to represent
    a document title. For other tasks, title is invalid.
    """

    transport: Optional[str] = None
    """Transport to access the model. Defaults to None."""
