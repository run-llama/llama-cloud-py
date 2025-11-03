# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetronomeGetDashboardParams"]


class MetronomeGetDashboardParams(TypedDict, total=False):
    organization_id: Required[str]

    dashboard_type: Literal["invoices", "usage"]
    """The type of dashboard to get"""
