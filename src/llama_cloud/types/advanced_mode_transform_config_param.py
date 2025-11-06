# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "AdvancedModeTransformConfigParam",
    "ChunkingConfig",
    "ChunkingConfigNoneChunkingConfig",
    "ChunkingConfigCharacterChunkingConfig",
    "ChunkingConfigTokenChunkingConfig",
    "ChunkingConfigSentenceChunkingConfig",
    "ChunkingConfigSemanticChunkingConfig",
    "SegmentationConfig",
    "SegmentationConfigNoneSegmentationConfig",
    "SegmentationConfigPageSegmentationConfig",
    "SegmentationConfigElementSegmentationConfig",
]


class ChunkingConfigNoneChunkingConfig(TypedDict, total=False):
    mode: Literal["none"]


class ChunkingConfigCharacterChunkingConfig(TypedDict, total=False):
    chunk_overlap: int

    chunk_size: int

    mode: Literal["character"]


class ChunkingConfigTokenChunkingConfig(TypedDict, total=False):
    chunk_overlap: int

    chunk_size: int

    mode: Literal["token"]

    separator: str


class ChunkingConfigSentenceChunkingConfig(TypedDict, total=False):
    chunk_overlap: int

    chunk_size: int

    mode: Literal["sentence"]

    paragraph_separator: str

    separator: str


class ChunkingConfigSemanticChunkingConfig(TypedDict, total=False):
    breakpoint_percentile_threshold: int

    buffer_size: int

    mode: Literal["semantic"]


ChunkingConfig: TypeAlias = Union[
    ChunkingConfigNoneChunkingConfig,
    ChunkingConfigCharacterChunkingConfig,
    ChunkingConfigTokenChunkingConfig,
    ChunkingConfigSentenceChunkingConfig,
    ChunkingConfigSemanticChunkingConfig,
]


class SegmentationConfigNoneSegmentationConfig(TypedDict, total=False):
    mode: Literal["none"]


class SegmentationConfigPageSegmentationConfig(TypedDict, total=False):
    mode: Literal["page"]

    page_separator: str


class SegmentationConfigElementSegmentationConfig(TypedDict, total=False):
    mode: Literal["element"]


SegmentationConfig: TypeAlias = Union[
    SegmentationConfigNoneSegmentationConfig,
    SegmentationConfigPageSegmentationConfig,
    SegmentationConfigElementSegmentationConfig,
]


class AdvancedModeTransformConfigParam(TypedDict, total=False):
    chunking_config: ChunkingConfig
    """Configuration for the chunking."""

    mode: Literal["advanced"]

    segmentation_config: SegmentationConfig
    """Configuration for the segmentation."""
