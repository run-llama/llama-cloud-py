# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DeleteParams"]


class DeleteParams(BaseModel):
    data_sink_id: Optional[str] = None
    """The ID for the data sink from which to delete data."""

    data_sources_ids_to_delete: Optional[List[str]] = None
    """The IDs for the data sources to delete."""

    document_ids_to_delete: Optional[List[str]] = None
    """The IDs for the documents to delete."""

    embed_collection_name: Optional[str] = None
    """The collection name to delete."""

    files_ids_to_delete: Optional[List[str]] = None
    """The IDs for the files to delete."""
