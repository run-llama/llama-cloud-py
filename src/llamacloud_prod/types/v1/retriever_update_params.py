# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrieverUpdateParams"]


class RetrieverUpdateParams(TypedDict, total=False):
    pipelines: Required[Optional[Iterable["RetrieverPipelineParam"]]]
    """The pipelines this retriever uses."""

    name: Optional[str]
    """A name for the retriever."""


from .retriever_pipeline_param import RetrieverPipelineParam
