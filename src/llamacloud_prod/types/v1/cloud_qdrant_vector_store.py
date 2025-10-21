# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudQdrantVectorStore"]


class CloudQdrantVectorStore(BaseModel):
    collection_name: str

    url: str

    class_name: Optional[str] = None

    client_kwargs: Optional[Dict[str, object]] = None

    max_retries: Optional[int] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None
