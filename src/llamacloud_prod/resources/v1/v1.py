# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from .evals import (
    EvalsResource,
    AsyncEvalsResource,
    EvalsResourceWithRawResponse,
    AsyncEvalsResourceWithRawResponse,
    EvalsResourceWithStreamingResponse,
    AsyncEvalsResourceWithStreamingResponse,
)
from ...types import v1_get_jobs_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from .projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .beta.beta import (
    BetaResource,
    AsyncBetaResource,
    BetaResourceWithRawResponse,
    AsyncBetaResourceWithRawResponse,
    BetaResourceWithStreamingResponse,
    AsyncBetaResourceWithStreamingResponse,
)
from .data_sinks import (
    DataSinksResource,
    AsyncDataSinksResource,
    DataSinksResourceWithRawResponse,
    AsyncDataSinksResourceWithRawResponse,
    DataSinksResourceWithStreamingResponse,
    AsyncDataSinksResourceWithStreamingResponse,
)
from .retrievers import (
    RetrieversResource,
    AsyncRetrieversResource,
    RetrieversResourceWithRawResponse,
    AsyncRetrieversResourceWithRawResponse,
    RetrieversResourceWithStreamingResponse,
    AsyncRetrieversResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .files.files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .data_sources import (
    DataSourcesResource,
    AsyncDataSourcesResource,
    DataSourcesResourceWithRawResponse,
    AsyncDataSourcesResourceWithRawResponse,
    DataSourcesResourceWithStreamingResponse,
    AsyncDataSourcesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from .parsing.parsing import (
    ParsingResource,
    AsyncParsingResource,
    ParsingResourceWithRawResponse,
    AsyncParsingResourceWithRawResponse,
    ParsingResourceWithStreamingResponse,
    AsyncParsingResourceWithStreamingResponse,
)
from .pipelines.pipelines import (
    PipelinesResource,
    AsyncPipelinesResource,
    PipelinesResourceWithRawResponse,
    AsyncPipelinesResourceWithRawResponse,
    PipelinesResourceWithStreamingResponse,
    AsyncPipelinesResourceWithStreamingResponse,
)
from .classifier.classifier import (
    ClassifierResource,
    AsyncClassifierResource,
    ClassifierResourceWithRawResponse,
    AsyncClassifierResourceWithRawResponse,
    ClassifierResourceWithStreamingResponse,
    AsyncClassifierResourceWithStreamingResponse,
)
from .extraction.extraction import (
    ExtractionResource,
    AsyncExtractionResource,
    ExtractionResourceWithRawResponse,
    AsyncExtractionResourceWithRawResponse,
    ExtractionResourceWithStreamingResponse,
    AsyncExtractionResourceWithStreamingResponse,
)
from .validate_integrations import (
    ValidateIntegrationsResource,
    AsyncValidateIntegrationsResource,
    ValidateIntegrationsResourceWithRawResponse,
    AsyncValidateIntegrationsResourceWithRawResponse,
    ValidateIntegrationsResourceWithStreamingResponse,
    AsyncValidateIntegrationsResourceWithStreamingResponse,
)
from .embedding_model_configs import (
    EmbeddingModelConfigsResource,
    AsyncEmbeddingModelConfigsResource,
    EmbeddingModelConfigsResourceWithRawResponse,
    AsyncEmbeddingModelConfigsResourceWithRawResponse,
    EmbeddingModelConfigsResourceWithStreamingResponse,
    AsyncEmbeddingModelConfigsResourceWithStreamingResponse,
)
from .organizations.organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ...types.v1_get_jobs_response import V1GetJobsResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def validate_integrations(self) -> ValidateIntegrationsResource:
        return ValidateIntegrationsResource(self._client)

    @cached_property
    def data_sinks(self) -> DataSinksResource:
        return DataSinksResource(self._client)

    @cached_property
    def data_sources(self) -> DataSourcesResource:
        return DataSourcesResource(self._client)

    @cached_property
    def embedding_model_configs(self) -> EmbeddingModelConfigsResource:
        return EmbeddingModelConfigsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def pipelines(self) -> PipelinesResource:
        return PipelinesResource(self._client)

    @cached_property
    def retrievers(self) -> RetrieversResource:
        return RetrieversResource(self._client)

    @cached_property
    def evals(self) -> EvalsResource:
        return EvalsResource(self._client)

    @cached_property
    def parsing(self) -> ParsingResource:
        return ParsingResource(self._client)

    @cached_property
    def classifier(self) -> ClassifierResource:
        return ClassifierResource(self._client)

    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def extraction(self) -> ExtractionResource:
        return ExtractionResource(self._client)

    @cached_property
    def beta(self) -> BetaResource:
        return BetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def get_jobs(
        self,
        *,
        job_name: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetJobsResponse:
        """
        Get jobs for a project.

        Note: The include_usage_metrics parameter is deprecated and will be removed in a
        future version. We've moved to usage v2 and this parameter will no longer return
        meaningful data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_name": job_name,
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "sort": sort,
                    },
                    v1_get_jobs_params.V1GetJobsParams,
                ),
            ),
            cast_to=V1GetJobsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def validate_integrations(self) -> AsyncValidateIntegrationsResource:
        return AsyncValidateIntegrationsResource(self._client)

    @cached_property
    def data_sinks(self) -> AsyncDataSinksResource:
        return AsyncDataSinksResource(self._client)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResource:
        return AsyncDataSourcesResource(self._client)

    @cached_property
    def embedding_model_configs(self) -> AsyncEmbeddingModelConfigsResource:
        return AsyncEmbeddingModelConfigsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResource:
        return AsyncPipelinesResource(self._client)

    @cached_property
    def retrievers(self) -> AsyncRetrieversResource:
        return AsyncRetrieversResource(self._client)

    @cached_property
    def evals(self) -> AsyncEvalsResource:
        return AsyncEvalsResource(self._client)

    @cached_property
    def parsing(self) -> AsyncParsingResource:
        return AsyncParsingResource(self._client)

    @cached_property
    def classifier(self) -> AsyncClassifierResource:
        return AsyncClassifierResource(self._client)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def extraction(self) -> AsyncExtractionResource:
        return AsyncExtractionResource(self._client)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        return AsyncBetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def get_jobs(
        self,
        *,
        job_name: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetJobsResponse:
        """
        Get jobs for a project.

        Note: The include_usage_metrics parameter is deprecated and will be removed in a
        future version. We've moved to usage v2 and this parameter will no longer return
        meaningful data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "job_name": job_name,
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "sort": sort,
                    },
                    v1_get_jobs_params.V1GetJobsParams,
                ),
            ),
            cast_to=V1GetJobsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_jobs = to_raw_response_wrapper(
            v1.get_jobs,
        )

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._v1.projects)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._v1.api_keys)

    @cached_property
    def validate_integrations(self) -> ValidateIntegrationsResourceWithRawResponse:
        return ValidateIntegrationsResourceWithRawResponse(self._v1.validate_integrations)

    @cached_property
    def data_sinks(self) -> DataSinksResourceWithRawResponse:
        return DataSinksResourceWithRawResponse(self._v1.data_sinks)

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithRawResponse:
        return DataSourcesResourceWithRawResponse(self._v1.data_sources)

    @cached_property
    def embedding_model_configs(self) -> EmbeddingModelConfigsResourceWithRawResponse:
        return EmbeddingModelConfigsResourceWithRawResponse(self._v1.embedding_model_configs)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._v1.organizations)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._v1.files)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithRawResponse:
        return PipelinesResourceWithRawResponse(self._v1.pipelines)

    @cached_property
    def retrievers(self) -> RetrieversResourceWithRawResponse:
        return RetrieversResourceWithRawResponse(self._v1.retrievers)

    @cached_property
    def evals(self) -> EvalsResourceWithRawResponse:
        return EvalsResourceWithRawResponse(self._v1.evals)

    @cached_property
    def parsing(self) -> ParsingResourceWithRawResponse:
        return ParsingResourceWithRawResponse(self._v1.parsing)

    @cached_property
    def classifier(self) -> ClassifierResourceWithRawResponse:
        return ClassifierResourceWithRawResponse(self._v1.classifier)

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._v1.auth)

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._v1.billing)

    @cached_property
    def extraction(self) -> ExtractionResourceWithRawResponse:
        return ExtractionResourceWithRawResponse(self._v1.extraction)

    @cached_property
    def beta(self) -> BetaResourceWithRawResponse:
        return BetaResourceWithRawResponse(self._v1.beta)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_jobs = async_to_raw_response_wrapper(
            v1.get_jobs,
        )

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._v1.projects)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._v1.api_keys)

    @cached_property
    def validate_integrations(self) -> AsyncValidateIntegrationsResourceWithRawResponse:
        return AsyncValidateIntegrationsResourceWithRawResponse(self._v1.validate_integrations)

    @cached_property
    def data_sinks(self) -> AsyncDataSinksResourceWithRawResponse:
        return AsyncDataSinksResourceWithRawResponse(self._v1.data_sinks)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithRawResponse:
        return AsyncDataSourcesResourceWithRawResponse(self._v1.data_sources)

    @cached_property
    def embedding_model_configs(self) -> AsyncEmbeddingModelConfigsResourceWithRawResponse:
        return AsyncEmbeddingModelConfigsResourceWithRawResponse(self._v1.embedding_model_configs)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._v1.organizations)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._v1.files)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithRawResponse:
        return AsyncPipelinesResourceWithRawResponse(self._v1.pipelines)

    @cached_property
    def retrievers(self) -> AsyncRetrieversResourceWithRawResponse:
        return AsyncRetrieversResourceWithRawResponse(self._v1.retrievers)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithRawResponse:
        return AsyncEvalsResourceWithRawResponse(self._v1.evals)

    @cached_property
    def parsing(self) -> AsyncParsingResourceWithRawResponse:
        return AsyncParsingResourceWithRawResponse(self._v1.parsing)

    @cached_property
    def classifier(self) -> AsyncClassifierResourceWithRawResponse:
        return AsyncClassifierResourceWithRawResponse(self._v1.classifier)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._v1.auth)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._v1.billing)

    @cached_property
    def extraction(self) -> AsyncExtractionResourceWithRawResponse:
        return AsyncExtractionResourceWithRawResponse(self._v1.extraction)

    @cached_property
    def beta(self) -> AsyncBetaResourceWithRawResponse:
        return AsyncBetaResourceWithRawResponse(self._v1.beta)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_jobs = to_streamed_response_wrapper(
            v1.get_jobs,
        )

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._v1.projects)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._v1.api_keys)

    @cached_property
    def validate_integrations(self) -> ValidateIntegrationsResourceWithStreamingResponse:
        return ValidateIntegrationsResourceWithStreamingResponse(self._v1.validate_integrations)

    @cached_property
    def data_sinks(self) -> DataSinksResourceWithStreamingResponse:
        return DataSinksResourceWithStreamingResponse(self._v1.data_sinks)

    @cached_property
    def data_sources(self) -> DataSourcesResourceWithStreamingResponse:
        return DataSourcesResourceWithStreamingResponse(self._v1.data_sources)

    @cached_property
    def embedding_model_configs(self) -> EmbeddingModelConfigsResourceWithStreamingResponse:
        return EmbeddingModelConfigsResourceWithStreamingResponse(self._v1.embedding_model_configs)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._v1.organizations)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._v1.files)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithStreamingResponse:
        return PipelinesResourceWithStreamingResponse(self._v1.pipelines)

    @cached_property
    def retrievers(self) -> RetrieversResourceWithStreamingResponse:
        return RetrieversResourceWithStreamingResponse(self._v1.retrievers)

    @cached_property
    def evals(self) -> EvalsResourceWithStreamingResponse:
        return EvalsResourceWithStreamingResponse(self._v1.evals)

    @cached_property
    def parsing(self) -> ParsingResourceWithStreamingResponse:
        return ParsingResourceWithStreamingResponse(self._v1.parsing)

    @cached_property
    def classifier(self) -> ClassifierResourceWithStreamingResponse:
        return ClassifierResourceWithStreamingResponse(self._v1.classifier)

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._v1.auth)

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._v1.billing)

    @cached_property
    def extraction(self) -> ExtractionResourceWithStreamingResponse:
        return ExtractionResourceWithStreamingResponse(self._v1.extraction)

    @cached_property
    def beta(self) -> BetaResourceWithStreamingResponse:
        return BetaResourceWithStreamingResponse(self._v1.beta)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_jobs = async_to_streamed_response_wrapper(
            v1.get_jobs,
        )

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._v1.projects)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._v1.api_keys)

    @cached_property
    def validate_integrations(self) -> AsyncValidateIntegrationsResourceWithStreamingResponse:
        return AsyncValidateIntegrationsResourceWithStreamingResponse(self._v1.validate_integrations)

    @cached_property
    def data_sinks(self) -> AsyncDataSinksResourceWithStreamingResponse:
        return AsyncDataSinksResourceWithStreamingResponse(self._v1.data_sinks)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        return AsyncDataSourcesResourceWithStreamingResponse(self._v1.data_sources)

    @cached_property
    def embedding_model_configs(self) -> AsyncEmbeddingModelConfigsResourceWithStreamingResponse:
        return AsyncEmbeddingModelConfigsResourceWithStreamingResponse(self._v1.embedding_model_configs)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._v1.organizations)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._v1.files)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithStreamingResponse:
        return AsyncPipelinesResourceWithStreamingResponse(self._v1.pipelines)

    @cached_property
    def retrievers(self) -> AsyncRetrieversResourceWithStreamingResponse:
        return AsyncRetrieversResourceWithStreamingResponse(self._v1.retrievers)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithStreamingResponse:
        return AsyncEvalsResourceWithStreamingResponse(self._v1.evals)

    @cached_property
    def parsing(self) -> AsyncParsingResourceWithStreamingResponse:
        return AsyncParsingResourceWithStreamingResponse(self._v1.parsing)

    @cached_property
    def classifier(self) -> AsyncClassifierResourceWithStreamingResponse:
        return AsyncClassifierResourceWithStreamingResponse(self._v1.classifier)

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._v1.auth)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._v1.billing)

    @cached_property
    def extraction(self) -> AsyncExtractionResourceWithStreamingResponse:
        return AsyncExtractionResourceWithStreamingResponse(self._v1.extraction)

    @cached_property
    def beta(self) -> AsyncBetaResourceWithStreamingResponse:
        return AsyncBetaResourceWithStreamingResponse(self._v1.beta)
