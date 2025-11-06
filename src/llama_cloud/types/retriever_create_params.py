# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrieverCreateParams"]


class RetrieverCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the retriever tool.

    Will default to the pipeline name if not provided.
    """

    organization_id: Optional[str]

    project_id: Optional[str]

    pipelines: Iterable["RetrieverPipelineParam"]
    """The pipelines this retriever uses."""


from .retriever_pipeline_param import RetrieverPipelineParam
