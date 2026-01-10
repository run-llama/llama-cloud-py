# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .hugging_face_inference_api_embedding_param import HuggingFaceInferenceAPIEmbeddingParam

__all__ = ["HuggingFaceInferenceAPIEmbeddingConfigParam"]


class HuggingFaceInferenceAPIEmbeddingConfigParam(TypedDict, total=False):
    component: HuggingFaceInferenceAPIEmbeddingParam
    """Configuration for the HuggingFace Inference API embedding model."""

    type: Literal["HUGGINGFACE_API_EMBEDDING"]
    """Type of the embedding model."""
