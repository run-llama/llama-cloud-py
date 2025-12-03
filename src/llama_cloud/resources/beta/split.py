# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.beta import split_get_params, split_list_params, split_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.beta.split_get_response import SplitGetResponse
from ...types.beta.split_list_response import SplitListResponse
from ...types.beta.split_create_response import SplitCreateResponse

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
        categories: Iterable[split_create_params.Category],
        document_input: split_create_params.DocumentInput,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        splitting_strategy: split_create_params.SplittingStrategy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """Create a document split job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          categories: Categories to split the document into.

          document_input: Document to be split.

          splitting_strategy: Strategy for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/split/jobs",
            body=maybe_transform(
                {
                    "categories": categories,
                    "document_input": document_input,
                    "splitting_strategy": splitting_strategy,
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
    ) -> SyncPaginatedClassifyJobs[SplitListResponse]:
        """List document split jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/split/jobs",
            page=SyncPaginatedClassifyJobs[SplitListResponse],
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

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return self._get(
            f"/api/v1/beta/split/jobs/{split_job_id}",
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
        categories: Iterable[split_create_params.Category],
        document_input: split_create_params.DocumentInput,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        splitting_strategy: split_create_params.SplittingStrategy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """Create a document split job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          categories: Categories to split the document into.

          document_input: Document to be split.

          splitting_strategy: Strategy for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/split/jobs",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "document_input": document_input,
                    "splitting_strategy": splitting_strategy,
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
    ) -> AsyncPaginator[SplitListResponse, AsyncPaginatedClassifyJobs[SplitListResponse]]:
        """List document split jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/split/jobs",
            page=AsyncPaginatedClassifyJobs[SplitListResponse],
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

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return await self._get(
            f"/api/v1/beta/split/jobs/{split_job_id}",
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
