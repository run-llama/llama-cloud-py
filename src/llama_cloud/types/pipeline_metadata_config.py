# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PipelineMetadataConfig"]


class PipelineMetadataConfig(BaseModel):
    excluded_embed_metadata_keys: Optional[List[str]] = None
    """List of metadata keys to exclude from embeddings"""

    excluded_llm_metadata_keys: Optional[List[str]] = None
    """List of metadata keys to exclude from LLM during retrieval"""
