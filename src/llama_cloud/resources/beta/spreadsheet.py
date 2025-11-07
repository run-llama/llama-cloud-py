# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedClassifyJobs, AsyncPaginatedClassifyJobs
from ...types.beta import (
    spreadsheet_get_params,
    spreadsheet_list_params,
    spreadsheet_create_params,
    spreadsheet_get_result_table_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.presigned_url import PresignedURL
from ...types.beta.spreadsheet_job import SpreadsheetJob
from ...types.beta.spreadsheet_parsing_config_param import SpreadsheetParsingConfigParam

__all__ = ["SpreadsheetResource", "AsyncSpreadsheetResource"]


class SpreadsheetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpreadsheetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return SpreadsheetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpreadsheetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return SpreadsheetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SpreadsheetParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpreadsheetJob:
        """Create a spreadsheet parsing job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          file_id: The ID of the file to parse

          config: Configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/spreadsheet/jobs",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                spreadsheet_create_params.SpreadsheetCreateParams,
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
                    spreadsheet_create_params.SpreadsheetCreateParams,
                ),
            ),
            cast_to=SpreadsheetJob,
        )

    def list(
        self,
        *,
        include_results: bool | Omit = omit,
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
    ) -> SyncPaginatedClassifyJobs[SpreadsheetJob]:
        """List spreadsheet parsing jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/spreadsheet/jobs",
            page=SyncPaginatedClassifyJobs[SpreadsheetJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    spreadsheet_list_params.SpreadsheetListParams,
                ),
            ),
            model=SpreadsheetJob,
        )

    def get(
        self,
        spreadsheet_job_id: str,
        *,
        include_results: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpreadsheetJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted tables
        and results if the job is complete, eliminating the need for a separate /results
        call.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return self._get(
            f"/api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    spreadsheet_get_params.SpreadsheetGetParams,
                ),
            ),
            cast_to=SpreadsheetJob,
        )

    def get_result_table(
        self,
        table_type: Literal["table", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        table_id: str,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """Generate a presigned URL to download a specific extracted table.

        Experimental:
        This endpoint is not yet ready for production use and is subject to change at
        any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not table_type:
            raise ValueError(f"Expected a non-empty value for `table_type` but received {table_type!r}")
        return self._get(
            f"/api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}/tables/{table_id}/result/{table_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    spreadsheet_get_result_table_params.SpreadsheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class AsyncSpreadsheetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpreadsheetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSpreadsheetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpreadsheetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncSpreadsheetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SpreadsheetParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpreadsheetJob:
        """Create a spreadsheet parsing job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          file_id: The ID of the file to parse

          config: Configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/spreadsheet/jobs",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                spreadsheet_create_params.SpreadsheetCreateParams,
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
                    spreadsheet_create_params.SpreadsheetCreateParams,
                ),
            ),
            cast_to=SpreadsheetJob,
        )

    def list(
        self,
        *,
        include_results: bool | Omit = omit,
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
    ) -> AsyncPaginator[SpreadsheetJob, AsyncPaginatedClassifyJobs[SpreadsheetJob]]:
        """List spreadsheet parsing jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/spreadsheet/jobs",
            page=AsyncPaginatedClassifyJobs[SpreadsheetJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    spreadsheet_list_params.SpreadsheetListParams,
                ),
            ),
            model=SpreadsheetJob,
        )

    async def get(
        self,
        spreadsheet_job_id: str,
        *,
        include_results: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpreadsheetJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted tables
        and results if the job is complete, eliminating the need for a separate /results
        call.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return await self._get(
            f"/api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    spreadsheet_get_params.SpreadsheetGetParams,
                ),
            ),
            cast_to=SpreadsheetJob,
        )

    async def get_result_table(
        self,
        table_type: Literal["table", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        table_id: str,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """Generate a presigned URL to download a specific extracted table.

        Experimental:
        This endpoint is not yet ready for production use and is subject to change at
        any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not table_type:
            raise ValueError(f"Expected a non-empty value for `table_type` but received {table_type!r}")
        return await self._get(
            f"/api/v1/beta/spreadsheet/jobs/{spreadsheet_job_id}/tables/{table_id}/result/{table_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    spreadsheet_get_result_table_params.SpreadsheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class SpreadsheetResourceWithRawResponse:
    def __init__(self, spreadsheet: SpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

        self.create = to_raw_response_wrapper(
            spreadsheet.create,
        )
        self.list = to_raw_response_wrapper(
            spreadsheet.list,
        )
        self.get = to_raw_response_wrapper(
            spreadsheet.get,
        )
        self.get_result_table = to_raw_response_wrapper(
            spreadsheet.get_result_table,
        )


class AsyncSpreadsheetResourceWithRawResponse:
    def __init__(self, spreadsheet: AsyncSpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

        self.create = async_to_raw_response_wrapper(
            spreadsheet.create,
        )
        self.list = async_to_raw_response_wrapper(
            spreadsheet.list,
        )
        self.get = async_to_raw_response_wrapper(
            spreadsheet.get,
        )
        self.get_result_table = async_to_raw_response_wrapper(
            spreadsheet.get_result_table,
        )


class SpreadsheetResourceWithStreamingResponse:
    def __init__(self, spreadsheet: SpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

        self.create = to_streamed_response_wrapper(
            spreadsheet.create,
        )
        self.list = to_streamed_response_wrapper(
            spreadsheet.list,
        )
        self.get = to_streamed_response_wrapper(
            spreadsheet.get,
        )
        self.get_result_table = to_streamed_response_wrapper(
            spreadsheet.get_result_table,
        )


class AsyncSpreadsheetResourceWithStreamingResponse:
    def __init__(self, spreadsheet: AsyncSpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

        self.create = async_to_streamed_response_wrapper(
            spreadsheet.create,
        )
        self.list = async_to_streamed_response_wrapper(
            spreadsheet.list,
        )
        self.get = async_to_streamed_response_wrapper(
            spreadsheet.get,
        )
        self.get_result_table = async_to_streamed_response_wrapper(
            spreadsheet.get_result_table,
        )
