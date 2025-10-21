# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .batches import (
    BatchesResource,
    AsyncBatchesResource,
    BatchesResourceWithRawResponse,
    AsyncBatchesResourceWithRawResponse,
    BatchesResourceWithStreamingResponse,
    AsyncBatchesResourceWithStreamingResponse,
)
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .agent_data import (
    AgentDataResource,
    AsyncAgentDataResource,
    AgentDataResourceWithRawResponse,
    AsyncAgentDataResourceWithRawResponse,
    AgentDataResourceWithStreamingResponse,
    AsyncAgentDataResourceWithStreamingResponse,
)
from ....types.v1 import beta_retrieve_quota_management_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .parse_configurations import (
    ParseConfigurationsResource,
    AsyncParseConfigurationsResource,
    ParseConfigurationsResourceWithRawResponse,
    AsyncParseConfigurationsResourceWithRawResponse,
    ParseConfigurationsResourceWithStreamingResponse,
    AsyncParseConfigurationsResourceWithStreamingResponse,
)
from .spreadsheet.spreadsheet import (
    SpreadsheetResource,
    AsyncSpreadsheetResource,
    SpreadsheetResourceWithRawResponse,
    AsyncSpreadsheetResourceWithRawResponse,
    SpreadsheetResourceWithStreamingResponse,
    AsyncSpreadsheetResourceWithStreamingResponse,
)
from ....types.v1.beta_retrieve_quota_management_response import BetaRetrieveQuotaManagementResponse

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def batches(self) -> BatchesResource:
        return BatchesResource(self._client)

    @cached_property
    def agent_data(self) -> AgentDataResource:
        return AgentDataResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def parse_configurations(self) -> ParseConfigurationsResource:
        return ParseConfigurationsResource(self._client)

    @cached_property
    def spreadsheet(self) -> SpreadsheetResource:
        return SpreadsheetResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)

    def retrieve_quota_management(
        self,
        *,
        source_id: str,
        source_type: Literal["organization"],
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaRetrieveQuotaManagementResponse:
        """
        Retrieve a paginated list of quota configurations with optional filtering.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/quota-management",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "source_id": source_id,
                        "source_type": source_type,
                        "page": page,
                        "page_size": page_size,
                    },
                    beta_retrieve_quota_management_params.BetaRetrieveQuotaManagementParams,
                ),
            ),
            cast_to=BetaRetrieveQuotaManagementResponse,
        )


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def batches(self) -> AsyncBatchesResource:
        return AsyncBatchesResource(self._client)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResource:
        return AsyncAgentDataResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def parse_configurations(self) -> AsyncParseConfigurationsResource:
        return AsyncParseConfigurationsResource(self._client)

    @cached_property
    def spreadsheet(self) -> AsyncSpreadsheetResource:
        return AsyncSpreadsheetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)

    async def retrieve_quota_management(
        self,
        *,
        source_id: str,
        source_type: Literal["organization"],
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaRetrieveQuotaManagementResponse:
        """
        Retrieve a paginated list of quota configurations with optional filtering.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/quota-management",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "source_id": source_id,
                        "source_type": source_type,
                        "page": page,
                        "page_size": page_size,
                    },
                    beta_retrieve_quota_management_params.BetaRetrieveQuotaManagementParams,
                ),
            ),
            cast_to=BetaRetrieveQuotaManagementResponse,
        )


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.retrieve_quota_management = to_raw_response_wrapper(
            beta.retrieve_quota_management,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._beta.api_keys)

    @cached_property
    def batches(self) -> BatchesResourceWithRawResponse:
        return BatchesResourceWithRawResponse(self._beta.batches)

    @cached_property
    def agent_data(self) -> AgentDataResourceWithRawResponse:
        return AgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._beta.files)

    @cached_property
    def parse_configurations(self) -> ParseConfigurationsResourceWithRawResponse:
        return ParseConfigurationsResourceWithRawResponse(self._beta.parse_configurations)

    @cached_property
    def spreadsheet(self) -> SpreadsheetResourceWithRawResponse:
        return SpreadsheetResourceWithRawResponse(self._beta.spreadsheet)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.retrieve_quota_management = async_to_raw_response_wrapper(
            beta.retrieve_quota_management,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._beta.api_keys)

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithRawResponse:
        return AsyncBatchesResourceWithRawResponse(self._beta.batches)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithRawResponse:
        return AsyncAgentDataResourceWithRawResponse(self._beta.agent_data)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._beta.files)

    @cached_property
    def parse_configurations(self) -> AsyncParseConfigurationsResourceWithRawResponse:
        return AsyncParseConfigurationsResourceWithRawResponse(self._beta.parse_configurations)

    @cached_property
    def spreadsheet(self) -> AsyncSpreadsheetResourceWithRawResponse:
        return AsyncSpreadsheetResourceWithRawResponse(self._beta.spreadsheet)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.retrieve_quota_management = to_streamed_response_wrapper(
            beta.retrieve_quota_management,
        )

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._beta.api_keys)

    @cached_property
    def batches(self) -> BatchesResourceWithStreamingResponse:
        return BatchesResourceWithStreamingResponse(self._beta.batches)

    @cached_property
    def agent_data(self) -> AgentDataResourceWithStreamingResponse:
        return AgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._beta.files)

    @cached_property
    def parse_configurations(self) -> ParseConfigurationsResourceWithStreamingResponse:
        return ParseConfigurationsResourceWithStreamingResponse(self._beta.parse_configurations)

    @cached_property
    def spreadsheet(self) -> SpreadsheetResourceWithStreamingResponse:
        return SpreadsheetResourceWithStreamingResponse(self._beta.spreadsheet)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.retrieve_quota_management = async_to_streamed_response_wrapper(
            beta.retrieve_quota_management,
        )

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._beta.api_keys)

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithStreamingResponse:
        return AsyncBatchesResourceWithStreamingResponse(self._beta.batches)

    @cached_property
    def agent_data(self) -> AsyncAgentDataResourceWithStreamingResponse:
        return AsyncAgentDataResourceWithStreamingResponse(self._beta.agent_data)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._beta.files)

    @cached_property
    def parse_configurations(self) -> AsyncParseConfigurationsResourceWithStreamingResponse:
        return AsyncParseConfigurationsResourceWithStreamingResponse(self._beta.parse_configurations)

    @cached_property
    def spreadsheet(self) -> AsyncSpreadsheetResourceWithStreamingResponse:
        return AsyncSpreadsheetResourceWithStreamingResponse(self._beta.spreadsheet)
