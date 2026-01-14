# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._polling import (
    BackoffStrategy,
    poll_until_complete,
    poll_until_complete_async,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.extraction import (
    job_file_params,
    job_list_params,
    job_create_params,
    job_get_result_params,
)
from ...types.extraction.extract_job import ExtractJob
from ...types.extraction.job_list_response import JobListResponse
from ...types.extraction.extract_config_param import ExtractConfigParam
from ...types.extraction.job_get_result_response import JobGetResultResponse
from ...types.extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
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

          config_override: Configuration parameters for the extraction agent.

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

    def get(
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

    def get_result(
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
    ) -> JobGetResultResponse:
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
                    job_get_result_params.JobGetResultParams,
                ),
            ),
            cast_to=JobGetResultResponse,
        )

    def extract(
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
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultResponse:
        """
        Create an extraction job and wait for it to complete, returning the result.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_result() into a single call for the most common end-to-end workflow.

        Args:
            extraction_agent_id: The id of the extraction agent

            file_id: The id of the file

            from_ui: Whether the request is from the UI

            config_override: Additional parameters for the extraction agent.

            data_schema_override: The data schema to override the extraction agent's data schema with

            priority: The priority for the request. This field may be ignored or overwritten depending
                on the organization tier.

            webhook_configurations: The outbound webhook configurations

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The extraction result (JobGetResultResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get result
            result = client.extraction.jobs.extract(extraction_agent_id="agent_id", file_id="file_id", verbose=True)

            # Result is ready to use immediately
            print(result.data)
            ```
        """
        # Create the job
        job = self.create(
            extraction_agent_id=extraction_agent_id,
            file_id=file_id,
            from_ui=from_ui,
            config_override=config_override,
            data_schema_override=data_schema_override,
            priority=priority,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        self.wait_for_completion(
            job.id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the result
        return self.get_result(
            job.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    def wait_for_completion(
        self,
        job_id: str,
        *,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExtractJob:
        """
        Wait for an extraction job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            job_id: The ID of the extraction job to wait for

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ExtractJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create an extraction job
            job = client.extraction.jobs.create(extraction_agent_id="agent_id", file_id="file_id")

            # Wait for it to complete
            completed_job = client.extraction.jobs.wait_for_completion(job.id, verbose=True)

            # Get the result
            result = client.extraction.jobs.get_result(job.id)
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        def get_status() -> ExtractJob:
            return self.get(
                job_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ExtractJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ExtractJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ExtractJob) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
            if job.error:
                error_parts.append(f"Error: {job.error}")
            return " | ".join(error_parts)

        return poll_until_complete(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
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

          config_override: Configuration parameters for the extraction agent.

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

    async def get(
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

    async def get_result(
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
    ) -> JobGetResultResponse:
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
                    job_get_result_params.JobGetResultParams,
                ),
            ),
            cast_to=JobGetResultResponse,
        )

    async def extract(
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
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultResponse:
        """
        Create an extraction job and wait for it to complete, returning the result.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_result() into a single call for the most common end-to-end workflow.

        Args:
            extraction_agent_id: The id of the extraction agent

            file_id: The id of the file

            from_ui: Whether the request is from the UI

            config_override: Additional parameters for the extraction agent.

            data_schema_override: The data schema to override the extraction agent's data schema with

            priority: The priority for the request. This field may be ignored or overwritten depending
                on the organization tier.

            webhook_configurations: The outbound webhook configurations

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The extraction result (JobGetResultResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get result
            result = await client.extraction.jobs.extract(
                extraction_agent_id="agent_id", file_id="file_id", verbose=True
            )

            # Result is ready to use immediately
            print(result.data)
            ```
        """
        # Create the job
        job = await self.create(
            extraction_agent_id=extraction_agent_id,
            file_id=file_id,
            from_ui=from_ui,
            config_override=config_override,
            data_schema_override=data_schema_override,
            priority=priority,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        await self.wait_for_completion(
            job.id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the result
        return await self.get_result(
            job.id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    async def wait_for_completion(
        self,
        job_id: str,
        *,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExtractJob:
        """
        Wait for an extraction job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            job_id: The ID of the extraction job to wait for

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ExtractJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create an extraction job
            job = await client.extraction.jobs.create(extraction_agent_id="agent_id", file_id="file_id")

            # Wait for it to complete
            completed_job = await client.extraction.jobs.wait_for_completion(job.id, verbose=True)

            # Get the result
            result = await client.extraction.jobs.get_result(job.id)
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        async def get_status() -> ExtractJob:
            return await self.get(
                job_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ExtractJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ExtractJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ExtractJob) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
            if job.error:
                error_parts.append(f"Error: {job.error}")
            return " | ".join(error_parts)

        return await poll_until_complete_async(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.file = to_raw_response_wrapper(
            jobs.file,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )
        self.get_result = to_raw_response_wrapper(
            jobs.get_result,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.file = async_to_raw_response_wrapper(
            jobs.file,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )
        self.get_result = async_to_raw_response_wrapper(
            jobs.get_result,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.file = to_streamed_response_wrapper(
            jobs.file,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_result = to_streamed_response_wrapper(
            jobs.get_result,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.file = async_to_streamed_response_wrapper(
            jobs.file,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_result = async_to_streamed_response_wrapper(
            jobs.get_result,
        )
