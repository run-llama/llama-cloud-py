# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.beta import batch_list_params, batch_create_params, batch_retrieve_params
from ....types.v1.beta.batch import Batch
from ....types.v1.beta.batch_list_response import BatchListResponse
from ....types.v1.beta.batch_retrieve_response import BatchRetrieveResponse
from ....types.v1.llama_parse_parameters_param import LlamaParseParametersParam

__all__ = ["BatchesResource", "AsyncBatchesResource"]


class BatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return BatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return BatchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        input_id: str,
        input_type: str,
        body_project_id: str,
        tool: str,
        organization_id: Optional[str] | Omit = omit,
        query_project_id: Optional[str] | Omit = omit,
        completion_window: int | Omit = omit,
        output_id: Optional[str] | Omit = omit,
        output_type: Optional[str] | Omit = omit,
        tool_data: Optional[LlamaParseParametersParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Batch:
        """Create Batch

        Args:
          external_id: A developer-provided ID for the batch.

        This ID will be returned in the response.

          input_id: The ID of the input file for the batch.

          input_type: The type of input file. Currently only 'datasource' is supported.

          body_project_id: The ID of the project to which the batch belongs

          tool: The tool to be used for all requests in the batch.

          completion_window: The time frame within which the batch should be processed. Currently only 24h is
              supported.

          output_id: The ID of the output file for the batch.

          output_type: The type of output file. Currently only 'datasource' is supported.

          tool_data: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/batches",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "input_id": input_id,
                    "input_type": input_type,
                    "body_project_id": body_project_id,
                    "tool": tool,
                    "completion_window": completion_window,
                    "output_id": output_id,
                    "output_type": output_type,
                    "tool_data": tool_data,
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
                        "query_project_id": query_project_id,
                    },
                    batch_create_params.BatchCreateParams,
                ),
            ),
            cast_to=Batch,
        )

    def retrieve(
        self,
        batch_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchRetrieveResponse:
        """
        Get Batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/api/v1/beta/batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, batch_retrieve_params.BatchRetrieveParams),
            ),
            cast_to=BatchRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List Batches

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/batches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )


class AsyncBatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        input_id: str,
        input_type: str,
        body_project_id: str,
        tool: str,
        organization_id: Optional[str] | Omit = omit,
        query_project_id: Optional[str] | Omit = omit,
        completion_window: int | Omit = omit,
        output_id: Optional[str] | Omit = omit,
        output_type: Optional[str] | Omit = omit,
        tool_data: Optional[LlamaParseParametersParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Batch:
        """Create Batch

        Args:
          external_id: A developer-provided ID for the batch.

        This ID will be returned in the response.

          input_id: The ID of the input file for the batch.

          input_type: The type of input file. Currently only 'datasource' is supported.

          body_project_id: The ID of the project to which the batch belongs

          tool: The tool to be used for all requests in the batch.

          completion_window: The time frame within which the batch should be processed. Currently only 24h is
              supported.

          output_id: The ID of the output file for the batch.

          output_type: The type of output file. Currently only 'datasource' is supported.

          tool_data: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/batches",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "input_id": input_id,
                    "input_type": input_type,
                    "body_project_id": body_project_id,
                    "tool": tool,
                    "completion_window": completion_window,
                    "output_id": output_id,
                    "output_type": output_type,
                    "tool_data": tool_data,
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
                        "query_project_id": query_project_id,
                    },
                    batch_create_params.BatchCreateParams,
                ),
            ),
            cast_to=Batch,
        )

    async def retrieve(
        self,
        batch_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchRetrieveResponse:
        """
        Get Batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/api/v1/beta/batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, batch_retrieve_params.BatchRetrieveParams
                ),
            ),
            cast_to=BatchRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List Batches

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/batches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )


class BatchesResourceWithRawResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_raw_response_wrapper(
            batches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            batches.retrieve,
        )
        self.list = to_raw_response_wrapper(
            batches.list,
        )


class AsyncBatchesResourceWithRawResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_raw_response_wrapper(
            batches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            batches.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            batches.list,
        )


class BatchesResourceWithStreamingResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_streamed_response_wrapper(
            batches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            batches.list,
        )


class AsyncBatchesResourceWithStreamingResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_streamed_response_wrapper(
            batches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            batches.list,
        )
