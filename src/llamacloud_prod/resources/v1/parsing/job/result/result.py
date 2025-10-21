# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.parsing.job import (
    result_get_json_params,
    result_get_text_params,
    result_get_markdown_params,
    result_get_structured_params,
)
from ......types.v1.parsing.job.parsing_job_json_result import ParsingJobJsonResult
from ......types.v1.parsing.job.parsing_job_text_result import ParsingJobTextResult
from ......types.v1.parsing.job.parsing_job_markdown_result import ParsingJobMarkdownResult
from ......types.v1.parsing.job.parsing_job_structured_result import ParsingJobStructuredResult

__all__ = ["ResultResource", "AsyncResultResource"]


class ResultResource(SyncAPIResource):
    @cached_property
    def raw(self) -> RawResource:
        return RawResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return ResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return ResultResourceWithStreamingResponse(self)

    def get_image(
        self,
        name: str,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "image/jpeg", **(extra_headers or {})}
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/image/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_json(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobJsonResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, result_get_json_params.ResultGetJsonParams),
            ),
            cast_to=ParsingJobJsonResult,
        )

    def get_markdown(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobMarkdownResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, result_get_markdown_params.ResultGetMarkdownParams
                ),
            ),
            cast_to=ParsingJobMarkdownResult,
        )

    def get_pdf(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_structured(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobStructuredResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/structured",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, result_get_structured_params.ResultGetStructuredParams
                ),
            ),
            cast_to=ParsingJobStructuredResult,
        )

    def get_text(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobTextResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, result_get_text_params.ResultGetTextParams),
            ),
            cast_to=ParsingJobTextResult,
        )

    def get_xlsx(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/result/xlsx",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncResultResource(AsyncAPIResource):
    @cached_property
    def raw(self) -> AsyncRawResource:
        return AsyncRawResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncResultResourceWithStreamingResponse(self)

    async def get_image(
        self,
        name: str,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "image/jpeg", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/image/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_json(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobJsonResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, result_get_json_params.ResultGetJsonParams
                ),
            ),
            cast_to=ParsingJobJsonResult,
        )

    async def get_markdown(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobMarkdownResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, result_get_markdown_params.ResultGetMarkdownParams
                ),
            ),
            cast_to=ParsingJobMarkdownResult,
        )

    async def get_pdf(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_structured(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobStructuredResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/structured",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, result_get_structured_params.ResultGetStructuredParams
                ),
            ),
            cast_to=ParsingJobStructuredResult,
        )

    async def get_text(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJobTextResult:
        """
        Get a job by id

        Note: The 'credits_used' and 'job_credits_usage' fields in the response metadata
        are deprecated and will be removed in a future release.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, result_get_text_params.ResultGetTextParams
                ),
            ),
            cast_to=ParsingJobTextResult,
        )

    async def get_xlsx(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a job by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/result/xlsx",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ResultResourceWithRawResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.get_image = to_custom_raw_response_wrapper(
            result.get_image,
            BinaryAPIResponse,
        )
        self.get_json = to_raw_response_wrapper(
            result.get_json,
        )
        self.get_markdown = to_raw_response_wrapper(
            result.get_markdown,
        )
        self.get_pdf = to_raw_response_wrapper(
            result.get_pdf,
        )
        self.get_structured = to_raw_response_wrapper(
            result.get_structured,
        )
        self.get_text = to_raw_response_wrapper(
            result.get_text,
        )
        self.get_xlsx = to_raw_response_wrapper(
            result.get_xlsx,
        )

    @cached_property
    def raw(self) -> RawResourceWithRawResponse:
        return RawResourceWithRawResponse(self._result.raw)


class AsyncResultResourceWithRawResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.get_image = async_to_custom_raw_response_wrapper(
            result.get_image,
            AsyncBinaryAPIResponse,
        )
        self.get_json = async_to_raw_response_wrapper(
            result.get_json,
        )
        self.get_markdown = async_to_raw_response_wrapper(
            result.get_markdown,
        )
        self.get_pdf = async_to_raw_response_wrapper(
            result.get_pdf,
        )
        self.get_structured = async_to_raw_response_wrapper(
            result.get_structured,
        )
        self.get_text = async_to_raw_response_wrapper(
            result.get_text,
        )
        self.get_xlsx = async_to_raw_response_wrapper(
            result.get_xlsx,
        )

    @cached_property
    def raw(self) -> AsyncRawResourceWithRawResponse:
        return AsyncRawResourceWithRawResponse(self._result.raw)


class ResultResourceWithStreamingResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.get_image = to_custom_streamed_response_wrapper(
            result.get_image,
            StreamedBinaryAPIResponse,
        )
        self.get_json = to_streamed_response_wrapper(
            result.get_json,
        )
        self.get_markdown = to_streamed_response_wrapper(
            result.get_markdown,
        )
        self.get_pdf = to_streamed_response_wrapper(
            result.get_pdf,
        )
        self.get_structured = to_streamed_response_wrapper(
            result.get_structured,
        )
        self.get_text = to_streamed_response_wrapper(
            result.get_text,
        )
        self.get_xlsx = to_streamed_response_wrapper(
            result.get_xlsx,
        )

    @cached_property
    def raw(self) -> RawResourceWithStreamingResponse:
        return RawResourceWithStreamingResponse(self._result.raw)


class AsyncResultResourceWithStreamingResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.get_image = async_to_custom_streamed_response_wrapper(
            result.get_image,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_json = async_to_streamed_response_wrapper(
            result.get_json,
        )
        self.get_markdown = async_to_streamed_response_wrapper(
            result.get_markdown,
        )
        self.get_pdf = async_to_streamed_response_wrapper(
            result.get_pdf,
        )
        self.get_structured = async_to_streamed_response_wrapper(
            result.get_structured,
        )
        self.get_text = async_to_streamed_response_wrapper(
            result.get_text,
        )
        self.get_xlsx = async_to_streamed_response_wrapper(
            result.get_xlsx,
        )

    @cached_property
    def raw(self) -> AsyncRawResourceWithStreamingResponse:
        return AsyncRawResourceWithStreamingResponse(self._result.raw)
