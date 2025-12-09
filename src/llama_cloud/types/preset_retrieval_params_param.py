# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypedDict

from .retrieval_mode import RetrievalMode

__all__ = ["PresetRetrievalParamsParam"]


class PresetRetrievalParamsParam(TypedDict, total=False):
    """
    Schema for the search params for an retrieval execution that can be preset for a pipeline.
    """

    alpha: Optional[float]
    """
    Alpha value for hybrid retrieval to determine the weights between dense and
    sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.
    """

    class_name: str

    dense_similarity_cutoff: Optional[float]
    """Minimum similarity score wrt query for retrieval"""

    dense_similarity_top_k: Optional[int]
    """Number of nodes for dense retrieval."""

    enable_reranking: Optional[bool]
    """Enable reranking for retrieval"""

    files_top_k: Optional[int]
    """
    Number of files to retrieve (only for retrieval mode files_via_metadata and
    files_via_content).
    """

    rerank_top_n: Optional[int]
    """Number of reranked nodes for returning."""

    retrieval_mode: RetrievalMode
    """The retrieval mode for the query."""

    retrieve_image_nodes: bool
    """Whether to retrieve image nodes."""

    retrieve_page_figure_nodes: bool
    """Whether to retrieve page figure nodes."""

    retrieve_page_screenshot_nodes: bool
    """Whether to retrieve page screenshot nodes."""

    search_filters: Optional["MetadataFiltersParam"]
    """Metadata filters for vector stores."""

    search_filters_inference_schema: Optional[
        Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]
    ]
    """JSON Schema that will be used to infer search_filters.

    Omit or leave as null to skip inference.
    """

    sparse_similarity_top_k: Optional[int]
    """Number of nodes for sparse retrieval."""


from .metadata_filters_param import MetadataFiltersParam
