# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClassifyConfigurationParam", "Rule", "ParsingConfiguration"]


class Rule(TypedDict, total=False):
    """A rule for classifying documents."""

    description: Required[str]
    """Natural language description of what to classify"""

    type: Required[str]
    """Document type to assign when rule matches"""


class ParsingConfiguration(TypedDict, total=False):
    """Parsing configuration for classify jobs."""

    lang: str
    """Language of the document"""

    max_pages: Optional[int]
    """Maximum number of pages to process"""

    target_pages: Optional[str]
    """
    Comma-separated list of page numbers or ranges to process (1-based, e.g.,
    '1,3,5-7,9' or '1-3,8-10')
    """


class ClassifyConfigurationParam(TypedDict, total=False):
    """Configuration for classification."""

    rules: Required[Iterable[Rule]]
    """Classification rules to apply (at least one required)"""

    mode: Literal["FAST"]
    """Classification execution mode"""

    parsing_configuration: Optional[ParsingConfiguration]
    """Parsing configuration for classify jobs."""
