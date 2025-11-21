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
    page_figure_list_params,
    page_figure_get_figure_params,
    page_figure_get_figures_params,
    page_figure_generate_presigned_url_params,
)
from ..._base_client import make_request_options
from ...types.presigned_url import PresignedURL
from ...types.files.page_figure_list_response import PageFigureListResponse
from ...types.files.page_figure_get_figures_response import PageFigureGetFiguresResponse

__all__ = ["PageFiguresResource", "AsyncPageFiguresResource"]


class PageFiguresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageFiguresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return PageFiguresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageFiguresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return PageFiguresResourceWithStreamingResponse(self)

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
    ) -> PageFigureListResponse:
        """
        List metadata for all figures from all pages of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}/page-figures",
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
                    page_figure_list_params.PageFigureListParams,
                ),
            ),
            cast_to=PageFigureListResponse,
        )

    def generate_presigned_url(
        self,
        figure_name: str,
        *,
        id: str,
        page_index: int,
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
        Returns a presigned url to read a page figure.

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
        if not figure_name:
            raise ValueError(f"Expected a non-empty value for `figure_name` but received {figure_name!r}")
        return self._post(
            f"/api/v1/files/{id}/page-figures/{page_index}/{figure_name}/presigned_url",
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
                    page_figure_generate_presigned_url_params.PageFigureGeneratePresignedURLParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    def get_figure(
        self,
        figure_name: str,
        *,
        id: str,
        page_index: int,
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
        Get a specific figure from a page of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not figure_name:
            raise ValueError(f"Expected a non-empty value for `figure_name` but received {figure_name!r}")
        return self._get(
            f"/api/v1/files/{id}/page-figures/{page_index}/{figure_name}",
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
                    page_figure_get_figure_params.PageFigureGetFigureParams,
                ),
            ),
            cast_to=object,
        )

    def get_figures(
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
    ) -> PageFigureGetFiguresResponse:
        """
        List metadata for figures from a specific page of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/files/{id}/page-figures/{page_index}",
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
                    page_figure_get_figures_params.PageFigureGetFiguresParams,
                ),
            ),
            cast_to=PageFigureGetFiguresResponse,
        )


class AsyncPageFiguresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageFiguresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPageFiguresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageFiguresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncPageFiguresResourceWithStreamingResponse(self)

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
    ) -> PageFigureListResponse:
        """
        List metadata for all figures from all pages of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}/page-figures",
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
                    page_figure_list_params.PageFigureListParams,
                ),
            ),
            cast_to=PageFigureListResponse,
        )

    async def generate_presigned_url(
        self,
        figure_name: str,
        *,
        id: str,
        page_index: int,
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
        Returns a presigned url to read a page figure.

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
        if not figure_name:
            raise ValueError(f"Expected a non-empty value for `figure_name` but received {figure_name!r}")
        return await self._post(
            f"/api/v1/files/{id}/page-figures/{page_index}/{figure_name}/presigned_url",
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
                    page_figure_generate_presigned_url_params.PageFigureGeneratePresignedURLParams,
                ),
            ),
            cast_to=PresignedURL,
        )

    async def get_figure(
        self,
        figure_name: str,
        *,
        id: str,
        page_index: int,
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
        Get a specific figure from a page of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not figure_name:
            raise ValueError(f"Expected a non-empty value for `figure_name` but received {figure_name!r}")
        return await self._get(
            f"/api/v1/files/{id}/page-figures/{page_index}/{figure_name}",
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
                    page_figure_get_figure_params.PageFigureGetFigureParams,
                ),
            ),
            cast_to=object,
        )

    async def get_figures(
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
    ) -> PageFigureGetFiguresResponse:
        """
        List metadata for figures from a specific page of a file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/files/{id}/page-figures/{page_index}",
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
                    page_figure_get_figures_params.PageFigureGetFiguresParams,
                ),
            ),
            cast_to=PageFigureGetFiguresResponse,
        )


class PageFiguresResourceWithRawResponse:
    def __init__(self, page_figures: PageFiguresResource) -> None:
        self._page_figures = page_figures

        self.list = to_raw_response_wrapper(
            page_figures.list,
        )
        self.generate_presigned_url = to_raw_response_wrapper(
            page_figures.generate_presigned_url,
        )
        self.get_figure = to_raw_response_wrapper(
            page_figures.get_figure,
        )
        self.get_figures = to_raw_response_wrapper(
            page_figures.get_figures,
        )


class AsyncPageFiguresResourceWithRawResponse:
    def __init__(self, page_figures: AsyncPageFiguresResource) -> None:
        self._page_figures = page_figures

        self.list = async_to_raw_response_wrapper(
            page_figures.list,
        )
        self.generate_presigned_url = async_to_raw_response_wrapper(
            page_figures.generate_presigned_url,
        )
        self.get_figure = async_to_raw_response_wrapper(
            page_figures.get_figure,
        )
        self.get_figures = async_to_raw_response_wrapper(
            page_figures.get_figures,
        )


class PageFiguresResourceWithStreamingResponse:
    def __init__(self, page_figures: PageFiguresResource) -> None:
        self._page_figures = page_figures

        self.list = to_streamed_response_wrapper(
            page_figures.list,
        )
        self.generate_presigned_url = to_streamed_response_wrapper(
            page_figures.generate_presigned_url,
        )
        self.get_figure = to_streamed_response_wrapper(
            page_figures.get_figure,
        )
        self.get_figures = to_streamed_response_wrapper(
            page_figures.get_figures,
        )


class AsyncPageFiguresResourceWithStreamingResponse:
    def __init__(self, page_figures: AsyncPageFiguresResource) -> None:
        self._page_figures = page_figures

        self.list = async_to_streamed_response_wrapper(
            page_figures.list,
        )
        self.generate_presigned_url = async_to_streamed_response_wrapper(
            page_figures.generate_presigned_url,
        )
        self.get_figure = async_to_streamed_response_wrapper(
            page_figures.get_figure,
        )
        self.get_figures = async_to_streamed_response_wrapper(
            page_figures.get_figures,
        )
