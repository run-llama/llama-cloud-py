# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CloudPineconeVectorStore"]


class CloudPineconeVectorStore(BaseModel):
    index_name: str

    class_name: Optional[str] = None

    insert_kwargs: Optional[Dict[str, object]] = None

    namespace: Optional[str] = None

    supports_nested_metadata_filters: Optional[Literal[True]] = None
