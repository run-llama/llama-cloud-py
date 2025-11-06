# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .parsing_history_item import ParsingHistoryItem

__all__ = ["ParsingGetParsingHistoryResponse"]

ParsingGetParsingHistoryResponse: TypeAlias = List[ParsingHistoryItem]
