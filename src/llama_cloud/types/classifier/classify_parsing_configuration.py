# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..parser_languages import ParserLanguages

__all__ = ["ClassifyParsingConfiguration"]


class ClassifyParsingConfiguration(BaseModel):
    lang: Optional[ParserLanguages] = None
    """The language to parse the files in"""

    max_pages: Optional[int] = None
    """The maximum number of pages to parse"""

    target_pages: Optional[List[int]] = None
    """The pages to target for parsing (0-indexed, so first page is at 0)"""
