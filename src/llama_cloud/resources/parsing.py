# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import parsing_get_params, parsing_list_params, parsing_create_params, parsing_upload_file_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedClassifyJobs, AsyncPaginatedClassifyJobs
from .._base_client import AsyncPaginator, make_request_options
from ..types.parsing_get_response import ParsingGetResponse
from ..types.parsing_list_response import ParsingListResponse
from ..types.parsing_create_response import ParsingCreateResponse
from ..types.parsing_upload_file_response import ParsingUploadFileResponse

__all__ = ["ParsingResource", "AsyncParsingResource"]


class ParsingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ParsingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        version: Union[Literal["2025-12-18", "2025-12-11", "latest"], str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingCreateResponse:
        """
        Parse a file by file ID or URL.

        Args:
          tier: The parsing tier to use

          agentic_options: Options for agentic tier parsing (with AI agents).

          client_name: Name of the client making the parsing request

          crop_box: Document crop box boundaries

          disable_cache: Whether to disable caching for this parsing job

          fast_options: Options for fast tier parsing (without AI).

          file_id: ID of an existing file in the project to parse

          http_proxy: HTTP proxy URL for network requests (only used with source_url)

          input_options: Input format-specific parsing options

          output_options: Output format and styling options

          page_ranges: Page range selection options

          processing_control: Job processing control and failure handling

          processing_options: Processing options shared across all tiers

          source_url: Source URL to fetch document from

          version: Version of the tier configuration

          webhook_configurations: List of webhook configurations for notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2alpha1/parse",
            body=maybe_transform(
                {
                    "tier": tier,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "crop_box": crop_box,
                    "disable_cache": disable_cache,
                    "fast_options": fast_options,
                    "file_id": file_id,
                    "http_proxy": http_proxy,
                    "input_options": input_options,
                    "output_options": output_options,
                    "page_ranges": page_ranges,
                    "processing_control": processing_control,
                    "processing_options": processing_options,
                    "source_url": source_url,
                    "version": version,
                    "webhook_configurations": webhook_configurations,
                },
                parsing_create_params.ParsingCreateParams,
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
                    parsing_create_params.ParsingCreateParams,
                ),
            ),
            cast_to=ParsingCreateResponse,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedClassifyJobs[ParsingListResponse]:
        """
        List parse jobs for the current project with optional status filtering and
        pagination.

        Args:
          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2alpha1/parse",
            page=SyncPaginatedClassifyJobs[ParsingListResponse],
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
                        "status": status,
                    },
                    parsing_list_params.ParsingListParams,
                ),
            ),
            model=ParsingListResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetResponse:
        """
        Retrieve parse job with optional expanded result data (text, markdown, items).

        Args:
          expand: List of fields to include in response. Supported values: text, markdown, items,
              text_content_metadata, markdown_content_metadata, items_content_metadata.
              Example: ?expand=text&expand=markdown&expand=text_content_metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v2alpha1/parse/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_get_params.ParsingGetParams,
                ),
            ),
            cast_to=ParsingGetResponse,
        )

    def upload_file(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingUploadFileResponse:
        """
        Upload and parse a file using multipart/form-data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2alpha1/parse/upload",
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
                    parsing_upload_file_params.ParsingUploadFileParams,
                ),
            ),
            cast_to=ParsingUploadFileResponse,
        )


class AsyncParsingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncParsingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        version: Union[Literal["2025-12-18", "2025-12-11", "latest"], str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingCreateResponse:
        """
        Parse a file by file ID or URL.

        Args:
          tier: The parsing tier to use

          agentic_options: Options for agentic tier parsing (with AI agents).

          client_name: Name of the client making the parsing request

          crop_box: Document crop box boundaries

          disable_cache: Whether to disable caching for this parsing job

          fast_options: Options for fast tier parsing (without AI).

          file_id: ID of an existing file in the project to parse

          http_proxy: HTTP proxy URL for network requests (only used with source_url)

          input_options: Input format-specific parsing options

          output_options: Output format and styling options

          page_ranges: Page range selection options

          processing_control: Job processing control and failure handling

          processing_options: Processing options shared across all tiers

          source_url: Source URL to fetch document from

          version: Version of the tier configuration

          webhook_configurations: List of webhook configurations for notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2alpha1/parse",
            body=await async_maybe_transform(
                {
                    "tier": tier,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "crop_box": crop_box,
                    "disable_cache": disable_cache,
                    "fast_options": fast_options,
                    "file_id": file_id,
                    "http_proxy": http_proxy,
                    "input_options": input_options,
                    "output_options": output_options,
                    "page_ranges": page_ranges,
                    "processing_control": processing_control,
                    "processing_options": processing_options,
                    "source_url": source_url,
                    "version": version,
                    "webhook_configurations": webhook_configurations,
                },
                parsing_create_params.ParsingCreateParams,
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
                    parsing_create_params.ParsingCreateParams,
                ),
            ),
            cast_to=ParsingCreateResponse,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ParsingListResponse, AsyncPaginatedClassifyJobs[ParsingListResponse]]:
        """
        List parse jobs for the current project with optional status filtering and
        pagination.

        Args:
          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2alpha1/parse",
            page=AsyncPaginatedClassifyJobs[ParsingListResponse],
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
                        "status": status,
                    },
                    parsing_list_params.ParsingListParams,
                ),
            ),
            model=ParsingListResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetResponse:
        """
        Retrieve parse job with optional expanded result data (text, markdown, items).

        Args:
          expand: List of fields to include in response. Supported values: text, markdown, items,
              text_content_metadata, markdown_content_metadata, items_content_metadata.
              Example: ?expand=text&expand=markdown&expand=text_content_metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v2alpha1/parse/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_get_params.ParsingGetParams,
                ),
            ),
            cast_to=ParsingGetResponse,
        )

    async def upload_file(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingUploadFileResponse:
        """
        Upload and parse a file using multipart/form-data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2alpha1/parse/upload",
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
                    parsing_upload_file_params.ParsingUploadFileParams,
                ),
            ),
            cast_to=ParsingUploadFileResponse,
        )


class ParsingResourceWithRawResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create = to_raw_response_wrapper(
            parsing.create,
        )
        self.list = to_raw_response_wrapper(
            parsing.list,
        )
        self.get = to_raw_response_wrapper(
            parsing.get,
        )
        self.upload_file = to_raw_response_wrapper(
            parsing.upload_file,
        )


class AsyncParsingResourceWithRawResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create = async_to_raw_response_wrapper(
            parsing.create,
        )
        self.list = async_to_raw_response_wrapper(
            parsing.list,
        )
        self.get = async_to_raw_response_wrapper(
            parsing.get,
        )
        self.upload_file = async_to_raw_response_wrapper(
            parsing.upload_file,
        )


class ParsingResourceWithStreamingResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create = to_streamed_response_wrapper(
            parsing.create,
        )
        self.list = to_streamed_response_wrapper(
            parsing.list,
        )
        self.get = to_streamed_response_wrapper(
            parsing.get,
        )
        self.upload_file = to_streamed_response_wrapper(
            parsing.upload_file,
        )


class AsyncParsingResourceWithStreamingResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create = async_to_streamed_response_wrapper(
            parsing.create,
        )
        self.list = async_to_streamed_response_wrapper(
            parsing.list,
        )
        self.get = async_to_streamed_response_wrapper(
            parsing.get,
        )
        self.upload_file = async_to_streamed_response_wrapper(
            parsing.upload_file,
        )
