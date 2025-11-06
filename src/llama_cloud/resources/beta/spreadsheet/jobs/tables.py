# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.presigned_url import PresignedURL
from .....types.beta.spreadsheet.jobs import table_retrieve_params

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

    def retrieve(
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
                    table_retrieve_params.TableRetrieveParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

    async def retrieve(
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
                    table_retrieve_params.TableRetrieveParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.retrieve = to_raw_response_wrapper(
            tables.retrieve,
        )


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.retrieve = async_to_raw_response_wrapper(
            tables.retrieve,
        )


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.retrieve = to_streamed_response_wrapper(
            tables.retrieve,
        )


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.retrieve = async_to_streamed_response_wrapper(
            tables.retrieve,
        )
