# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ClassifyConfiguration", "Rule", "ParsingConfiguration"]


class Rule(BaseModel):
    """A rule for classifying documents."""

    description: str
    """Natural language criteria for matching this rule"""

    type: str
    """Document type to assign when rule matches"""


class ParsingConfiguration(BaseModel):
    """Parsing configuration for classify jobs."""

    lang: Optional[str] = None
    """ISO 639-1 language code for the document"""

    max_pages: Optional[int] = None
    """Maximum number of pages to process. Omit for no limit."""

    target_pages: Optional[str] = None
    """Comma-separated page numbers or ranges to process (1-based).

    Omit to process all pages.
    """


class ClassifyConfiguration(BaseModel):
    """Configuration for a classify job."""

    rules: List[Rule]
    """Classify rules to evaluate against the document (at least one required)"""

    mode: Optional[Literal["FAST"]] = None
    """Classify execution mode"""

    parsing_configuration: Optional[ParsingConfiguration] = None
    """Parsing configuration for classify jobs."""
