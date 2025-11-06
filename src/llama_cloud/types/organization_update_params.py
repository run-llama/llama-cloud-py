# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the organization."""

    feature_flags: Optional[Dict[str, object]]
    """Feature flags for the organization."""
