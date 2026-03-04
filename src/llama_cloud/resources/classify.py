# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import classify_get_params, classify_list_params, classify_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.classify_get_response import ClassifyGetResponse
from ..types.classify_list_response import ClassifyListResponse
from ..types.classify_create_response import ClassifyCreateResponse
from ..types.classify_configuration_param import ClassifyConfigurationParam

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[ClassifyConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        parse_job_id: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyCreateResponse:
        """
        Create a classify job.

        Args:
          configuration: Configuration for classification.

          configuration_id: Product configuration ID for reusable presets

          file_id: File ID to classify

          parse_job_id: Parse job ID to classify

          transaction_id: Idempotency key scoped to the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/classify",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "file_id": file_id,
                    "parse_job_id": parse_job_id,
                    "transaction_id": transaction_id,
                },
                classify_create_params.ClassifyCreateParams,
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
                    classify_create_params.ClassifyCreateParams,
                ),
            ),
            cast_to=ClassifyCreateResponse,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ClassifyListResponse]:
        """
        List classify jobs.

        Args:
          configuration_id: Filter by configuration ID

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/classify",
            page=SyncPaginatedCursor[ClassifyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    classify_list_params.ClassifyListParams,
                ),
            ),
            model=ClassifyListResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyGetResponse:
        """
        Retrieve classify job by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v2/classify/{job_id}",
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
                    classify_get_params.ClassifyGetParams,
                ),
            ),
            cast_to=ClassifyGetResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[ClassifyConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        parse_job_id: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyCreateResponse:
        """
        Create a classify job.

        Args:
          configuration: Configuration for classification.

          configuration_id: Product configuration ID for reusable presets

          file_id: File ID to classify

          parse_job_id: Parse job ID to classify

          transaction_id: Idempotency key scoped to the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/classify",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "file_id": file_id,
                    "parse_job_id": parse_job_id,
                    "transaction_id": transaction_id,
                },
                classify_create_params.ClassifyCreateParams,
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
                    classify_create_params.ClassifyCreateParams,
                ),
            ),
            cast_to=ClassifyCreateResponse,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ClassifyListResponse, AsyncPaginatedCursor[ClassifyListResponse]]:
        """
        List classify jobs.

        Args:
          configuration_id: Filter by configuration ID

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/classify",
            page=AsyncPaginatedCursor[ClassifyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    classify_list_params.ClassifyListParams,
                ),
            ),
            model=ClassifyListResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyGetResponse:
        """
        Retrieve classify job by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v2/classify/{job_id}",
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
                    classify_get_params.ClassifyGetParams,
                ),
            ),
            cast_to=ClassifyGetResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.create = to_raw_response_wrapper(
            classify.create,
        )
        self.list = to_raw_response_wrapper(
            classify.list,
        )
        self.get = to_raw_response_wrapper(
            classify.get,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.create = async_to_raw_response_wrapper(
            classify.create,
        )
        self.list = async_to_raw_response_wrapper(
            classify.list,
        )
        self.get = async_to_raw_response_wrapper(
            classify.get,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.create = to_streamed_response_wrapper(
            classify.create,
        )
        self.list = to_streamed_response_wrapper(
            classify.list,
        )
        self.get = to_streamed_response_wrapper(
            classify.get,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.create = async_to_streamed_response_wrapper(
            classify.create,
        )
        self.list = async_to_streamed_response_wrapper(
            classify.list,
        )
        self.get = async_to_streamed_response_wrapper(
            classify.get,
        )
