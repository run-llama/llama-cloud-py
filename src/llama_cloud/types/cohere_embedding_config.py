# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .cohere_embedding import CohereEmbedding

__all__ = ["CohereEmbeddingConfig"]


class CohereEmbeddingConfig(BaseModel):
    component: Optional[CohereEmbedding] = None
    """Configuration for the Cohere embedding model."""

    type: Optional[Literal["COHERE_EMBEDDING"]] = None
    """Type of the embedding model."""
