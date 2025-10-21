# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["ParsingCreateScreenshotParams"]


class ParsingCreateScreenshotParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    do_not_cache: bool

    file: Optional[FileTypes]

    http_proxy: str

    input_s3_path: str

    input_s3_region: str

    input_url: str

    invalidate_cache: bool

    job_timeout_extra_time_per_page_in_seconds: float

    job_timeout_in_seconds: float

    max_pages: Optional[int]

    output_s3_path_prefix: str

    output_s3_region: str

    target_pages: str

    webhook_configurations: str

    webhook_url: str
