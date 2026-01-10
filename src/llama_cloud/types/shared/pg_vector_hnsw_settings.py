# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PgVectorHnswSettings"]


class PgVectorHnswSettings(BaseModel):
    """HNSW settings for PGVector."""

    distance_method: Optional[Literal["l2", "ip", "cosine", "l1", "hamming", "jaccard"]] = None
    """The distance method to use."""

    ef_construction: Optional[int] = None
    """The number of edges to use during the construction phase."""

    ef_search: Optional[int] = None
    """The number of edges to use during the search phase."""

    m: Optional[int] = None
    """The number of bi-directional links created for each new element."""

    vector_type: Optional[Literal["vector", "half_vec", "bit", "sparse_vec"]] = None
    """The type of vector to use."""
