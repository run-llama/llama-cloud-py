# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .._models import BaseModel
from .pipelines.text_node import TextNode
from .page_figure_node_with_score import PageFigureNodeWithScore
from .page_screenshot_node_with_score import PageScreenshotNodeWithScore

__all__ = ["PipelineRetrieveResponse", "RetrievalNode"]


class RetrievalNode(BaseModel):
    """
    Same as NodeWithScore but type for node is a TextNode instead of BaseNode.
    FastAPI doesn't accept abstract classes like BaseNode.
    """

    node: TextNode
    """Provided for backward compatibility.

    Note: we keep the field with the typo "seperator" to maintain backward
    compatibility for serialized objects.
    """

    class_name: Optional[str] = None

    score: Optional[float] = None


class PipelineRetrieveResponse(BaseModel):
    """Schema for the result of an retrieval execution."""

    pipeline_id: str
    """The ID of the pipeline that the query was retrieved against."""

    retrieval_nodes: List[RetrievalNode]
    """The nodes retrieved by the pipeline for the given query."""

    class_name: Optional[str] = None

    image_nodes: Optional[List[PageScreenshotNodeWithScore]] = None
    """The image nodes retrieved by the pipeline for the given query.

    Deprecated - will soon be replaced with 'page_screenshot_nodes'.
    """

    inferred_search_filters: Optional["MetadataFilters"] = None
    """Metadata filters for vector stores."""

    metadata: Optional[Dict[str, str]] = None
    """Metadata associated with the retrieval execution"""

    page_figure_nodes: Optional[List[PageFigureNodeWithScore]] = None
    """The page figure nodes retrieved by the pipeline for the given query."""

    retrieval_latency: Optional[Dict[str, float]] = None
    """The end-to-end latency for retrieval and reranking."""


from .metadata_filters import MetadataFilters
