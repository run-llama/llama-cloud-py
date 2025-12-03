from __future__ import annotations

from typing import Any, List, Optional
from typing_extensions import override

import httpx
from llama_index.core.schema import TextNode, QueryBundle, NodeWithScore
from llama_index.core.constants import DEFAULT_PROJECT_NAME
from llama_index.core.base.base_retriever import BaseRetriever

from llama_cloud import LlamaCloud, AsyncLlamaCloud, omit
from llama_cloud.types import (
    Retriever,
    ReRankConfigParam,
    RetrieverPipeline,
    PresetRetrievalParams,
    CompositeRetrievalMode,
    RetrieverPipelineParam,
)
from llama_cloud.types.composite_retrieval_result import Node

from .base import LlamaCloudIndex
from .api_utils import (
    resolve_project,
    resolve_retriever,
    page_screenshot_nodes_to_node_with_score,
    apage_screenshot_nodes_to_node_with_score,
)


class LlamaCloudCompositeRetriever(BaseRetriever):
    def __init__(
        self,
        # retriever identifier
        name: Optional[str] = None,
        retriever_id: Optional[str] = None,
        # project identifier
        project_name: Optional[str] = DEFAULT_PROJECT_NAME,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        # creation options
        create_if_not_exists: bool = False,
        # connection params
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 60,
        httpx_client: Optional[httpx.Client] = None,
        async_httpx_client: Optional[httpx.AsyncClient] = None,
        # composite retrieval params
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfigParam] = None,
        persisted: Optional[bool] = True,
        **kwargs: Any,
    ) -> None:
        """Initialize the Composite Retriever."""
        # initialize clients
        self._client = LlamaCloud(api_key=api_key, base_url=base_url, http_client=httpx_client, timeout=timeout)
        self._aclient = AsyncLlamaCloud(
            api_key=api_key, base_url=base_url, http_client=async_httpx_client, timeout=timeout
        )

        self.project = resolve_project(self._client, project_name, project_id, organization_id)

        self.name = name
        self.project_name = self.project.name
        self._persisted = persisted

        retriever = resolve_retriever(self._client, self.project, name, retriever_id, persisted)

        if retriever is None and persisted and self.name is not None:
            if create_if_not_exists:
                retriever = self._client.retrievers.upsert(
                    project_id=self.project.id,
                    name=self.name,
                    pipelines=[],
                )
            else:
                raise ValueError(f"Retriever with name '{self.name}' does not exist in project.")

        if retriever is None:
            raise ValueError("Failed to resolve retriever")
        self.retriever = retriever

        # composite retrieval params
        self._mode = mode if mode is not None else omit
        self._rerank_top_n = rerank_top_n if rerank_top_n is not None else omit
        self._rerank_config = rerank_config if rerank_config is not None else omit

        super().__init__(  # type: ignore
            callback_manager=kwargs.get("callback_manager"),
            verbose=kwargs.get("verbose", False),
        )

    @property
    def retriever_pipelines(self) -> List[RetrieverPipeline]:
        return self.retriever.pipelines or []

    def update_retriever_pipelines(self, pipelines: List[RetrieverPipeline]) -> Retriever:
        if self._persisted:
            self.retriever = self._client.retrievers.update(
                retriever_id=self.retriever.id,
                pipelines=[RetrieverPipelineParam(**pipeline.model_dump()) for pipeline in pipelines],  # type: ignore [typeddict-item]
            )
        else:
            # Update in-memory retriever for non-persisted case using copy
            self.retriever = self.retriever.model_copy(update={"pipelines": pipelines})

        return self.retriever

    def add_index(
        self,
        index: LlamaCloudIndex,
        name: Optional[str] = None,
        description: Optional[str] = None,
        preset_retrieval_parameters: Optional[PresetRetrievalParams] = None,
    ) -> Retriever:
        name = name or index.name
        preset_retrieval_parameters = preset_retrieval_parameters or index.pipeline.preset_retrieval_parameters
        retriever_pipeline = RetrieverPipeline(
            pipeline_id=index.id,
            name=name,
            description=description,
            preset_retrieval_parameters=preset_retrieval_parameters,
        )
        current_retriever_pipelines_by_name = {pipeline.name: pipeline for pipeline in (self.retriever_pipelines or [])}
        current_retriever_pipelines_by_name[retriever_pipeline.name] = retriever_pipeline
        return self.update_retriever_pipelines(list(current_retriever_pipelines_by_name.values()))

    def remove_index(self, name: str) -> bool:
        current_retriever_pipeline_names = self.retriever.pipelines or []  # type: ignore [union-attr]
        new_retriever_pipelines = [pipeline for pipeline in current_retriever_pipeline_names if pipeline.name != name]
        if len(new_retriever_pipelines) == len(current_retriever_pipeline_names):
            return False
        self.update_retriever_pipelines(new_retriever_pipelines)
        return True

    async def aupdate_retriever_pipelines(self, pipelines: List[RetrieverPipeline]) -> Retriever:
        if self._persisted:
            self.retriever = await self._aclient.retrievers.update(
                retriever_id=self.retriever.id,
                pipelines=pipelines,  # type: ignore [arg-type]
            )
        else:
            # Update in-memory retriever for non-persisted case using copy
            self.retriever = self.retriever.copy(update={"pipelines": pipelines})  # type: ignore [union-attr]
        return self.retriever

    async def async_add_index(
        self,
        index: LlamaCloudIndex,
        name: Optional[str] = None,
        description: Optional[str] = None,
        preset_retrieval_parameters: Optional[PresetRetrievalParams] = None,
    ) -> Retriever:
        name = name or index.name
        preset_retrieval_parameters = preset_retrieval_parameters or index.pipeline.preset_retrieval_parameters
        retriever_pipeline = RetrieverPipeline(
            pipeline_id=index.id,
            name=name,
            description=description,
            preset_retrieval_parameters=preset_retrieval_parameters,
        )
        current_retriever_pipelines_by_name = {pipeline.name: pipeline for pipeline in (self.retriever_pipelines or [])}
        current_retriever_pipelines_by_name[retriever_pipeline.name] = retriever_pipeline
        return await self.aupdate_retriever_pipelines(list(current_retriever_pipelines_by_name.values()))

    async def aremove_index(self, name: str) -> bool:
        current_retriever_pipeline_names = self.retriever.pipelines or []  # type: ignore [union-attr]
        new_retriever_pipelines = [pipeline for pipeline in current_retriever_pipeline_names if pipeline.name != name]
        if len(new_retriever_pipelines) == len(current_retriever_pipeline_names):
            return False
        await self.aupdate_retriever_pipelines(new_retriever_pipelines)
        return True

    def _result_nodes_to_node_with_score(self, composite_retrieval_node: Node) -> NodeWithScore:
        return NodeWithScore(
            node=TextNode(
                id=composite_retrieval_node.node.id,
                text=composite_retrieval_node.node.text,
                metadata=composite_retrieval_node.node.metadata,
            ),
            score=composite_retrieval_node.score,
        )

    @override
    def _retrieve(
        self,
        query_bundle: QueryBundle,
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfigParam] = None,
    ) -> List[NodeWithScore]:
        mode = mode if mode is not None else self._mode  # type: ignore

        rerank_top_n = rerank_top_n if rerank_top_n is not None else self._rerank_top_n  # type: ignore
        rerank_config = (
            rerank_config if rerank_config is not None else self._rerank_config  # type: ignore
        )

        # Inject rerank_top_n into rerank_config if specified
        if rerank_top_n is not None:
            if rerank_config is None:
                rerank_config = ReRankConfigParam(top_n=rerank_top_n)
            else:
                # Update existing rerank_config with top_n
                rerank_config = ReRankConfigParam(top_n=rerank_top_n, type=rerank_config.get("type", "system_default"))

        if self._persisted:
            result = self._client.retrievers.retriever.search(
                retriever_id=self.retriever.id,
                mode=mode,  # type: ignore
                rerank_config=rerank_config,  # type: ignore
                query=query_bundle.query_str,
            )
        else:
            result = self._client.retrievers.search(
                project_id=self.project.id,
                mode=mode,  # type: ignore
                rerank_config=rerank_config,  # type: ignore
                query=query_bundle.query_str,
                pipelines=self.retriever.pipelines,  # type: ignore
            )
        node_w_scores = [self._result_nodes_to_node_with_score(node) for node in (result.nodes or [])]
        image_nodes_w_scores = page_screenshot_nodes_to_node_with_score(
            self._client, result.image_nodes, self.retriever.project_id
        )
        return sorted(node_w_scores + image_nodes_w_scores, key=lambda x: x.score or 1.0, reverse=True)

    @override
    async def _aretrieve(
        self,
        query_bundle: QueryBundle,
        mode: Optional[CompositeRetrievalMode] = None,
        rerank_top_n: Optional[int] = None,
        rerank_config: Optional[ReRankConfigParam] = None,
    ) -> List[NodeWithScore]:
        mode = mode if mode is not None else self._mode  # type: ignore

        rerank_top_n = rerank_top_n if rerank_top_n is not None else self._rerank_top_n  # type: ignore
        rerank_config = (
            rerank_config if rerank_config is not None else self._rerank_config  # type: ignore
        )

        # Inject rerank_top_n into rerank_config if specified
        if rerank_top_n is not None:
            if rerank_config is None:
                rerank_config = ReRankConfigParam(top_n=rerank_top_n)
            else:
                # Update existing rerank_config with top_n
                rerank_config = ReRankConfigParam(top_n=rerank_top_n, type=rerank_config.get("type", "system_default"))

        if self._persisted:
            result = await self._aclient.retrievers.retriever.search(
                retriever_id=self.retriever.id,
                mode=mode,  # type: ignore
                rerank_config=rerank_config,  # type: ignore
                query=query_bundle.query_str,
            )
        else:
            result = await self._aclient.retrievers.search(
                project_id=self.project.id,
                mode=mode,  # type: ignore
                rerank_config=rerank_config,  # type: ignore
                query=query_bundle.query_str,
                pipelines=self.retriever.pipelines,  # type: ignore [arg-type]
            )
        node_w_scores = [self._result_nodes_to_node_with_score(node) for node in result.nodes or []]
        image_nodes_w_scores = await apage_screenshot_nodes_to_node_with_score(
            self._aclient, result.image_nodes, self.retriever.project_id
        )
        return sorted(node_w_scores + image_nodes_w_scores, key=lambda x: x.score or 1.0, reverse=True)
