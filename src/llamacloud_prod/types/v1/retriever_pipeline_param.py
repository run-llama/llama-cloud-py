# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RetrieverPipelineParam"]


class RetrieverPipelineParam(TypedDict, total=False):
    description: Required[Optional[str]]
    """A description of the retriever tool."""

    name: Required[Optional[str]]
    """A name for the retriever tool.

    Will default to the pipeline name if not provided.
    """

    pipeline_id: Required[str]
    """The ID of the pipeline this tool uses."""

    preset_retrieval_parameters: "PresetRetrievalParamsParam"
    """Parameters for retrieval configuration."""


from .preset_retrieval_params_param import PresetRetrievalParamsParam
