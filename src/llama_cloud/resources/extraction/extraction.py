# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import extraction_run_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._polling import BackoffStrategy
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.extraction.extract_job import ExtractJob
from .extraction_agents.extraction_agents import (
    ExtractionAgentsResource,
    AsyncExtractionAgentsResource,
    ExtractionAgentsResourceWithRawResponse,
    AsyncExtractionAgentsResourceWithRawResponse,
    ExtractionAgentsResourceWithStreamingResponse,
    AsyncExtractionAgentsResourceWithStreamingResponse,
)
from ...types.extraction.extract_config_param import ExtractConfigParam
from ...types.extraction.job_get_result_response import JobGetResultResponse
from ...types.extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["ExtractionResource", "AsyncExtractionResource"]


class ExtractionResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def extraction_agents(self) -> ExtractionAgentsResource:
        return ExtractionAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ExtractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ExtractionResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file: Optional[extraction_run_params.File] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Stateless extraction endpoint that uses a default extraction agent in the user's
        default project. Requires data_schema, config, and either file_id, text, or
        base64 encoded file data.

        Args:
          config: The configuration parameters for the extraction

          data_schema: The schema of the data to extract

          file: Schema for file data with base64 content and MIME type.

          file_id: The ID of the file to extract from

          text: The text content to extract from

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/run",
            body=maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                    "file": file,
                    "file_id": file_id,
                    "text": text,
                    "webhook_configurations": webhook_configurations,
                },
                extraction_run_params.ExtractionRunParams,
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
                    extraction_run_params.ExtractionRunParams,
                ),
            ),
            cast_to=ExtractJob,
        )

    def extract(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file: Optional[extraction_run_params.File] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
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
        Run a stateless extraction and wait for it to complete, returning the result.

        This is a convenience method that combines run(), wait_for_completion(),
        and get_result() into a single call for the most common end-to-end workflow.

        This endpoint uses a default extraction agent in the user's default project.

        Args:
            config: The configuration parameters for the extraction

            data_schema: The schema of the data to extract

            organization_id: The organization ID to use for the extraction

            project_id: The project ID to use for the extraction

            file: Schema for file data with base64 content and MIME type.

            file_id: The ID of the file to extract from

            text: The text content to extract from

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

            # One-shot: run stateless extraction, wait for completion, and get result
            result = client.extraction.extract(
                config={"llm_model": "gpt-4"},
                data_schema={"name": "string", "age": "number"},
                file_id="file_id",
                verbose=True,
            )

            # Result is ready to use immediately
            print(result.data)
            ```
        """
        # Run the extraction job
        job = self.run(
            config=config,
            data_schema=data_schema,
            organization_id=organization_id,
            project_id=project_id,
            file=file,
            file_id=file_id,
            text=text,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        self.jobs.wait_for_completion(
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
        return self.jobs.get_result(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class AsyncExtractionResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def extraction_agents(self) -> AsyncExtractionAgentsResource:
        return AsyncExtractionAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncExtractionResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file: Optional[extraction_run_params.File] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractJob:
        """
        Stateless extraction endpoint that uses a default extraction agent in the user's
        default project. Requires data_schema, config, and either file_id, text, or
        base64 encoded file data.

        Args:
          config: The configuration parameters for the extraction

          data_schema: The schema of the data to extract

          file: Schema for file data with base64 content and MIME type.

          file_id: The ID of the file to extract from

          text: The text content to extract from

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/run",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                    "file": file,
                    "file_id": file_id,
                    "text": text,
                    "webhook_configurations": webhook_configurations,
                },
                extraction_run_params.ExtractionRunParams,
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
                    extraction_run_params.ExtractionRunParams,
                ),
            ),
            cast_to=ExtractJob,
        )

    async def extract(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file: Optional[extraction_run_params.File] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
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
        Run a stateless extraction and wait for it to complete, returning the result.

        This is a convenience method that combines run(), wait_for_completion(),
        and get_result() into a single call for the most common end-to-end workflow.

        This endpoint uses a default extraction agent in the user's default project.

        Args:
            config: The configuration parameters for the extraction

            data_schema: The schema of the data to extract

            organization_id: The organization ID to use for the extraction

            project_id: The project ID to use for the extraction

            file: Schema for file data with base64 content and MIME type.

            file_id: The ID of the file to extract from

            text: The text content to extract from

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

            # One-shot: run stateless extraction, wait for completion, and get result
            result = await client.extraction.extract(
                config={"llm_model": "gpt-4"},
                data_schema={"name": "string", "age": "number"},
                file_id="file_id",
                verbose=True,
            )

            # Result is ready to use immediately
            print(result.data)
            ```
        """
        # Run the extraction job
        job = await self.run(
            config=config,
            data_schema=data_schema,
            organization_id=organization_id,
            project_id=project_id,
            file=file,
            file_id=file_id,
            text=text,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        await self.jobs.wait_for_completion(
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
        return await self.jobs.get_result(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class ExtractionResourceWithRawResponse:
    def __init__(self, extraction: ExtractionResource) -> None:
        self._extraction = extraction

        self.run = to_raw_response_wrapper(
            extraction.run,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._extraction.jobs)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._extraction.runs)

    @cached_property
    def extraction_agents(self) -> ExtractionAgentsResourceWithRawResponse:
        return ExtractionAgentsResourceWithRawResponse(self._extraction.extraction_agents)


class AsyncExtractionResourceWithRawResponse:
    def __init__(self, extraction: AsyncExtractionResource) -> None:
        self._extraction = extraction

        self.run = async_to_raw_response_wrapper(
            extraction.run,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._extraction.jobs)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._extraction.runs)

    @cached_property
    def extraction_agents(self) -> AsyncExtractionAgentsResourceWithRawResponse:
        return AsyncExtractionAgentsResourceWithRawResponse(self._extraction.extraction_agents)


class ExtractionResourceWithStreamingResponse:
    def __init__(self, extraction: ExtractionResource) -> None:
        self._extraction = extraction

        self.run = to_streamed_response_wrapper(
            extraction.run,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._extraction.jobs)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._extraction.runs)

    @cached_property
    def extraction_agents(self) -> ExtractionAgentsResourceWithStreamingResponse:
        return ExtractionAgentsResourceWithStreamingResponse(self._extraction.extraction_agents)


class AsyncExtractionResourceWithStreamingResponse:
    def __init__(self, extraction: AsyncExtractionResource) -> None:
        self._extraction = extraction

        self.run = async_to_streamed_response_wrapper(
            extraction.run,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._extraction.jobs)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._extraction.runs)

    @cached_property
    def extraction_agents(self) -> AsyncExtractionAgentsResourceWithStreamingResponse:
        return AsyncExtractionAgentsResourceWithStreamingResponse(self._extraction.extraction_agents)
