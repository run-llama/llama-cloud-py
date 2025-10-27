# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import v1
from .. import _compat
from .delete_params import DeleteParams as DeleteParams
from .v1_get_jobs_params import V1GetJobsParams as V1GetJobsParams
from .v1_get_jobs_response import V1GetJobsResponse as V1GetJobsResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    v1.metadata_filters.MetadataFilters.update_forward_refs()  # type: ignore
    v1.pipeline.Pipeline.update_forward_refs()  # type: ignore
    v1.preset_retrieval_params.PresetRetrievalParams.update_forward_refs()  # type: ignore
    v1.pipeline_retrieve_playground_session_response.PipelineRetrievePlaygroundSessionResponse.update_forward_refs()  # type: ignore
    v1.retriever.Retriever.update_forward_refs()  # type: ignore
    v1.retriever_pipeline.RetrieverPipeline.update_forward_refs()  # type: ignore
else:
    v1.metadata_filters.MetadataFilters.model_rebuild(_parent_namespace_depth=0)
    v1.pipeline.Pipeline.model_rebuild(_parent_namespace_depth=0)
    v1.preset_retrieval_params.PresetRetrievalParams.model_rebuild(_parent_namespace_depth=0)
    v1.pipeline_retrieve_playground_session_response.PipelineRetrievePlaygroundSessionResponse.model_rebuild(
        _parent_namespace_depth=0
    )
    v1.retriever.Retriever.model_rebuild(_parent_namespace_depth=0)
    v1.retriever_pipeline.RetrieverPipeline.model_rebuild(_parent_namespace_depth=0)
