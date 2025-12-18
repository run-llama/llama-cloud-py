# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import parsing_upload_file_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
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

        self.upload_file = to_raw_response_wrapper(
            parsing.upload_file,
        )


class AsyncParsingResourceWithRawResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.upload_file = async_to_raw_response_wrapper(
            parsing.upload_file,
        )


class ParsingResourceWithStreamingResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.upload_file = to_streamed_response_wrapper(
            parsing.upload_file,
        )


class AsyncParsingResourceWithStreamingResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.upload_file = async_to_streamed_response_wrapper(
            parsing.upload_file,
        )
