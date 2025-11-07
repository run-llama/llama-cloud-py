# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SpreadsheetGetResultTableParams"]


class SpreadsheetGetResultTableParams(TypedDict, total=False):
    spreadsheet_job_id: Required[str]

    table_id: Required[str]

    expires_at_seconds: Optional[int]

    organization_id: Optional[str]

    project_id: Optional[str]
