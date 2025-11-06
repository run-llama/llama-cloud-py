# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs.jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SpreadsheetResource", "AsyncSpreadsheetResource"]


class SpreadsheetResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpreadsheetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return SpreadsheetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpreadsheetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return SpreadsheetResourceWithStreamingResponse(self)


class AsyncSpreadsheetResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpreadsheetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSpreadsheetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpreadsheetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncSpreadsheetResourceWithStreamingResponse(self)


class SpreadsheetResourceWithRawResponse:
    def __init__(self, spreadsheet: SpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._spreadsheet.jobs)


class AsyncSpreadsheetResourceWithRawResponse:
    def __init__(self, spreadsheet: AsyncSpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._spreadsheet.jobs)


class SpreadsheetResourceWithStreamingResponse:
    def __init__(self, spreadsheet: SpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._spreadsheet.jobs)


class AsyncSpreadsheetResourceWithStreamingResponse:
    def __init__(self, spreadsheet: AsyncSpreadsheetResource) -> None:
        self._spreadsheet = spreadsheet

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._spreadsheet.jobs)
