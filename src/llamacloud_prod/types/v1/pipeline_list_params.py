# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .pipeline_type import PipelineType

__all__ = ["PipelineListParams"]


class PipelineListParams(TypedDict, total=False):
    organization_id: Optional[str]

    pipeline_name: Optional[str]

    pipeline_type: Optional[PipelineType]
    """Enum for representing the type of a pipeline"""

    project_id: Optional[str]

    project_name: Optional[str]
