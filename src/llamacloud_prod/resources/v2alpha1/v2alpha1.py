# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .parse import (
    ParseResource,
    AsyncParseResource,
    ParseResourceWithRawResponse,
    AsyncParseResourceWithRawResponse,
    ParseResourceWithStreamingResponse,
    AsyncParseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V2alpha1Resource", "AsyncV2alpha1Resource"]


class V2alpha1Resource(SyncAPIResource):
    @cached_property
    def parse(self) -> ParseResource:
        return ParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2alpha1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return V2alpha1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2alpha1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return V2alpha1ResourceWithStreamingResponse(self)


class AsyncV2alpha1Resource(AsyncAPIResource):
    @cached_property
    def parse(self) -> AsyncParseResource:
        return AsyncParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2alpha1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2alpha1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2alpha1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncV2alpha1ResourceWithStreamingResponse(self)


class V2alpha1ResourceWithRawResponse:
    def __init__(self, v2alpha1: V2alpha1Resource) -> None:
        self._v2alpha1 = v2alpha1

    @cached_property
    def parse(self) -> ParseResourceWithRawResponse:
        return ParseResourceWithRawResponse(self._v2alpha1.parse)


class AsyncV2alpha1ResourceWithRawResponse:
    def __init__(self, v2alpha1: AsyncV2alpha1Resource) -> None:
        self._v2alpha1 = v2alpha1

    @cached_property
    def parse(self) -> AsyncParseResourceWithRawResponse:
        return AsyncParseResourceWithRawResponse(self._v2alpha1.parse)


class V2alpha1ResourceWithStreamingResponse:
    def __init__(self, v2alpha1: V2alpha1Resource) -> None:
        self._v2alpha1 = v2alpha1

    @cached_property
    def parse(self) -> ParseResourceWithStreamingResponse:
        return ParseResourceWithStreamingResponse(self._v2alpha1.parse)


class AsyncV2alpha1ResourceWithStreamingResponse:
    def __init__(self, v2alpha1: AsyncV2alpha1Resource) -> None:
        self._v2alpha1 = v2alpha1

    @cached_property
    def parse(self) -> AsyncParseResourceWithStreamingResponse:
        return AsyncParseResourceWithStreamingResponse(self._v2alpha1.parse)
