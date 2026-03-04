# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClassifyConfigurationParam", "Rule"]


class Rule(TypedDict, total=False):
    """A rule for classifying documents."""

    description: Required[str]
    """Natural language description of what to classify"""

    type: Required[str]
    """Document type to assign when rule matches"""


class ClassifyConfigurationParam(TypedDict, total=False):
    """Configuration for classification."""

    rules: Required[Iterable[Rule]]
    """Classification rules to apply (at least one required)"""

    mode: Literal["FAST"]
    """Classification execution mode"""
