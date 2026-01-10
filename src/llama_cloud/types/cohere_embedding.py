# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CohereEmbedding"]


class CohereEmbedding(BaseModel):
    api_key: Optional[str] = None
    """The Cohere API key."""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    embedding_type: Optional[str] = None
    """Embedding type. If not provided float embedding_type is used when needed."""

    input_type: Optional[str] = None
    """Model Input type.

    If not provided, search_document and search_query are used when needed.
    """

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Cohere model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    truncate: Optional[str] = None
    """Truncation type - START/ END/ NONE"""
