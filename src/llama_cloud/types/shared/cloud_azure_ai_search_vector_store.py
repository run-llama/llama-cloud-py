# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudAzureAISearchVectorStore"]


class CloudAzureAISearchVectorStore(BaseModel):
    """Cloud Azure AI Search Vector Store."""

    search_service_endpoint: str

    class_name: Optional[str] = None

    client_id: Optional[str] = None

    embedding_dimension: Optional[int] = None

    filterable_metadata_field_keys: Optional[Dict[str, object]] = None

    index_name: Optional[str] = None

    search_service_api_version: Optional[str] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None

    tenant_id: Optional[str] = None
