# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudQdrantVectorStoreParam"]


class CloudQdrantVectorStoreParam(TypedDict, total=False):
    api_key: Required[str]

    collection_name: Required[str]

    url: Required[str]

    class_name: str

    client_kwargs: Dict[str, object]

    max_retries: int

    supports_nested_metadata_filters: Literal[True]
