# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .pg_vector_hnsw_settings import PgVectorHnswSettings

__all__ = ["CloudPostgresVectorStore"]


class CloudPostgresVectorStore(BaseModel):
    database: str

    embed_dim: int

    host: str

    port: int

    schema_name: str

    table_name: str

    user: str

    class_name: Optional[str] = None

    hnsw_settings: Optional[PgVectorHnswSettings] = None
    """HNSW settings for PGVector."""

    hybrid_search: Optional[bool] = None

    perform_setup: Optional[bool] = None

    supports_nested_metadata_filters: Optional[bool] = None
