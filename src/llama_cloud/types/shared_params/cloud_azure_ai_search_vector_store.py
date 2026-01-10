# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudAzureAISearchVectorStore"]


class CloudAzureAISearchVectorStore(TypedDict, total=False):
    """Cloud Azure AI Search Vector Store."""

    search_service_api_key: Required[str]

    search_service_endpoint: Required[str]

    class_name: str

    client_id: Optional[str]

    client_secret: Optional[str]

    embedding_dimension: Optional[int]

    filterable_metadata_field_keys: Optional[Dict[str, object]]

    index_name: Optional[str]

    search_service_api_version: Optional[str]

    supports_nested_metadata_filters: Literal[True]

    tenant_id: Optional[str]
