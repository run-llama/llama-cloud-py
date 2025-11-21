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
    sheet_get_params,
    sheet_list_params,
    sheet_create_params,
    sheet_delete_job_params,
    sheet_get_result_table_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.presigned_url import PresignedURL
from ...types.beta.sheets_job import SheetsJob
from ...types.beta.sheets_parsing_config_param import SheetsParsingConfigParam

__all__ = ["SheetsResource", "AsyncSheetsResource"]


class SheetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return SheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return SheetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
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
            "/api/v1/beta/sheets/jobs",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                sheet_create_params.SheetCreateParams,
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
                    sheet_create_params.SheetCreateParams,
                ),
            ),
            cast_to=SheetsJob,
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
    ) -> SyncPaginatedClassifyJobs[SheetsJob]:
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
            "/api/v1/beta/sheets/jobs",
            page=SyncPaginatedClassifyJobs[SheetsJob],
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
                    sheet_list_params.SheetListParams,
                ),
            ),
            model=SheetsJob,
        )

    def delete_job(
        self,
        spreadsheet_job_id: str,
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
        """Delete a spreadsheet parsing job and its associated data.

        Experimental: This
        endpoint is not yet ready for production use and is subject to change at any
        time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return self._delete(
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}",
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
                    sheet_delete_job_params.SheetDeleteJobParams,
                ),
            ),
            cast_to=object,
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
    ) -> SheetsJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted regions
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
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}",
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
                    sheet_get_params.SheetGetParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    def get_result_table(
        self,
        region_type: Literal["table", "extra", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        region_id: str,
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
        """Generate a presigned URL to download a specific extracted region.

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
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        if not region_type:
            raise ValueError(f"Expected a non-empty value for `region_type` but received {region_type!r}")
        return self._get(
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}",
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
                    sheet_get_result_table_params.SheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class AsyncSheetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncSheetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
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
            "/api/v1/beta/sheets/jobs",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                sheet_create_params.SheetCreateParams,
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
                    sheet_create_params.SheetCreateParams,
                ),
            ),
            cast_to=SheetsJob,
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
    ) -> AsyncPaginator[SheetsJob, AsyncPaginatedClassifyJobs[SheetsJob]]:
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
            "/api/v1/beta/sheets/jobs",
            page=AsyncPaginatedClassifyJobs[SheetsJob],
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
                    sheet_list_params.SheetListParams,
                ),
            ),
            model=SheetsJob,
        )

    async def delete_job(
        self,
        spreadsheet_job_id: str,
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
        """Delete a spreadsheet parsing job and its associated data.

        Experimental: This
        endpoint is not yet ready for production use and is subject to change at any
        time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return await self._delete(
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}",
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
                    sheet_delete_job_params.SheetDeleteJobParams,
                ),
            ),
            cast_to=object,
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
    ) -> SheetsJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted regions
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
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}",
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
                    sheet_get_params.SheetGetParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    async def get_result_table(
        self,
        region_type: Literal["table", "extra", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        region_id: str,
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
        """Generate a presigned URL to download a specific extracted region.

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
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        if not region_type:
            raise ValueError(f"Expected a non-empty value for `region_type` but received {region_type!r}")
        return await self._get(
            f"/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}",
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
                    sheet_get_result_table_params.SheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class SheetsResourceWithRawResponse:
    def __init__(self, sheets: SheetsResource) -> None:
        self._sheets = sheets

        self.create = to_raw_response_wrapper(
            sheets.create,
        )
        self.list = to_raw_response_wrapper(
            sheets.list,
        )
        self.delete_job = to_raw_response_wrapper(
            sheets.delete_job,
        )
        self.get = to_raw_response_wrapper(
            sheets.get,
        )
        self.get_result_table = to_raw_response_wrapper(
            sheets.get_result_table,
        )


class AsyncSheetsResourceWithRawResponse:
    def __init__(self, sheets: AsyncSheetsResource) -> None:
        self._sheets = sheets

        self.create = async_to_raw_response_wrapper(
            sheets.create,
        )
        self.list = async_to_raw_response_wrapper(
            sheets.list,
        )
        self.delete_job = async_to_raw_response_wrapper(
            sheets.delete_job,
        )
        self.get = async_to_raw_response_wrapper(
            sheets.get,
        )
        self.get_result_table = async_to_raw_response_wrapper(
            sheets.get_result_table,
        )


class SheetsResourceWithStreamingResponse:
    def __init__(self, sheets: SheetsResource) -> None:
        self._sheets = sheets

        self.create = to_streamed_response_wrapper(
            sheets.create,
        )
        self.list = to_streamed_response_wrapper(
            sheets.list,
        )
        self.delete_job = to_streamed_response_wrapper(
            sheets.delete_job,
        )
        self.get = to_streamed_response_wrapper(
            sheets.get,
        )
        self.get_result_table = to_streamed_response_wrapper(
            sheets.get_result_table,
        )


class AsyncSheetsResourceWithStreamingResponse:
    def __init__(self, sheets: AsyncSheetsResource) -> None:
        self._sheets = sheets

        self.create = async_to_streamed_response_wrapper(
            sheets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sheets.list,
        )
        self.delete_job = async_to_streamed_response_wrapper(
            sheets.delete_job,
        )
        self.get = async_to_streamed_response_wrapper(
            sheets.get,
        )
        self.get_result_table = async_to_streamed_response_wrapper(
            sheets.get_result_table,
        )
