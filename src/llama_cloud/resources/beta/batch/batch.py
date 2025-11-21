# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from .job_items import (
    JobItemsResource,
    AsyncJobItemsResource,
    JobItemsResourceWithRawResponse,
    AsyncJobItemsResourceWithRawResponse,
    JobItemsResourceWithStreamingResponse,
    AsyncJobItemsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedBatchItems, AsyncPaginatedBatchItems
from ....types.beta import batch_list_params, batch_cancel_params, batch_create_params, batch_get_status_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.beta.batch_list_response import BatchListResponse
from ....types.beta.batch_cancel_response import BatchCancelResponse
from ....types.beta.batch_create_response import BatchCreateResponse
from ....types.beta.batch_get_status_response import BatchGetStatusResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def job_items(self) -> JobItemsResource:
        return JobItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        job_config: batch_create_params.JobConfig,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        continue_as_new_threshold: Optional[int] | Omit = omit,
        directory_id: Optional[str] | Omit = omit,
        item_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        page_size: int | Omit = omit,
        temporal_namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Create a new batch processing job for a directory.

        Processes all files in the specified directory according to the job
        configuration. The job runs asynchronously and you can monitor progress using
        the job status endpoint.

        Args:
          job_config: Job configuration for batch processing. Can be BatchParseJobRecordCreate or
              ClassifyJob.

          continue_as_new_threshold: Maximum number of files to process before calling continue-as-new. If None,
              continue-as-new is called after every batch. (only used in directory mode)

          directory_id: ID of the directory containing files to process

          item_ids: List of specific item IDs to process. Either this or directory_id must be
              provided.

          page_size: Number of files to fetch per batch from the directory (only used in directory
              mode)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"temporal-namespace": temporal_namespace}), **(extra_headers or {})}
        return self._post(
            "/api/v1/beta/batch-processing",
            body=maybe_transform(
                {
                    "job_config": job_config,
                    "continue_as_new_threshold": continue_as_new_threshold,
                    "directory_id": directory_id,
                    "item_ids": item_ids,
                    "page_size": page_size,
                },
                batch_create_params.BatchCreateParams,
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
                    batch_create_params.BatchCreateParams,
                ),
            ),
            cast_to=BatchCreateResponse,
        )

    def list(
        self,
        *,
        directory_id: Optional[str] | Omit = omit,
        job_type: Optional[Literal["parse", "extract", "classify"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "running", "dispatched", "completed", "failed", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedBatchItems[BatchListResponse]:
        """
        List all batch processing jobs for a project with optional filtering.

        Returns a paginated list of batch jobs with filters for directory, job type, and
        status. Useful for viewing job history, monitoring progress, and finding
        specific jobs.

        Args:
          directory_id: Filter by directory ID

          job_type: Type of batch processing operation.

          limit: Maximum number of jobs to return

          offset: Number of jobs to skip for pagination

          status: Status of a batch processing job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/batch-processing",
            page=SyncPaginatedBatchItems[BatchListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory_id": directory_id,
                        "job_type": job_type,
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "status": status,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            model=BatchListResponse,
        )

    def cancel(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        temporal_namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCancelResponse:
        """
        Cancel a running batch processing job.

        Stops processing and marks all pending items as cancelled. Items currently being
        processed may complete depending on their state.

        Args:
          reason: Optional reason for cancelling the job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {**strip_not_given({"temporal-namespace": temporal_namespace}), **(extra_headers or {})}
        return self._post(
            f"/api/v1/beta/batch-processing/{job_id}/cancel",
            body=maybe_transform({"reason": reason}, batch_cancel_params.BatchCancelParams),
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
                    batch_cancel_params.BatchCancelParams,
                ),
            ),
            cast_to=BatchCancelResponse,
        )

    def get_status(
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
    ) -> BatchGetStatusResponse:
        """
        Get detailed status of a batch processing job.

        Returns current progress, file counts, and estimated completion time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/api/v1/beta/batch-processing/{job_id}",
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
                    batch_get_status_params.BatchGetStatusParams,
                ),
            ),
            cast_to=BatchGetStatusResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def job_items(self) -> AsyncJobItemsResource:
        return AsyncJobItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        job_config: batch_create_params.JobConfig,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        continue_as_new_threshold: Optional[int] | Omit = omit,
        directory_id: Optional[str] | Omit = omit,
        item_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        page_size: int | Omit = omit,
        temporal_namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Create a new batch processing job for a directory.

        Processes all files in the specified directory according to the job
        configuration. The job runs asynchronously and you can monitor progress using
        the job status endpoint.

        Args:
          job_config: Job configuration for batch processing. Can be BatchParseJobRecordCreate or
              ClassifyJob.

          continue_as_new_threshold: Maximum number of files to process before calling continue-as-new. If None,
              continue-as-new is called after every batch. (only used in directory mode)

          directory_id: ID of the directory containing files to process

          item_ids: List of specific item IDs to process. Either this or directory_id must be
              provided.

          page_size: Number of files to fetch per batch from the directory (only used in directory
              mode)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"temporal-namespace": temporal_namespace}), **(extra_headers or {})}
        return await self._post(
            "/api/v1/beta/batch-processing",
            body=await async_maybe_transform(
                {
                    "job_config": job_config,
                    "continue_as_new_threshold": continue_as_new_threshold,
                    "directory_id": directory_id,
                    "item_ids": item_ids,
                    "page_size": page_size,
                },
                batch_create_params.BatchCreateParams,
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
                    batch_create_params.BatchCreateParams,
                ),
            ),
            cast_to=BatchCreateResponse,
        )

    def list(
        self,
        *,
        directory_id: Optional[str] | Omit = omit,
        job_type: Optional[Literal["parse", "extract", "classify"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "running", "dispatched", "completed", "failed", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BatchListResponse, AsyncPaginatedBatchItems[BatchListResponse]]:
        """
        List all batch processing jobs for a project with optional filtering.

        Returns a paginated list of batch jobs with filters for directory, job type, and
        status. Useful for viewing job history, monitoring progress, and finding
        specific jobs.

        Args:
          directory_id: Filter by directory ID

          job_type: Type of batch processing operation.

          limit: Maximum number of jobs to return

          offset: Number of jobs to skip for pagination

          status: Status of a batch processing job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/batch-processing",
            page=AsyncPaginatedBatchItems[BatchListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory_id": directory_id,
                        "job_type": job_type,
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "status": status,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            model=BatchListResponse,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        temporal_namespace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCancelResponse:
        """
        Cancel a running batch processing job.

        Stops processing and marks all pending items as cancelled. Items currently being
        processed may complete depending on their state.

        Args:
          reason: Optional reason for cancelling the job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {**strip_not_given({"temporal-namespace": temporal_namespace}), **(extra_headers or {})}
        return await self._post(
            f"/api/v1/beta/batch-processing/{job_id}/cancel",
            body=await async_maybe_transform({"reason": reason}, batch_cancel_params.BatchCancelParams),
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
                    batch_cancel_params.BatchCancelParams,
                ),
            ),
            cast_to=BatchCancelResponse,
        )

    async def get_status(
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
    ) -> BatchGetStatusResponse:
        """
        Get detailed status of a batch processing job.

        Returns current progress, file counts, and estimated completion time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/api/v1/beta/batch-processing/{job_id}",
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
                    batch_get_status_params.BatchGetStatusParams,
                ),
            ),
            cast_to=BatchGetStatusResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.list = to_raw_response_wrapper(
            batch.list,
        )
        self.cancel = to_raw_response_wrapper(
            batch.cancel,
        )
        self.get_status = to_raw_response_wrapper(
            batch.get_status,
        )

    @cached_property
    def job_items(self) -> JobItemsResourceWithRawResponse:
        return JobItemsResourceWithRawResponse(self._batch.job_items)


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.list = async_to_raw_response_wrapper(
            batch.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            batch.cancel,
        )
        self.get_status = async_to_raw_response_wrapper(
            batch.get_status,
        )

    @cached_property
    def job_items(self) -> AsyncJobItemsResourceWithRawResponse:
        return AsyncJobItemsResourceWithRawResponse(self._batch.job_items)


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.list = to_streamed_response_wrapper(
            batch.list,
        )
        self.cancel = to_streamed_response_wrapper(
            batch.cancel,
        )
        self.get_status = to_streamed_response_wrapper(
            batch.get_status,
        )

    @cached_property
    def job_items(self) -> JobItemsResourceWithStreamingResponse:
        return JobItemsResourceWithStreamingResponse(self._batch.job_items)


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.list = async_to_streamed_response_wrapper(
            batch.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            batch.cancel,
        )
        self.get_status = async_to_streamed_response_wrapper(
            batch.get_status,
        )

    @cached_property
    def job_items(self) -> AsyncJobItemsResourceWithStreamingResponse:
        return AsyncJobItemsResourceWithStreamingResponse(self._batch.job_items)
