# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ClassifyConfiguration", "Rule", "ParsingConfiguration"]


class Rule(BaseModel):
    """A rule for classifying documents."""

    description: str
    """Natural language description of what to classify"""

    type: str
    """Document type to assign when rule matches"""


class ParsingConfiguration(BaseModel):
    """Parsing configuration for classify jobs."""

    lang: Optional[str] = None
    """Language of the document"""

    max_pages: Optional[int] = None
    """Maximum number of pages to process"""

    target_pages: Optional[str] = None
    """
    Comma-separated list of page numbers or ranges to process (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10')
    """


class ClassifyConfiguration(BaseModel):
    """Configuration for classification."""

    rules: List[Rule]
    """Classification rules to apply (at least one required)"""

    mode: Optional[Literal["FAST"]] = None
    """Classification execution mode"""

    parsing_configuration: Optional[ParsingConfiguration] = None
    """Parsing configuration for classify jobs."""
