# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AutoTransformConfigParam"]


class AutoTransformConfigParam(TypedDict, total=False):
    chunk_overlap: int
    """Chunk overlap for the transformation."""

    chunk_size: int
    """Chunk size for the transformation."""

    mode: Literal["auto"]
