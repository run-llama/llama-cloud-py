# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .hugging_face_inference_api_embedding import HuggingFaceInferenceAPIEmbedding

__all__ = ["HuggingFaceInferenceAPIEmbeddingConfig"]


class HuggingFaceInferenceAPIEmbeddingConfig(BaseModel):
    component: Optional[HuggingFaceInferenceAPIEmbedding] = None
    """Configuration for the HuggingFace Inference API embedding model."""

    type: Optional[Literal["HUGGINGFACE_API_EMBEDDING"]] = None
    """Type of the embedding model."""
