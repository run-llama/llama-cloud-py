# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BetaRetrieveQuotaManagementParams"]


class BetaRetrieveQuotaManagementParams(TypedDict, total=False):
    source_id: Required[str]

    source_type: Required[Literal["organization"]]

    page: int

    page_size: int
