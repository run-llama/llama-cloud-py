# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...pagination import SyncPaginatedClassifyJobs, AsyncPaginatedClassifyJobs
from ..._base_client import AsyncPaginator, make_request_options
from ...types.classifier import (
    job_get_params,
    job_list_params,
    job_create_params,
    job_get_results_params,
)
from ...types.classifier.classify_job import ClassifyJob
from ...types.classifier.classifier_rule_param import ClassifierRuleParam
from ...types.classifier.job_get_results_response import JobGetResultsResponse
from ...types.classifier.classify_parsing_configuration_param import ClassifyParsingConfigurationParam

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
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Create a classify job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          file_ids: The IDs of the files to classify

          rules: The rules to classify the files

          parsing_configuration: The configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/classifier/jobs",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "rules": rules,
                    "parsing_configuration": parsing_configuration,
                },
                job_create_params.JobCreateParams,
            ),
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
                    job_create_params.JobCreateParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedClassifyJobs[ClassifyJob]:
        """List classify jobs.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/classifier/jobs",
            page=SyncPaginatedClassifyJobs[ClassifyJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=ClassifyJob,
        )

    def get(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Get a classify job.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return self._get(
            f"/api/v1/classifier/jobs/{classify_job_id}",
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
                    job_get_params.JobGetParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    def get_results(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResultsResponse:
        """Get the results of a classify job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return self._get(
            f"/api/v1/classifier/jobs/{classify_job_id}/results",
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
                    job_get_results_params.JobGetResultsParams,
                ),
            ),
            cast_to=JobGetResultsResponse,
        )

    def create_and_wait(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 300.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultsResponse:
        """
        Create a classify job and wait for it to complete, returning the results.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_results() into a single call for the most common end-to-end workflow.

        Args:
            file_ids: The IDs of the files to classify

            rules: The rules to classify the files

            organization_id: Optional organization ID

            project_id: Optional project ID

            parsing_configuration: The configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The classification results (JobGetResultsResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            results = client.classifier.jobs.create_and_wait(
                file_ids=["file1", "file2", "file3"],
                rules=[
                    {"name": "invoice", "description": "Invoice documents"},
                    {"name": "receipt", "description": "Receipt documents"},
                ],
                verbose=True,
            )

            # Results are ready to use immediately
            for file_result in results.files:
                print(f"File {file_result.file_id}: {file_result.classification}")
            ```
        """
        # Create the job
        job = self.create(
            file_ids=file_ids,
            rules=rules,
            organization_id=organization_id,
            project_id=project_id,
            parsing_configuration=parsing_configuration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the results
        return self.get_results(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    def wait_for_completion(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 300.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ClassifyJob:
        """
        Wait for a classify job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            classify_job_id: The ID of the classify job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ClassifyJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a classify job
            job = client.classifier.jobs.create(file_ids=["file1", "file2"], rules=[...])

            # Wait for it to complete
            completed_job = client.classifier.jobs.wait_for_completion(job.id, verbose=True)

            # Get the results
            results = client.classifier.jobs.get_results(job.id)
            ```
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")

        def get_status() -> ClassifyJob:
            return self.get(
                classify_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ClassifyJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ClassifyJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ClassifyJob) -> str:
            error_parts = [f"Job {classify_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
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
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Create a classify job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          file_ids: The IDs of the files to classify

          rules: The rules to classify the files

          parsing_configuration: The configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/classifier/jobs",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "rules": rules,
                    "parsing_configuration": parsing_configuration,
                },
                job_create_params.JobCreateParams,
            ),
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
                    job_create_params.JobCreateParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ClassifyJob, AsyncPaginatedClassifyJobs[ClassifyJob]]:
        """List classify jobs.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/classifier/jobs",
            page=AsyncPaginatedClassifyJobs[ClassifyJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=ClassifyJob,
        )

    async def get(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Get a classify job.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return await self._get(
            f"/api/v1/classifier/jobs/{classify_job_id}",
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
                    job_get_params.JobGetParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    async def get_results(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResultsResponse:
        """Get the results of a classify job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return await self._get(
            f"/api/v1/classifier/jobs/{classify_job_id}/results",
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
                    job_get_results_params.JobGetResultsParams,
                ),
            ),
            cast_to=JobGetResultsResponse,
        )

    async def create_and_wait(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 300.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultsResponse:
        """
        Create a classify job and wait for it to complete, returning the results.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_results() into a single call for the most common end-to-end workflow.

        Args:
            file_ids: The IDs of the files to classify

            rules: The rules to classify the files

            organization_id: Optional organization ID

            project_id: Optional project ID

            parsing_configuration: The configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The classification results (JobGetResultsResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            results = await client.classifier.jobs.create_and_wait(
                file_ids=["file1", "file2", "file3"],
                rules=[
                    {"name": "invoice", "description": "Invoice documents"},
                    {"name": "receipt", "description": "Receipt documents"},
                ],
                verbose=True,
            )

            # Results are ready to use immediately
            for file_result in results.files:
                print(f"File {file_result.file_id}: {file_result.classification}")
            ```
        """
        # Create the job
        job = await self.create(
            file_ids=file_ids,
            rules=rules,
            organization_id=organization_id,
            project_id=project_id,
            parsing_configuration=parsing_configuration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        await self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the results
        return await self.get_results(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    async def wait_for_completion(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 300.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ClassifyJob:
        """
        Wait for a classify job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            classify_job_id: The ID of the classify job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ClassifyJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a classify job
            job = await client.classifier.jobs.create(file_ids=["file1", "file2"], rules=[...])

            # Wait for it to complete
            completed_job = await client.classifier.jobs.wait_for_completion(job.id, verbose=True)

            # Get the results
            results = await client.classifier.jobs.get_results(job.id)
            ```
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")

        async def get_status() -> ClassifyJob:
            return await self.get(
                classify_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ClassifyJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ClassifyJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ClassifyJob) -> str:
            error_parts = [f"Job {classify_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
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
        self.get = to_raw_response_wrapper(
            jobs.get,
        )
        self.get_results = to_raw_response_wrapper(
            jobs.get_results,
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
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )
        self.get_results = async_to_raw_response_wrapper(
            jobs.get_results,
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
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_results = to_streamed_response_wrapper(
            jobs.get_results,
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
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
        self.get_results = async_to_streamed_response_wrapper(
            jobs.get_results,
        )
