# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudPostgresVectorStoreParam", "HnswSettings"]


class HnswSettings(TypedDict, total=False):
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


class CloudPostgresVectorStoreParam(TypedDict, total=False):
    database: Required[str]

    embed_dim: Required[int]

    host: Required[str]

    password: Required[str]

    port: Required[int]

    schema_name: Required[str]

    table_name: Required[str]

    user: Required[str]

    class_name: str

    hnsw_settings: Optional[HnswSettings]
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool]

    perform_setup: bool

    supports_nested_metadata_filters: bool
