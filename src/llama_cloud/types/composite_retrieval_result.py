# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .page_figure_node_with_score import PageFigureNodeWithScore
from .page_screenshot_node_with_score import PageScreenshotNodeWithScore

__all__ = ["CompositeRetrievalResult", "Node", "NodeNode"]


class NodeNode(BaseModel):
    id: str
    """The ID of the retrieved node."""

    end_char_idx: Optional[int] = None
    """The end character index of the retrieved node in the document"""

    pipeline_id: str
    """The ID of the pipeline this node was retrieved from."""

    retriever_id: str
    """The ID of the retriever this node was retrieved from."""

    retriever_pipeline_name: str
    """The name of the retrieval pipeline this node was retrieved from."""

    start_char_idx: Optional[int] = None
    """The start character index of the retrieved node in the document"""

    text: str
    """The text of the retrieved node."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata associated with the retrieved node."""


class Node(BaseModel):
    node: NodeNode

    class_name: Optional[str] = None

    score: Optional[float] = None


class CompositeRetrievalResult(BaseModel):
    image_nodes: Optional[List[PageScreenshotNodeWithScore]] = None
    """The image nodes retrieved by the pipeline for the given query.

    Deprecated - will soon be replaced with 'page_screenshot_nodes'.
    """

    nodes: Optional[List[Node]] = None
    """The retrieved nodes from the composite retrieval."""

    page_figure_nodes: Optional[List[PageFigureNodeWithScore]] = None
    """The page figure nodes retrieved by the pipeline for the given query."""
