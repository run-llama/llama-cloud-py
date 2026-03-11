# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .extract_options_param import ExtractOptionsParam

__all__ = ["ExtractConfigurationParam"]


class ExtractConfigurationParam(TypedDict, total=False):
    """Extraction configuration combining parse and extract settings."""

    extract_options: Required[ExtractOptionsParam]
    """Extract-specific configuration options including the data schema"""

    parse_config_id: Optional[str]
    """Parse config ID used for extraction"""

    parse_tier: Optional[str]
    """Parse tier to use for extraction (e.g. fast, cost_effective, agentic)."""
