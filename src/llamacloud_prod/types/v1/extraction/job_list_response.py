# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .extract_job import ExtractJob

__all__ = ["JobListResponse"]

JobListResponse: TypeAlias = List[ExtractJob]
