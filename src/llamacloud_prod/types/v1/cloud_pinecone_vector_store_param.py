# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudPineconeVectorStoreParam"]


class CloudPineconeVectorStoreParam(TypedDict, total=False):
    api_key: Required[str]
    """The API key for authenticating with Pinecone"""

    index_name: Required[str]

    class_name: str

    insert_kwargs: Optional[Dict[str, object]]

    namespace: Optional[str]

    supports_nested_metadata_filters: Literal[True]
