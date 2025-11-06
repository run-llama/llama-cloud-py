# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["RetrieverPipeline"]


class RetrieverPipeline(BaseModel):
    description: Optional[str] = None
    """A description of the retriever tool."""

    name: Optional[str] = None
    """A name for the retriever tool.

    Will default to the pipeline name if not provided.
    """

    pipeline_id: str
    """The ID of the pipeline this tool uses."""

    preset_retrieval_parameters: Optional["PresetRetrievalParams"] = None
    """Parameters for retrieval configuration."""


from .preset_retrieval_params import PresetRetrievalParams
