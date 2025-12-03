# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
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
from ....types.extraction import (
    extraction_agent_list_params,
    extraction_agent_create_params,
    extraction_agent_update_params,
)
from ....types.extraction.extract_agent import ExtractAgent
from ....types.extraction.extract_config_param import ExtractConfigParam
from ....types.extraction.extraction_agent_list_response import ExtractionAgentListResponse

__all__ = ["ExtractionAgentsResource", "AsyncExtractionAgentsResource"]


class ExtractionAgentsResource(SyncAPIResource):
    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractionAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ExtractionAgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Create Extraction Agent

        Args:
          config: The configuration parameters for the extraction agent.

          data_schema: The schema of the data.

          name: The name of the extraction schema

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/extraction-agents",
            body=maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                    "name": name,
                },
                extraction_agent_create_params.ExtractionAgentCreateParams,
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
                    extraction_agent_create_params.ExtractionAgentCreateParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    def update(
        self,
        extraction_agent_id: str,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Update Extraction Agent

        Args:
          config: The configuration parameters for the extraction agent.

          data_schema: The schema of the data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return self._put(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                },
                extraction_agent_update_params.ExtractionAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractAgent,
        )

    def list(
        self,
        *,
        include_default: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionAgentListResponse:
        """
        List Extraction Agents

        Args:
          include_default: Whether to include default agents in the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/extraction/extraction-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_default": include_default,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    extraction_agent_list_params.ExtractionAgentListParams,
                ),
            ),
            cast_to=ExtractionAgentListResponse,
        )

    def delete(
        self,
        extraction_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Extraction Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return self._delete(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        extraction_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Get Extraction Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return self._get(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractAgent,
        )


class AsyncExtractionAgentsResource(AsyncAPIResource):
    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractionAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncExtractionAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Create Extraction Agent

        Args:
          config: The configuration parameters for the extraction agent.

          data_schema: The schema of the data.

          name: The name of the extraction schema

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/extraction-agents",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                    "name": name,
                },
                extraction_agent_create_params.ExtractionAgentCreateParams,
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
                    extraction_agent_create_params.ExtractionAgentCreateParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    async def update(
        self,
        extraction_agent_id: str,
        *,
        config: ExtractConfigParam,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Update Extraction Agent

        Args:
          config: The configuration parameters for the extraction agent.

          data_schema: The schema of the data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return await self._put(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "data_schema": data_schema,
                },
                extraction_agent_update_params.ExtractionAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractAgent,
        )

    async def list(
        self,
        *,
        include_default: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionAgentListResponse:
        """
        List Extraction Agents

        Args:
          include_default: Whether to include default agents in the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/extraction/extraction-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_default": include_default,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    extraction_agent_list_params.ExtractionAgentListParams,
                ),
            ),
            cast_to=ExtractionAgentListResponse,
        )

    async def delete(
        self,
        extraction_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Extraction Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return await self._delete(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        extraction_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """
        Get Extraction Agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not extraction_agent_id:
            raise ValueError(
                f"Expected a non-empty value for `extraction_agent_id` but received {extraction_agent_id!r}"
            )
        return await self._get(
            f"/api/v1/extraction/extraction-agents/{extraction_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractAgent,
        )


class ExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.create = to_raw_response_wrapper(
            extraction_agents.create,
        )
        self.update = to_raw_response_wrapper(
            extraction_agents.update,
        )
        self.list = to_raw_response_wrapper(
            extraction_agents.list,
        )
        self.delete = to_raw_response_wrapper(
            extraction_agents.delete,
        )
        self.get = to_raw_response_wrapper(
            extraction_agents.get,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._extraction_agents.schema)


class AsyncExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.create = async_to_raw_response_wrapper(
            extraction_agents.create,
        )
        self.update = async_to_raw_response_wrapper(
            extraction_agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            extraction_agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extraction_agents.delete,
        )
        self.get = async_to_raw_response_wrapper(
            extraction_agents.get,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._extraction_agents.schema)


class ExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.create = to_streamed_response_wrapper(
            extraction_agents.create,
        )
        self.update = to_streamed_response_wrapper(
            extraction_agents.update,
        )
        self.list = to_streamed_response_wrapper(
            extraction_agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            extraction_agents.delete,
        )
        self.get = to_streamed_response_wrapper(
            extraction_agents.get,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._extraction_agents.schema)


class AsyncExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.create = async_to_streamed_response_wrapper(
            extraction_agents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            extraction_agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            extraction_agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extraction_agents.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            extraction_agents.get,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._extraction_agents.schema)
