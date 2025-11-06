# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.files import (
    page_screenshot_list_params,
    page_screenshot_retrieve_params,
    page_screenshot_generate_presigned_url_params,
)
from ..._base_client import make_request_options
from ...types.presigned_url import PresignedURL
from ...types.files.page_screenshot_list_response import PageScreenshotListResponse

__all__ = ["PageScreenshotsResource", "AsyncPageScreenshotsResource"]


class PageScreenshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageScreenshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return PageScreenshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageScreenshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return PageScreenshotsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        page_index: int,
        *,
        id: str,
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
        Get screenshot of a page from a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}/page_screenshots/{page_index}",
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
                    page_screenshot_retrieve_params.PageScreenshotRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    def list(
        self,
        id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageScreenshotListResponse:
        """
        List metadata for all screenshots of pages from a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}/page_screenshots",
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
                    page_screenshot_list_params.PageScreenshotListParams,
                ),
            ),
            cast_to=PageScreenshotListResponse,
        )

    def generate_presigned_url(
        self,
        page_index: int,
        *,
        id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Returns a presigned url to read a page screenshot.

        The presigned url is valid for a limited time period, after which it will
        expire. Be careful on accidental exposure of the presigned url, as it may allow
        unauthorized access to the file before the expiration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/files/{id}/page_screenshots/{page_index}/presigned_url",
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
                    page_screenshot_generate_presigned_url_params.PageScreenshotGeneratePresignedURLParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class AsyncPageScreenshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageScreenshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPageScreenshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageScreenshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncPageScreenshotsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        page_index: int,
        *,
        id: str,
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
        Get screenshot of a page from a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}/page_screenshots/{page_index}",
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
                    page_screenshot_retrieve_params.PageScreenshotRetrieveParams,
                ),
            ),
            cast_to=object,
        )

    async def list(
        self,
        id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageScreenshotListResponse:
        """
        List metadata for all screenshots of pages from a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}/page_screenshots",
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
                    page_screenshot_list_params.PageScreenshotListParams,
                ),
            ),
            cast_to=PageScreenshotListResponse,
        )

    async def generate_presigned_url(
        self,
        page_index: int,
        *,
        id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Returns a presigned url to read a page screenshot.

        The presigned url is valid for a limited time period, after which it will
        expire. Be careful on accidental exposure of the presigned url, as it may allow
        unauthorized access to the file before the expiration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/files/{id}/page_screenshots/{page_index}/presigned_url",
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
                    page_screenshot_generate_presigned_url_params.PageScreenshotGeneratePresignedURLParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class PageScreenshotsResourceWithRawResponse:
    def __init__(self, page_screenshots: PageScreenshotsResource) -> None:
        self._page_screenshots = page_screenshots

        self.retrieve = to_raw_response_wrapper(
            page_screenshots.retrieve,
        )
        self.list = to_raw_response_wrapper(
            page_screenshots.list,
        )
        self.generate_presigned_url = to_raw_response_wrapper(
            page_screenshots.generate_presigned_url,
        )


class AsyncPageScreenshotsResourceWithRawResponse:
    def __init__(self, page_screenshots: AsyncPageScreenshotsResource) -> None:
        self._page_screenshots = page_screenshots

        self.retrieve = async_to_raw_response_wrapper(
            page_screenshots.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            page_screenshots.list,
        )
        self.generate_presigned_url = async_to_raw_response_wrapper(
            page_screenshots.generate_presigned_url,
        )


class PageScreenshotsResourceWithStreamingResponse:
    def __init__(self, page_screenshots: PageScreenshotsResource) -> None:
        self._page_screenshots = page_screenshots

        self.retrieve = to_streamed_response_wrapper(
            page_screenshots.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            page_screenshots.list,
        )
        self.generate_presigned_url = to_streamed_response_wrapper(
            page_screenshots.generate_presigned_url,
        )


class AsyncPageScreenshotsResourceWithStreamingResponse:
    def __init__(self, page_screenshots: AsyncPageScreenshotsResource) -> None:
        self._page_screenshots = page_screenshots

        self.retrieve = async_to_streamed_response_wrapper(
            page_screenshots.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            page_screenshots.list,
        )
        self.generate_presigned_url = async_to_streamed_response_wrapper(
            page_screenshots.generate_presigned_url,
        )
