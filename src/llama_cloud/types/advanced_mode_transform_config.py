# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AdvancedModeTransformConfig",
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


class ChunkingConfigNoneChunkingConfig(BaseModel):
    mode: Optional[Literal["none"]] = None


class ChunkingConfigCharacterChunkingConfig(BaseModel):
    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    mode: Optional[Literal["character"]] = None


class ChunkingConfigTokenChunkingConfig(BaseModel):
    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    mode: Optional[Literal["token"]] = None

    separator: Optional[str] = None


class ChunkingConfigSentenceChunkingConfig(BaseModel):
    chunk_overlap: Optional[int] = None

    chunk_size: Optional[int] = None

    mode: Optional[Literal["sentence"]] = None

    paragraph_separator: Optional[str] = None

    separator: Optional[str] = None


class ChunkingConfigSemanticChunkingConfig(BaseModel):
    breakpoint_percentile_threshold: Optional[int] = None

    buffer_size: Optional[int] = None

    mode: Optional[Literal["semantic"]] = None


ChunkingConfig: TypeAlias = Union[
    ChunkingConfigNoneChunkingConfig,
    ChunkingConfigCharacterChunkingConfig,
    ChunkingConfigTokenChunkingConfig,
    ChunkingConfigSentenceChunkingConfig,
    ChunkingConfigSemanticChunkingConfig,
]


class SegmentationConfigNoneSegmentationConfig(BaseModel):
    mode: Optional[Literal["none"]] = None


class SegmentationConfigPageSegmentationConfig(BaseModel):
    mode: Optional[Literal["page"]] = None

    page_separator: Optional[str] = None


class SegmentationConfigElementSegmentationConfig(BaseModel):
    mode: Optional[Literal["element"]] = None


SegmentationConfig: TypeAlias = Union[
    SegmentationConfigNoneSegmentationConfig,
    SegmentationConfigPageSegmentationConfig,
    SegmentationConfigElementSegmentationConfig,
]


class AdvancedModeTransformConfig(BaseModel):
    chunking_config: Optional[ChunkingConfig] = None
    """Configuration for the chunking."""

    mode: Optional[Literal["advanced"]] = None

    segmentation_config: Optional[SegmentationConfig] = None
    """Configuration for the segmentation."""
