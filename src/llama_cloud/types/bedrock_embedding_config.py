# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .bedrock_embedding import BedrockEmbedding

__all__ = ["BedrockEmbeddingConfig"]


class BedrockEmbeddingConfig(BaseModel):
    component: Optional[BedrockEmbedding] = None
    """Configuration for the Bedrock embedding model."""

    type: Optional[Literal["BEDROCK_EMBEDDING"]] = None
    """Type of the embedding model."""
