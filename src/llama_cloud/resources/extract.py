# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    extract_get_params,
    extract_list_params,
    extract_create_params,
    extract_delete_params,
    extract_generate_schema_params,
    extract_validate_schema_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._polling import (
    DEFAULT_TIMEOUT,
    BackoffStrategy,
    poll_until_complete,
    poll_until_complete_async,
)
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.extract_v2_job import ExtractV2Job
from ..types.extract_configuration_param import ExtractConfigurationParam
from ..types.extract_generate_schema_response import ExtractGenerateSchemaResponse
from ..types.extract_v2_schema_validate_response import ExtractV2SchemaValidateResponse
from ..types.extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["url", "file_id", "parse_job_id"],
        value: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create a new extraction job.

        Provide exactly one of configuration_id (saved configuration) or inline config.

        Args:
          type: Type of document input.

          value: Document identifier (URL, file ID, or parse job ID).

          config: Extraction configuration combining parse and extract settings.

          configuration_id: Saved extract configuration ID (mutually exclusive with config)

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract",
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                    "config": config,
                    "configuration_id": configuration_id,
                    "webhook_configurations": webhook_configurations,
                },
                extract_create_params.ExtractCreateParams,
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
                    extract_create_params.ExtractCreateParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        document_input_type: Optional[str] | Omit = omit,
        document_input_value: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ExtractV2Job]:
        """
        List extraction jobs with optional filtering and pagination.

        Args:
          configuration_id: Filter by configuration ID

          document_input_type: Filter by document input type (file_id or parse_job_id)

          document_input_value: Filter by document input value

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/extract",
            page=SyncPaginatedCursor[ExtractV2Job],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "document_input_type": document_input_type,
                        "document_input_value": document_input_value,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    extract_list_params.ExtractListParams,
                ),
            ),
            model=ExtractV2Job,
        )

    def delete(
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
    ) -> object:
        """
        Delete an extraction job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_delete_params.ExtractDeleteParams,
                ),
            ),
            cast_to=object,
        )

    def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractGenerateSchemaResponse:
        """
        Generate a JSON schema and return a product configuration request.

        Args:
          data_schema: Optional schema to validate, refine, or extend

          file_id: Optional file ID to analyze for schema generation

          name: Name for the generated configuration (auto-generated if omitted)

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract/schema/generate",
            body=maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "name": name,
                    "prompt": prompt,
                },
                extract_generate_schema_params.ExtractGenerateSchemaParams,
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
                    extract_generate_schema_params.ExtractGenerateSchemaParams,
                ),
            ),
            cast_to=ExtractGenerateSchemaResponse,
        )

    def get(
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
    ) -> ExtractV2Job:
        """
        Get a single extraction job by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_get_params.ExtractGetParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def validate_schema(
        self,
        *,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2SchemaValidateResponse:
        """
        Validate a JSON schema for extraction.

        Args:
          data_schema: Schema to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract/schema/validation",
            body=maybe_transform(
                {"data_schema": data_schema}, extract_validate_schema_params.ExtractValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractV2SchemaValidateResponse,
        )

    def wait_for_completion(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExtractV2Job:
        """
        Wait for an extraction job to complete by polling until it reaches a terminal state.

        Args:
            job_id: The ID of the extraction job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2 hours)

            backoff: Backoff strategy: "constant", "linear" (default), or "exponential"

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed extraction job

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            job = client.extract.create(type="file_id", value="file-abc123")
            completed_job = client.extract.wait_for_completion(job.id, verbose=True)
            print(completed_job.extract_result)
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        def get_status() -> ExtractV2Job:
            return self.get(
                job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ExtractV2Job) -> bool:
            return job.status == "COMPLETED"

        def is_error(job: ExtractV2Job) -> bool:
            return job.status in ("FAILED", "CANCELLED")

        def get_error_message(job: ExtractV2Job) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
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

    def run(
        self,
        *,
        type: Literal["url", "file_id", "parse_job_id"],
        value: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        polling_timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create an extraction job, wait for it to complete, and return the result.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Args:
            type: Type of document input.

            value: Document identifier (URL, file ID, or parse job ID).

            config: Extraction configuration combining parse and extract settings.

            configuration_id: Saved extract configuration ID (mutually exclusive with config)

            webhook_configurations: The outbound webhook configurations

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            polling_timeout: Maximum time to wait in seconds (default: 2 hours)

            backoff: Backoff strategy: "constant", "linear" (default), or "exponential"

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The completed extraction job with extract_result populated

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create, wait, and get result
            result = client.extract.run(
                type="file_id",
                value="file-abc123",
                config={"extract_options": {"data_schema": {...}}},
                verbose=True,
            )
            print(result.extract_result)
            ```
        """
        job = self.create(
            type=type,
            value=value,
            organization_id=organization_id,
            project_id=project_id,
            config=config,
            configuration_id=configuration_id,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=polling_timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["url", "file_id", "parse_job_id"],
        value: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create a new extraction job.

        Provide exactly one of configuration_id (saved configuration) or inline config.

        Args:
          type: Type of document input.

          value: Document identifier (URL, file ID, or parse job ID).

          config: Extraction configuration combining parse and extract settings.

          configuration_id: Saved extract configuration ID (mutually exclusive with config)

          webhook_configurations: The outbound webhook configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                    "config": config,
                    "configuration_id": configuration_id,
                    "webhook_configurations": webhook_configurations,
                },
                extract_create_params.ExtractCreateParams,
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
                    extract_create_params.ExtractCreateParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        document_input_type: Optional[str] | Omit = omit,
        document_input_value: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "THROTTLED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExtractV2Job, AsyncPaginatedCursor[ExtractV2Job]]:
        """
        List extraction jobs with optional filtering and pagination.

        Args:
          configuration_id: Filter by configuration ID

          document_input_type: Filter by document input type (file_id or parse_job_id)

          document_input_value: Filter by document input value

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/extract",
            page=AsyncPaginatedCursor[ExtractV2Job],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "document_input_type": document_input_type,
                        "document_input_value": document_input_value,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    extract_list_params.ExtractListParams,
                ),
            ),
            model=ExtractV2Job,
        )

    async def delete(
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
    ) -> object:
        """
        Delete an extraction job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_delete_params.ExtractDeleteParams,
                ),
            ),
            cast_to=object,
        )

    async def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractGenerateSchemaResponse:
        """
        Generate a JSON schema and return a product configuration request.

        Args:
          data_schema: Optional schema to validate, refine, or extend

          file_id: Optional file ID to analyze for schema generation

          name: Name for the generated configuration (auto-generated if omitted)

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract/schema/generate",
            body=await async_maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "name": name,
                    "prompt": prompt,
                },
                extract_generate_schema_params.ExtractGenerateSchemaParams,
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
                    extract_generate_schema_params.ExtractGenerateSchemaParams,
                ),
            ),
            cast_to=ExtractGenerateSchemaResponse,
        )

    async def get(
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
    ) -> ExtractV2Job:
        """
        Get a single extraction job by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_get_params.ExtractGetParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    async def validate_schema(
        self,
        *,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2SchemaValidateResponse:
        """
        Validate a JSON schema for extraction.

        Args:
          data_schema: Schema to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract/schema/validation",
            body=await async_maybe_transform(
                {"data_schema": data_schema}, extract_validate_schema_params.ExtractValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractV2SchemaValidateResponse,
        )

    async def wait_for_completion(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ExtractV2Job:
        """
        Wait for an extraction job to complete by polling until it reaches a terminal state.

        Args:
            job_id: The ID of the extraction job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2 hours)

            backoff: Backoff strategy: "constant", "linear" (default), or "exponential"

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed extraction job

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            job = await client.extract.create(type="file_id", value="file-abc123")
            completed_job = await client.extract.wait_for_completion(job.id, verbose=True)
            print(completed_job.extract_result)
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        async def get_status() -> ExtractV2Job:
            return await self.get(
                job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ExtractV2Job) -> bool:
            return job.status == "COMPLETED"

        def is_error(job: ExtractV2Job) -> bool:
            return job.status in ("FAILED", "CANCELLED")

        def get_error_message(job: ExtractV2Job) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
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

    async def run(
        self,
        *,
        type: Literal["url", "file_id", "parse_job_id"],
        value: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configurations: Optional[Iterable[WebhookConfigurationParam]] | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        polling_timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create an extraction job, wait for it to complete, and return the result.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Args:
            type: Type of document input.

            value: Document identifier (URL, file ID, or parse job ID).

            config: Extraction configuration combining parse and extract settings.

            configuration_id: Saved extract configuration ID (mutually exclusive with config)

            webhook_configurations: The outbound webhook configurations

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            polling_timeout: Maximum time to wait in seconds (default: 2 hours)

            backoff: Backoff strategy: "constant", "linear" (default), or "exponential"

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The completed extraction job with extract_result populated

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            result = await client.extract.run(
                type="file_id",
                value="file-abc123",
                config={"extract_options": {"data_schema": {...}}},
                verbose=True,
            )
            print(result.extract_result)
            ```
        """
        job = await self.create(
            type=type,
            value=value,
            organization_id=organization_id,
            project_id=project_id,
            config=config,
            configuration_id=configuration_id,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return await self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=polling_timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_raw_response_wrapper(
            extract.create,
        )
        self.list = to_raw_response_wrapper(
            extract.list,
        )
        self.delete = to_raw_response_wrapper(
            extract.delete,
        )
        self.generate_schema = to_raw_response_wrapper(
            extract.generate_schema,
        )
        self.get = to_raw_response_wrapper(
            extract.get,
        )
        self.validate_schema = to_raw_response_wrapper(
            extract.validate_schema,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_raw_response_wrapper(
            extract.create,
        )
        self.list = async_to_raw_response_wrapper(
            extract.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extract.delete,
        )
        self.generate_schema = async_to_raw_response_wrapper(
            extract.generate_schema,
        )
        self.get = async_to_raw_response_wrapper(
            extract.get,
        )
        self.validate_schema = async_to_raw_response_wrapper(
            extract.validate_schema,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_streamed_response_wrapper(
            extract.create,
        )
        self.list = to_streamed_response_wrapper(
            extract.list,
        )
        self.delete = to_streamed_response_wrapper(
            extract.delete,
        )
        self.generate_schema = to_streamed_response_wrapper(
            extract.generate_schema,
        )
        self.get = to_streamed_response_wrapper(
            extract.get,
        )
        self.validate_schema = to_streamed_response_wrapper(
            extract.validate_schema,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_streamed_response_wrapper(
            extract.create,
        )
        self.list = async_to_streamed_response_wrapper(
            extract.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extract.delete,
        )
        self.generate_schema = async_to_streamed_response_wrapper(
            extract.generate_schema,
        )
        self.get = async_to_streamed_response_wrapper(
            extract.get,
        )
        self.validate_schema = async_to_streamed_response_wrapper(
            extract.validate_schema,
        )
