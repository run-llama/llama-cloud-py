# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .result import (
    ResultResource,
    AsyncResultResource,
    ResultResourceWithRawResponse,
    AsyncResultResourceWithRawResponse,
    ResultResourceWithStreamingResponse,
    AsyncResultResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.parsing_job import ParsingJob
from ....types.presigned_url import PresignedURL

__all__ = ["JobResource", "AsyncJobResource"]


class JobResource(SyncAPIResource):
    @cached_property
    def result(self) -> ResultResource:
        return ResultResource(self._client)

    @cached_property
    def with_raw_response(self) -> JobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return JobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return JobResourceWithStreamingResponse(self)

    def generate_presigned_url(
        self,
        filename: str,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Generate a presigned URL for a job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return self._get(
            f"/api/v1/parsing/job/{job_id}/read/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresignedURL,
        )

    def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
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
            f"/api/v1/parsing/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    def get_details(
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
            f"/api/v1/parsing/job/{job_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_parameters(
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
            f"/api/v1/parsing/job/{job_id}/parameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncJobResource(AsyncAPIResource):
    @cached_property
    def result(self) -> AsyncResultResource:
        return AsyncResultResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncJobResourceWithStreamingResponse(self)

    async def generate_presigned_url(
        self,
        filename: str,
        *,
        job_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """
        Generate a presigned URL for a job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return await self._get(
            f"/api/v1/parsing/job/{job_id}/read/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresignedURL,
        )

    async def get(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
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
            f"/api/v1/parsing/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    async def get_details(
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
            f"/api/v1/parsing/job/{job_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_parameters(
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
            f"/api/v1/parsing/job/{job_id}/parameters",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class JobResourceWithRawResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.generate_presigned_url = to_raw_response_wrapper(
            job.generate_presigned_url,
        )
        self.get = to_raw_response_wrapper(
            job.get,
        )
        self.get_details = to_raw_response_wrapper(
            job.get_details,
        )
        self.get_parameters = to_raw_response_wrapper(
            job.get_parameters,
        )

    @cached_property
    def result(self) -> ResultResourceWithRawResponse:
        return ResultResourceWithRawResponse(self._job.result)


class AsyncJobResourceWithRawResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.generate_presigned_url = async_to_raw_response_wrapper(
            job.generate_presigned_url,
        )
        self.get = async_to_raw_response_wrapper(
            job.get,
        )
        self.get_details = async_to_raw_response_wrapper(
            job.get_details,
        )
        self.get_parameters = async_to_raw_response_wrapper(
            job.get_parameters,
        )

    @cached_property
    def result(self) -> AsyncResultResourceWithRawResponse:
        return AsyncResultResourceWithRawResponse(self._job.result)


class JobResourceWithStreamingResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.generate_presigned_url = to_streamed_response_wrapper(
            job.generate_presigned_url,
        )
        self.get = to_streamed_response_wrapper(
            job.get,
        )
        self.get_details = to_streamed_response_wrapper(
            job.get_details,
        )
        self.get_parameters = to_streamed_response_wrapper(
            job.get_parameters,
        )

    @cached_property
    def result(self) -> ResultResourceWithStreamingResponse:
        return ResultResourceWithStreamingResponse(self._job.result)


class AsyncJobResourceWithStreamingResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.generate_presigned_url = async_to_streamed_response_wrapper(
            job.generate_presigned_url,
        )
        self.get = async_to_streamed_response_wrapper(
            job.get,
        )
        self.get_details = async_to_streamed_response_wrapper(
            job.get_details,
        )
        self.get_parameters = async_to_streamed_response_wrapper(
            job.get_parameters,
        )

    @cached_property
    def result(self) -> AsyncResultResourceWithStreamingResponse:
        return AsyncResultResourceWithStreamingResponse(self._job.result)
