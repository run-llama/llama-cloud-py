# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PgVectorHnswSettings"]


class PgVectorHnswSettings(TypedDict, total=False):
    """HNSW settings for PGVector."""

    distance_method: Literal["l2", "ip", "cosine", "l1", "hamming", "jaccard"]
    """The distance method to use."""

    ef_construction: int
    """The number of edges to use during the construction phase."""

    ef_search: int
    """The number of edges to use during the search phase."""

    m: int
    """The number of bi-directional links created for each new element."""

    vector_type: Literal["vector", "half_vec", "bit", "sparse_vec"]
    """The type of vector to use."""
