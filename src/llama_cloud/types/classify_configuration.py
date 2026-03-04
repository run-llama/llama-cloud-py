# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ClassifyConfiguration", "Rule"]


class Rule(BaseModel):
    """A rule for classifying documents."""

    description: str
    """Natural language description of what to classify"""

    type: str
    """Document type to assign when rule matches"""


class ClassifyConfiguration(BaseModel):
    """Configuration for classification."""

    rules: List[Rule]
    """Classification rules to apply (at least one required)"""

    mode: Optional[Literal["FAST"]] = None
    """Classification execution mode"""
