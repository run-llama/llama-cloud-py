# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutoTransformConfig"]


class AutoTransformConfig(BaseModel):
    chunk_overlap: Optional[int] = None
    """Chunk overlap for the transformation."""

    chunk_size: Optional[int] = None
    """Chunk size for the transformation."""

    mode: Optional[Literal["auto"]] = None
