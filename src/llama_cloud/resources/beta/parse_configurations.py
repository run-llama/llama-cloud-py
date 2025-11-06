# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import (
    parse_configuration_query_params,
    parse_configuration_delete_params,
    parse_configuration_update_params,
    parse_configuration_retrieve_params,
    parse_configuration_retrieve_latest_params,
    parse_configuration_parse_configurations_params,
    parse_configuration_update_parse_configurations_params,
    parse_configuration_retrieve_parse_configurations_params,
)
from ..._base_client import make_request_options
from ...types.beta.parse_configuration import ParseConfiguration
from ...types.llama_parse_parameters_param import LlamaParseParametersParam
from ...types.beta.parse_configuration_query_response import ParseConfigurationQueryResponse

__all__ = ["ParseConfigurationsResource", "AsyncParseConfigurationsResource"]


class ParseConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ParseConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ParseConfigurationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Get a parse configuration by ID.

        Args: config_id: The ID of the parse configuration project: Validated project
        from dependency user: Current user db: Database session

        Returns: The parse configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            f"/api/v1/beta/parse-configurations/{config_id}",
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
                    parse_configuration_retrieve_params.ParseConfigurationRetrieveParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parameters: Optional[LlamaParseParametersParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Update a parse configuration.

        Args: config_id: The ID of the parse configuration to update config_update:
        Update data project: Validated project from dependency user: Current user db:
        Database session

        Returns: The updated parse configuration

        Args:
          parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._put(
            f"/api/v1/beta/parse-configurations/{config_id}",
            body=maybe_transform(
                {"parameters": parameters}, parse_configuration_update_params.ParseConfigurationUpdateParams
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
                    parse_configuration_update_params.ParseConfigurationUpdateParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    def delete(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a parse configuration.

        Args: config_id: The ID of the parse configuration to delete project: Validated
        project from dependency user: Current user db: Database session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/beta/parse-configurations/{config_id}",
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
                    parse_configuration_delete_params.ParseConfigurationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def parse_configurations(
        self,
        *,
        name: str,
        parameters: LlamaParseParametersParam,
        version: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Create a new parse configuration.

        Args: config_create: Parse configuration creation data project: Validated
        project from dependency user: Current user db: Database session

        Returns: The created parse configuration

        Args:
          name: Name of the parse configuration

          parameters: LlamaParseParameters configuration

          version: Version of the configuration

          creator: Creator of the configuration

          source_id: ID of the source

          source_type: Type of the source (e.g., 'project')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/parse-configurations",
            body=maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                    "version": version,
                    "creator": creator,
                    "source_id": source_id,
                    "source_type": source_type,
                },
                parse_configuration_parse_configurations_params.ParseConfigurationParseConfigurationsParams,
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
                    parse_configuration_parse_configurations_params.ParseConfigurationParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    def query(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        filter: Optional[parse_configuration_query_params.Filter] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfigurationQueryResponse:
        """
        Query parse configurations with filtering and pagination.

        Args: query_request: Query request with filters and pagination project:
        Validated project from dependency user: Current user db: Database session

        Returns: Paginated response with parse configurations

        Args:
          filter: Filter parameters for parse configuration queries.

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/parse-configurations/query",
            body=maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                parse_configuration_query_params.ParseConfigurationQueryParams,
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
                    parse_configuration_query_params.ParseConfigurationQueryParams,
                ),
            ),
            cast_to=ParseConfigurationQueryResponse,
        )

    def retrieve_latest(
        self,
        *,
        creator: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ParseConfiguration]:
        """
        Get the latest parse configuration for the current project.

        Args: project: Validated project from dependency user: Current user db: Database
        session creator: Optional creator filter

        Returns: The latest parse configuration or None if not found

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/parse-configurations/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "creator": creator,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parse_configuration_retrieve_latest_params.ParseConfigurationRetrieveLatestParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    def retrieve_parse_configurations(
        self,
        *,
        creator: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfigurationQueryResponse:
        """
        List parse configurations for the current project.

        Args: project: Validated project from dependency user: Current user db: Database
        session page_size: Number of items per page page_token: Token for pagination
        name: Filter by configuration name creator: Filter by creator version: Filter by
        version

        Returns: Paginated response with parse configurations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/parse-configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "creator": creator,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "version": version,
                    },
                    parse_configuration_retrieve_parse_configurations_params.ParseConfigurationRetrieveParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfigurationQueryResponse,
        )

    def update_parse_configurations(
        self,
        *,
        name: str,
        parameters: LlamaParseParametersParam,
        version: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Create or update a parse configuration by name.

        Args: config_create: Parse configuration creation data project: Validated
        project from dependency user: Current user db: Database session

        Returns: The created or updated parse configuration

        Args:
          name: Name of the parse configuration

          parameters: LlamaParseParameters configuration

          version: Version of the configuration

          creator: Creator of the configuration

          source_id: ID of the source

          source_type: Type of the source (e.g., 'project')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/beta/parse-configurations",
            body=maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                    "version": version,
                    "creator": creator,
                    "source_id": source_id,
                    "source_type": source_type,
                },
                parse_configuration_update_parse_configurations_params.ParseConfigurationUpdateParseConfigurationsParams,
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
                    parse_configuration_update_parse_configurations_params.ParseConfigurationUpdateParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )


class AsyncParseConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncParseConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncParseConfigurationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Get a parse configuration by ID.

        Args: config_id: The ID of the parse configuration project: Validated project
        from dependency user: Current user db: Database session

        Returns: The parse configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            f"/api/v1/beta/parse-configurations/{config_id}",
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
                    parse_configuration_retrieve_params.ParseConfigurationRetrieveParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    async def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parameters: Optional[LlamaParseParametersParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Update a parse configuration.

        Args: config_id: The ID of the parse configuration to update config_update:
        Update data project: Validated project from dependency user: Current user db:
        Database session

        Returns: The updated parse configuration

        Args:
          parameters: Settings that can be configured for how to use LlamaParse to parse files within
              a LlamaCloud pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._put(
            f"/api/v1/beta/parse-configurations/{config_id}",
            body=await async_maybe_transform(
                {"parameters": parameters}, parse_configuration_update_params.ParseConfigurationUpdateParams
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
                    parse_configuration_update_params.ParseConfigurationUpdateParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    async def delete(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a parse configuration.

        Args: config_id: The ID of the parse configuration to delete project: Validated
        project from dependency user: Current user db: Database session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/beta/parse-configurations/{config_id}",
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
                    parse_configuration_delete_params.ParseConfigurationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def parse_configurations(
        self,
        *,
        name: str,
        parameters: LlamaParseParametersParam,
        version: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Create a new parse configuration.

        Args: config_create: Parse configuration creation data project: Validated
        project from dependency user: Current user db: Database session

        Returns: The created parse configuration

        Args:
          name: Name of the parse configuration

          parameters: LlamaParseParameters configuration

          version: Version of the configuration

          creator: Creator of the configuration

          source_id: ID of the source

          source_type: Type of the source (e.g., 'project')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/parse-configurations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                    "version": version,
                    "creator": creator,
                    "source_id": source_id,
                    "source_type": source_type,
                },
                parse_configuration_parse_configurations_params.ParseConfigurationParseConfigurationsParams,
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
                    parse_configuration_parse_configurations_params.ParseConfigurationParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    async def query(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        filter: Optional[parse_configuration_query_params.Filter] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfigurationQueryResponse:
        """
        Query parse configurations with filtering and pagination.

        Args: query_request: Query request with filters and pagination project:
        Validated project from dependency user: Current user db: Database session

        Returns: Paginated response with parse configurations

        Args:
          filter: Filter parameters for parse configuration queries.

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/parse-configurations/query",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                parse_configuration_query_params.ParseConfigurationQueryParams,
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
                    parse_configuration_query_params.ParseConfigurationQueryParams,
                ),
            ),
            cast_to=ParseConfigurationQueryResponse,
        )

    async def retrieve_latest(
        self,
        *,
        creator: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ParseConfiguration]:
        """
        Get the latest parse configuration for the current project.

        Args: project: Validated project from dependency user: Current user db: Database
        session creator: Optional creator filter

        Returns: The latest parse configuration or None if not found

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/parse-configurations/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "creator": creator,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parse_configuration_retrieve_latest_params.ParseConfigurationRetrieveLatestParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )

    async def retrieve_parse_configurations(
        self,
        *,
        creator: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfigurationQueryResponse:
        """
        List parse configurations for the current project.

        Args: project: Validated project from dependency user: Current user db: Database
        session page_size: Number of items per page page_token: Token for pagination
        name: Filter by configuration name creator: Filter by creator version: Filter by
        version

        Returns: Paginated response with parse configurations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/parse-configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "creator": creator,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "version": version,
                    },
                    parse_configuration_retrieve_parse_configurations_params.ParseConfigurationRetrieveParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfigurationQueryResponse,
        )

    async def update_parse_configurations(
        self,
        *,
        name: str,
        parameters: LlamaParseParametersParam,
        version: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        source_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseConfiguration:
        """
        Create or update a parse configuration by name.

        Args: config_create: Parse configuration creation data project: Validated
        project from dependency user: Current user db: Database session

        Returns: The created or updated parse configuration

        Args:
          name: Name of the parse configuration

          parameters: LlamaParseParameters configuration

          version: Version of the configuration

          creator: Creator of the configuration

          source_id: ID of the source

          source_type: Type of the source (e.g., 'project')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/beta/parse-configurations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                    "version": version,
                    "creator": creator,
                    "source_id": source_id,
                    "source_type": source_type,
                },
                parse_configuration_update_parse_configurations_params.ParseConfigurationUpdateParseConfigurationsParams,
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
                    parse_configuration_update_parse_configurations_params.ParseConfigurationUpdateParseConfigurationsParams,
                ),
            ),
            cast_to=ParseConfiguration,
        )


class ParseConfigurationsResourceWithRawResponse:
    def __init__(self, parse_configurations: ParseConfigurationsResource) -> None:
        self._parse_configurations = parse_configurations

        self.retrieve = to_raw_response_wrapper(
            parse_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            parse_configurations.update,
        )
        self.delete = to_raw_response_wrapper(
            parse_configurations.delete,
        )
        self.parse_configurations = to_raw_response_wrapper(
            parse_configurations.parse_configurations,
        )
        self.query = to_raw_response_wrapper(
            parse_configurations.query,
        )
        self.retrieve_latest = to_raw_response_wrapper(
            parse_configurations.retrieve_latest,
        )
        self.retrieve_parse_configurations = to_raw_response_wrapper(
            parse_configurations.retrieve_parse_configurations,
        )
        self.update_parse_configurations = to_raw_response_wrapper(
            parse_configurations.update_parse_configurations,
        )


class AsyncParseConfigurationsResourceWithRawResponse:
    def __init__(self, parse_configurations: AsyncParseConfigurationsResource) -> None:
        self._parse_configurations = parse_configurations

        self.retrieve = async_to_raw_response_wrapper(
            parse_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            parse_configurations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            parse_configurations.delete,
        )
        self.parse_configurations = async_to_raw_response_wrapper(
            parse_configurations.parse_configurations,
        )
        self.query = async_to_raw_response_wrapper(
            parse_configurations.query,
        )
        self.retrieve_latest = async_to_raw_response_wrapper(
            parse_configurations.retrieve_latest,
        )
        self.retrieve_parse_configurations = async_to_raw_response_wrapper(
            parse_configurations.retrieve_parse_configurations,
        )
        self.update_parse_configurations = async_to_raw_response_wrapper(
            parse_configurations.update_parse_configurations,
        )


class ParseConfigurationsResourceWithStreamingResponse:
    def __init__(self, parse_configurations: ParseConfigurationsResource) -> None:
        self._parse_configurations = parse_configurations

        self.retrieve = to_streamed_response_wrapper(
            parse_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            parse_configurations.update,
        )
        self.delete = to_streamed_response_wrapper(
            parse_configurations.delete,
        )
        self.parse_configurations = to_streamed_response_wrapper(
            parse_configurations.parse_configurations,
        )
        self.query = to_streamed_response_wrapper(
            parse_configurations.query,
        )
        self.retrieve_latest = to_streamed_response_wrapper(
            parse_configurations.retrieve_latest,
        )
        self.retrieve_parse_configurations = to_streamed_response_wrapper(
            parse_configurations.retrieve_parse_configurations,
        )
        self.update_parse_configurations = to_streamed_response_wrapper(
            parse_configurations.update_parse_configurations,
        )


class AsyncParseConfigurationsResourceWithStreamingResponse:
    def __init__(self, parse_configurations: AsyncParseConfigurationsResource) -> None:
        self._parse_configurations = parse_configurations

        self.retrieve = async_to_streamed_response_wrapper(
            parse_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            parse_configurations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            parse_configurations.delete,
        )
        self.parse_configurations = async_to_streamed_response_wrapper(
            parse_configurations.parse_configurations,
        )
        self.query = async_to_streamed_response_wrapper(
            parse_configurations.query,
        )
        self.retrieve_latest = async_to_streamed_response_wrapper(
            parse_configurations.retrieve_latest,
        )
        self.retrieve_parse_configurations = async_to_streamed_response_wrapper(
            parse_configurations.retrieve_parse_configurations,
        )
        self.update_parse_configurations = async_to_streamed_response_wrapper(
            parse_configurations.update_parse_configurations,
        )
