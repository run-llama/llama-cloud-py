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
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.extraction import (
    extraction_agent_update_params,
    extraction_agent_retrieve_by_name_params,
    extraction_agent_retrieve_default_params,
    extraction_agent_extraction_agents_params,
    extraction_agent_retrieve_extraction_agents_params,
)
from .....types.v1.extraction.extract_agent import ExtractAgent
from .....types.v1.extraction.extract_config_param import ExtractConfigParam
from .....types.v1.extraction.extraction_agent_retrieve_extraction_agents_response import (
    ExtractionAgentRetrieveExtractionAgentsResponse,
)

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

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return ExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return ExtractionAgentsResourceWithStreamingResponse(self)

    def retrieve(
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

    def extraction_agents(
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
                extraction_agent_extraction_agents_params.ExtractionAgentExtractionAgentsParams,
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
                    extraction_agent_extraction_agents_params.ExtractionAgentExtractionAgentsParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    def retrieve_by_name(
        self,
        name: str,
        *,
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
        Get Extraction Agent By Name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/v1/extraction/extraction-agents/by-name/{name}",
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
                    extraction_agent_retrieve_by_name_params.ExtractionAgentRetrieveByNameParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    def retrieve_default(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """Get or create a default extraction agent for the current project.

        The default
        agent has an empty schema and default configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/extraction/extraction-agents/default",
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
                    extraction_agent_retrieve_default_params.ExtractionAgentRetrieveDefaultParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    def retrieve_extraction_agents(
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
    ) -> ExtractionAgentRetrieveExtractionAgentsResponse:
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
                    extraction_agent_retrieve_extraction_agents_params.ExtractionAgentRetrieveExtractionAgentsParams,
                ),
            ),
            cast_to=ExtractionAgentRetrieveExtractionAgentsResponse,
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

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncExtractionAgentsResourceWithStreamingResponse(self)

    async def retrieve(
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

    async def extraction_agents(
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
                extraction_agent_extraction_agents_params.ExtractionAgentExtractionAgentsParams,
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
                    extraction_agent_extraction_agents_params.ExtractionAgentExtractionAgentsParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    async def retrieve_by_name(
        self,
        name: str,
        *,
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
        Get Extraction Agent By Name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/v1/extraction/extraction-agents/by-name/{name}",
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
                    extraction_agent_retrieve_by_name_params.ExtractionAgentRetrieveByNameParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    async def retrieve_default(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractAgent:
        """Get or create a default extraction agent for the current project.

        The default
        agent has an empty schema and default configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/extraction/extraction-agents/default",
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
                    extraction_agent_retrieve_default_params.ExtractionAgentRetrieveDefaultParams,
                ),
            ),
            cast_to=ExtractAgent,
        )

    async def retrieve_extraction_agents(
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
    ) -> ExtractionAgentRetrieveExtractionAgentsResponse:
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
                    extraction_agent_retrieve_extraction_agents_params.ExtractionAgentRetrieveExtractionAgentsParams,
                ),
            ),
            cast_to=ExtractionAgentRetrieveExtractionAgentsResponse,
        )


class ExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.retrieve = to_raw_response_wrapper(
            extraction_agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            extraction_agents.update,
        )
        self.delete = to_raw_response_wrapper(
            extraction_agents.delete,
        )
        self.extraction_agents = to_raw_response_wrapper(
            extraction_agents.extraction_agents,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            extraction_agents.retrieve_by_name,
        )
        self.retrieve_default = to_raw_response_wrapper(
            extraction_agents.retrieve_default,
        )
        self.retrieve_extraction_agents = to_raw_response_wrapper(
            extraction_agents.retrieve_extraction_agents,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._extraction_agents.schema)


class AsyncExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.retrieve = async_to_raw_response_wrapper(
            extraction_agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            extraction_agents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            extraction_agents.delete,
        )
        self.extraction_agents = async_to_raw_response_wrapper(
            extraction_agents.extraction_agents,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            extraction_agents.retrieve_by_name,
        )
        self.retrieve_default = async_to_raw_response_wrapper(
            extraction_agents.retrieve_default,
        )
        self.retrieve_extraction_agents = async_to_raw_response_wrapper(
            extraction_agents.retrieve_extraction_agents,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._extraction_agents.schema)


class ExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.retrieve = to_streamed_response_wrapper(
            extraction_agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            extraction_agents.update,
        )
        self.delete = to_streamed_response_wrapper(
            extraction_agents.delete,
        )
        self.extraction_agents = to_streamed_response_wrapper(
            extraction_agents.extraction_agents,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            extraction_agents.retrieve_by_name,
        )
        self.retrieve_default = to_streamed_response_wrapper(
            extraction_agents.retrieve_default,
        )
        self.retrieve_extraction_agents = to_streamed_response_wrapper(
            extraction_agents.retrieve_extraction_agents,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._extraction_agents.schema)


class AsyncExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.retrieve = async_to_streamed_response_wrapper(
            extraction_agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            extraction_agents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            extraction_agents.delete,
        )
        self.extraction_agents = async_to_streamed_response_wrapper(
            extraction_agents.extraction_agents,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            extraction_agents.retrieve_by_name,
        )
        self.retrieve_default = async_to_streamed_response_wrapper(
            extraction_agents.retrieve_default,
        )
        self.retrieve_extraction_agents = async_to_streamed_response_wrapper(
            extraction_agents.retrieve_extraction_agents,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._extraction_agents.schema)
