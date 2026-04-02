# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClassifyV2ParametersParam", "Rule", "ParsingConfiguration"]


class Rule(TypedDict, total=False):
    """A rule for classifying documents."""

    description: Required[str]
    """Natural language criteria for matching this rule"""

    type: Required[str]
    """Document type to assign when rule matches"""


class ParsingConfiguration(TypedDict, total=False):
    """Parsing configuration for classify jobs."""

    lang: str
    """ISO 639-1 language code for the document"""

    max_pages: Optional[int]
    """Maximum number of pages to process. Omit for no limit."""

    target_pages: Optional[str]
    """Comma-separated page numbers or ranges to process (1-based).

    Omit to process all pages.
    """


class ClassifyV2ParametersParam(TypedDict, total=False):
    """Typed parameters for a *classify v2* product configuration."""

    product_type: Required[Literal["classify_v2"]]
    """Product type."""

    rules: Required[Iterable[Rule]]
    """Classify rules to evaluate against the document (at least one required)"""

    mode: Literal["FAST"]
    """Classify execution mode"""

    parsing_configuration: Optional[ParsingConfiguration]
    """Parsing configuration for classify jobs."""
