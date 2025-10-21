# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ClassifierResource", "AsyncClassifierResource"]


class ClassifierResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return ClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return ClassifierResourceWithStreamingResponse(self)


class AsyncClassifierResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncClassifierResourceWithStreamingResponse(self)


class ClassifierResourceWithRawResponse:
    def __init__(self, classifier: ClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._classifier.jobs)


class AsyncClassifierResourceWithRawResponse:
    def __init__(self, classifier: AsyncClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._classifier.jobs)


class ClassifierResourceWithStreamingResponse:
    def __init__(self, classifier: ClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._classifier.jobs)


class AsyncClassifierResourceWithStreamingResponse:
    def __init__(self, classifier: AsyncClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._classifier.jobs)
