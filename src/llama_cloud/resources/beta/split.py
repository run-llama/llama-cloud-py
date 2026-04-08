# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ...types.beta import split_get_params, split_list_params, split_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.beta.split_get_response import SplitGetResponse
from ...types.beta.split_list_response import SplitListResponse
from ...types.beta.split_create_response import SplitCreateResponse
from ...types.beta.split_document_input_param import SplitDocumentInputParam

__all__ = ["SplitResource", "AsyncSplitResource"]


class SplitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return SplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return SplitResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """
        Create a document split job.

        Args:
          document_input: Document to be split.

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved split configuration ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/split/jobs",
            body=maybe_transform(
                {
                    "document_input": document_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                },
                split_create_params.SplitCreateParams,
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
                    split_create_params.SplitCreateParams,
                ),
            ),
            cast_to=SplitCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[SplitListResponse]:
        """
        List document split jobs.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status (pending, processing, completed, failed, cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/split/jobs",
            page=SyncPaginatedCursor[SplitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    split_list_params.SplitListParams,
                ),
            ),
            model=SplitListResponse,
        )

    def get(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitGetResponse:
        """
        Get a document split job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return self._get(
            path_template("/api/v1/beta/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_get_params.SplitGetParams,
                ),
            ),
            cast_to=SplitGetResponse,
        )


class AsyncSplitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncSplitResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """
        Create a document split job.

        Args:
          document_input: Document to be split.

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved split configuration ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/split/jobs",
            body=await async_maybe_transform(
                {
                    "document_input": document_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                },
                split_create_params.SplitCreateParams,
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
                    split_create_params.SplitCreateParams,
                ),
            ),
            cast_to=SplitCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SplitListResponse, AsyncPaginatedCursor[SplitListResponse]]:
        """
        List document split jobs.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status (pending, processing, completed, failed, cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/split/jobs",
            page=AsyncPaginatedCursor[SplitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    split_list_params.SplitListParams,
                ),
            ),
            model=SplitListResponse,
        )

    async def get(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitGetResponse:
        """
        Get a document split job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return await self._get(
            path_template("/api/v1/beta/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_get_params.SplitGetParams,
                ),
            ),
            cast_to=SplitGetResponse,
        )


class SplitResourceWithRawResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_raw_response_wrapper(
            split.create,
        )
        self.list = to_raw_response_wrapper(
            split.list,
        )
        self.get = to_raw_response_wrapper(
            split.get,
        )


class AsyncSplitResourceWithRawResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_raw_response_wrapper(
            split.create,
        )
        self.list = async_to_raw_response_wrapper(
            split.list,
        )
        self.get = async_to_raw_response_wrapper(
            split.get,
        )


class SplitResourceWithStreamingResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_streamed_response_wrapper(
            split.create,
        )
        self.list = to_streamed_response_wrapper(
            split.list,
        )
        self.get = to_streamed_response_wrapper(
            split.get,
        )


class AsyncSplitResourceWithStreamingResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_streamed_response_wrapper(
            split.create,
        )
        self.list = async_to_streamed_response_wrapper(
            split.list,
        )
        self.get = async_to_streamed_response_wrapper(
            split.get,
        )
