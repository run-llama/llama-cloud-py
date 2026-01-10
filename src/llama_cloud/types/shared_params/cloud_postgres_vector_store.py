# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .pg_vector_hnsw_settings import PgVectorHnswSettings

__all__ = ["CloudPostgresVectorStore"]


class CloudPostgresVectorStore(TypedDict, total=False):
    database: Required[str]

    embed_dim: Required[int]

    host: Required[str]

    password: Required[str]

    port: Required[int]

    schema_name: Required[str]

    table_name: Required[str]

    user: Required[str]

    class_name: str

    hnsw_settings: Optional[PgVectorHnswSettings]
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool]

    perform_setup: bool

    supports_nested_metadata_filters: bool
