# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .text_node import TextNode

__all__ = ["DocumentGetChunksResponse"]

DocumentGetChunksResponse: TypeAlias = List[TextNode]
