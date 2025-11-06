# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PipelineMetadataConfigParam"]


class PipelineMetadataConfigParam(TypedDict, total=False):
    excluded_embed_metadata_keys: SequenceNotStr[str]
    """List of metadata keys to exclude from embeddings"""

    excluded_llm_metadata_keys: SequenceNotStr[str]
    """List of metadata keys to exclude from LLM during retrieval"""
