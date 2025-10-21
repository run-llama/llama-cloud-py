# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.extraction import (
    job_file_params,
    job_list_params,
    job_batch_params,
    job_create_params,
    job_retrieve_result_params,
)
from ....types.v1.extraction.extract_job import ExtractJob
from ....types.v1.extraction.job_list_response import JobListResponse
from ....types.v1.extraction.job_batch_response import JobBatchResponse
from ....types.v1.extraction.extract_config_param import ExtractConfigParam
from ....types.v1.extraction.webhook_configuration_param import WebhookConfigurationParam
from ....types.v1.extraction.job_retrieve_result_response import JobRetrieveResultResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        extraction_agent_id: str,
        file_id: str,
        from_ui: bool | Omit = omit,
        config_override: Optional[ExtractConfigParam] | Omit = omit,
        data_schema_override: Union[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None
        ]
        | Omit = omit,
        priority: Optional[Literal["low", "medium", "high", "critical"]] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Run Job

        Args:
          extraction_agent_id: The id of the extraction agent

          file_id: The id of the file

          config_override: Additional parameters for the extraction agent.

          data_schema_override: The data schema to override the extraction agent's data schema with

          priority: The priority for the request. This field may be ignored or overwritten depending
              on the organization tier.

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/jobs",
            body=maybe_transform(
                {
                    "extraction_agent_id": extraction_agent_id,
                    "file_id": file_id,
                    "config_override": config_override,
                    "data_schema_override": data_schema_override,
                    "priority": priority,
                    "webhook_configurations": webhook_configurations,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_ui": from_ui}, job_create_params.JobCreateParams),
            ),
            cast_to=ExtractJob,
        )

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Get Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/extraction/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractJob,
        )

    def list(
        self,
        *,
        extraction_agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        List Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/extraction/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"extraction_agent_id": extraction_agent_id}, job_list_params.JobListParams),
            ),
            cast_to=JobListResponse,
        )

    def batch(
        self,
        *,
        extraction_agent_id: str,
        file_ids: SequenceNotStr[str],
        from_ui: bool | Omit = omit,
        config_override: Optional[ExtractConfigParam] | Omit = omit,
        data_schema_override: Union[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobBatchResponse:
        """
        Run Batch Jobs

        Args:
          extraction_agent_id: The id of the extraction agent

          file_ids: The ids of the files

          config_override: Additional parameters for the extraction agent.

          data_schema_override: The data schema to override the extraction agent's data schema with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/jobs/batch",
            body=maybe_transform(
                {
                    "extraction_agent_id": extraction_agent_id,
                    "file_ids": file_ids,
                    "config_override": config_override,
                    "data_schema_override": data_schema_override,
                },
                job_batch_params.JobBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_ui": from_ui}, job_batch_params.JobBatchParams),
            ),
            cast_to=JobBatchResponse,
        )

    def file(
        self,
        *,
        extraction_agent_id: str,
        file: FileTypes,
        from_ui: bool | Omit = omit,
        config_override: Optional[str] | Omit = omit,
        data_schema_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Run Job On File

        Args:
          extraction_agent_id: The id of the extraction agent

          file: The file to run the job on

          config_override: The config to override the extraction agent's config with as a JSON string

          data_schema_override: The data schema to override the extraction agent's data schema with as a JSON
              string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "extraction_agent_id": extraction_agent_id,
                "file": file,
                "config_override": config_override,
                "data_schema_override": data_schema_override,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/extraction/jobs/file",
            body=maybe_transform(body, job_file_params.JobFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_ui": from_ui}, job_file_params.JobFileParams),
            ),
            cast_to=ExtractJob,
        )

    def retrieve_result(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResultResponse:
        """
        Get Job Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/extraction/jobs/{job_id}/result",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    job_retrieve_result_params.JobRetrieveResultParams,
                ),
            ),
            cast_to=JobRetrieveResultResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        extraction_agent_id: str,
        file_id: str,
        from_ui: bool | Omit = omit,
        config_override: Optional[ExtractConfigParam] | Omit = omit,
        data_schema_override: Union[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None
        ]
        | Omit = omit,
        priority: Optional[Literal["low", "medium", "high", "critical"]] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Run Job

        Args:
          extraction_agent_id: The id of the extraction agent

          file_id: The id of the file

          config_override: Additional parameters for the extraction agent.

          data_schema_override: The data schema to override the extraction agent's data schema with

          priority: The priority for the request. This field may be ignored or overwritten depending
              on the organization tier.

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/jobs",
            body=await async_maybe_transform(
                {
                    "extraction_agent_id": extraction_agent_id,
                    "file_id": file_id,
                    "config_override": config_override,
                    "data_schema_override": data_schema_override,
                    "priority": priority,
                    "webhook_configurations": webhook_configurations,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"from_ui": from_ui}, job_create_params.JobCreateParams),
            ),
            cast_to=ExtractJob,
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Get Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/extraction/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractJob,
        )

    async def list(
        self,
        *,
        extraction_agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        List Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/extraction/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"extraction_agent_id": extraction_agent_id}, job_list_params.JobListParams
                ),
            ),
            cast_to=JobListResponse,
        )

    async def batch(
        self,
        *,
        extraction_agent_id: str,
        file_ids: SequenceNotStr[str],
        from_ui: bool | Omit = omit,
        config_override: Optional[ExtractConfigParam] | Omit = omit,
        data_schema_override: Union[
            Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobBatchResponse:
        """
        Run Batch Jobs

        Args:
          extraction_agent_id: The id of the extraction agent

          file_ids: The ids of the files

          config_override: Additional parameters for the extraction agent.

          data_schema_override: The data schema to override the extraction agent's data schema with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/jobs/batch",
            body=await async_maybe_transform(
                {
                    "extraction_agent_id": extraction_agent_id,
                    "file_ids": file_ids,
                    "config_override": config_override,
                    "data_schema_override": data_schema_override,
                },
                job_batch_params.JobBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"from_ui": from_ui}, job_batch_params.JobBatchParams),
            ),
            cast_to=JobBatchResponse,
        )

    async def file(
        self,
        *,
        extraction_agent_id: str,
        file: FileTypes,
        from_ui: bool | Omit = omit,
        config_override: Optional[str] | Omit = omit,
        data_schema_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Run Job On File

        Args:
          extraction_agent_id: The id of the extraction agent

          file: The file to run the job on

          config_override: The config to override the extraction agent's config with as a JSON string

          data_schema_override: The data schema to override the extraction agent's data schema with as a JSON
              string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "extraction_agent_id": extraction_agent_id,
                "file": file,
                "config_override": config_override,
                "data_schema_override": data_schema_override,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/extraction/jobs/file",
            body=await async_maybe_transform(body, job_file_params.JobFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"from_ui": from_ui}, job_file_params.JobFileParams),
            ),
            cast_to=ExtractJob,
        )

    async def retrieve_result(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResultResponse:
        """
        Get Job Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/extraction/jobs/{job_id}/result",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    job_retrieve_result_params.JobRetrieveResultParams,
                ),
            ),
            cast_to=JobRetrieveResultResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.batch = to_raw_response_wrapper(
            jobs.batch,
        )
        self.file = to_raw_response_wrapper(
            jobs.file,
        )
        self.retrieve_result = to_raw_response_wrapper(
            jobs.retrieve_result,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.batch = async_to_raw_response_wrapper(
            jobs.batch,
        )
        self.file = async_to_raw_response_wrapper(
            jobs.file,
        )
        self.retrieve_result = async_to_raw_response_wrapper(
            jobs.retrieve_result,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.batch = to_streamed_response_wrapper(
            jobs.batch,
        )
        self.file = to_streamed_response_wrapper(
            jobs.file,
        )
        self.retrieve_result = to_streamed_response_wrapper(
            jobs.retrieve_result,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.batch = async_to_streamed_response_wrapper(
            jobs.batch,
        )
        self.file = async_to_streamed_response_wrapper(
            jobs.file,
        )
        self.retrieve_result = async_to_streamed_response_wrapper(
            jobs.retrieve_result,
        )
