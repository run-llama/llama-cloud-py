# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

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
from ....types.extraction.extraction_agents import schema_generate_schema_params, schema_validate_schema_params
from ....types.extraction.extraction_agents.schema_generate_schema_response import SchemaGenerateSchemaResponse
from ....types.extraction.extraction_agents.schema_validate_schema_response import SchemaValidateSchemaResponse

__all__ = ["SchemaResource", "AsyncSchemaResource"]


class SchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return SchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return SchemaResourceWithStreamingResponse(self)

    def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaGenerateSchemaResponse:
        """
        Generates or refines an extraction agent's schema definition from a file,
        natural language prompt, or existing schema.

        Args:
          data_schema: Optional schema to validate, refine, or extend during generation

          file_id: Optional file ID to analyze for schema generation

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/extraction-agents/schema/generate",
            body=maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "prompt": prompt,
                },
                schema_generate_schema_params.SchemaGenerateSchemaParams,
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
                    schema_generate_schema_params.SchemaGenerateSchemaParams,
                ),
            ),
            cast_to=SchemaGenerateSchemaResponse,
        )

    def validate_schema(
        self,
        *,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaValidateSchemaResponse:
        """Validates an extraction agent's schema definition.

        Returns the normalized and
        validated schema if valid, otherwise raises an HTTP 400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/extraction/extraction-agents/schema/validation",
            body=maybe_transform(
                {"data_schema": data_schema}, schema_validate_schema_params.SchemaValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaValidateSchemaResponse,
        )


class AsyncSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncSchemaResourceWithStreamingResponse(self)

    async def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaGenerateSchemaResponse:
        """
        Generates or refines an extraction agent's schema definition from a file,
        natural language prompt, or existing schema.

        Args:
          data_schema: Optional schema to validate, refine, or extend during generation

          file_id: Optional file ID to analyze for schema generation

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/extraction-agents/schema/generate",
            body=await async_maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "prompt": prompt,
                },
                schema_generate_schema_params.SchemaGenerateSchemaParams,
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
                    schema_generate_schema_params.SchemaGenerateSchemaParams,
                ),
            ),
            cast_to=SchemaGenerateSchemaResponse,
        )

    async def validate_schema(
        self,
        *,
        data_schema: Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaValidateSchemaResponse:
        """Validates an extraction agent's schema definition.

        Returns the normalized and
        validated schema if valid, otherwise raises an HTTP 400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/extraction/extraction-agents/schema/validation",
            body=await async_maybe_transform(
                {"data_schema": data_schema}, schema_validate_schema_params.SchemaValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaValidateSchemaResponse,
        )


class SchemaResourceWithRawResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.generate_schema = to_raw_response_wrapper(
            schema.generate_schema,
        )
        self.validate_schema = to_raw_response_wrapper(
            schema.validate_schema,
        )


class AsyncSchemaResourceWithRawResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.generate_schema = async_to_raw_response_wrapper(
            schema.generate_schema,
        )
        self.validate_schema = async_to_raw_response_wrapper(
            schema.validate_schema,
        )


class SchemaResourceWithStreamingResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.generate_schema = to_streamed_response_wrapper(
            schema.generate_schema,
        )
        self.validate_schema = to_streamed_response_wrapper(
            schema.validate_schema,
        )


class AsyncSchemaResourceWithStreamingResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.generate_schema = async_to_streamed_response_wrapper(
            schema.generate_schema,
        )
        self.validate_schema = async_to_streamed_response_wrapper(
            schema.validate_schema,
        )
