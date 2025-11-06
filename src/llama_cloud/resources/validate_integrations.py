# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    ConfigurableDataSinkNames,
    ConfigurableDataSourceNames,
    validate_integration_validate_data_sink_connection_params,
    validate_integration_validate_embedding_connection_params,
    validate_integration_validate_data_source_connection_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.base_connection_validation import BaseConnectionValidation
from ..types.configurable_data_sink_names import ConfigurableDataSinkNames
from ..types.configurable_data_source_names import ConfigurableDataSourceNames

__all__ = ["ValidateIntegrationsResource", "AsyncValidateIntegrationsResource"]


class ValidateIntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidateIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ValidateIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ValidateIntegrationsResourceWithStreamingResponse(self)

    def validate_data_sink_connection(
        self,
        *,
        component: validate_integration_validate_data_sink_connection_params.Component,
        name: str,
        sink_type: ConfigurableDataSinkNames,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate a data sink connection.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/validate-integrations/validate-data-sink-connection",
            body=maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "sink_type": sink_type,
                },
                validate_integration_validate_data_sink_connection_params.ValidateIntegrationValidateDataSinkConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseConnectionValidation,
        )

    def validate_data_source_connection(
        self,
        *,
        component: validate_integration_validate_data_source_connection_params.Component,
        name: str,
        source_type: ConfigurableDataSourceNames,
        existing_data_source_id: Optional[str] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate a data source connection.

        Args:
          component: Component that implements the data source

          name: The name of the data source.

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/validate-integrations/validate-data-source-connection",
            body=maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "source_type": source_type,
                    "custom_metadata": custom_metadata,
                },
                validate_integration_validate_data_source_connection_params.ValidateIntegrationValidateDataSourceConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"existing_data_source_id": existing_data_source_id},
                    validate_integration_validate_data_source_connection_params.ValidateIntegrationValidateDataSourceConnectionParams,
                ),
            ),
            cast_to=BaseConnectionValidation,
        )

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.AzureOpenAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["AZURE_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Azure OpenAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.CohereEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["COHERE_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Cohere embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.GeminiEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["GEMINI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Gemini embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.HuggingFaceInferenceAPIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["HUGGINGFACE_API_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the HuggingFace Inference API embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.OpenAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["OPENAI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the OpenAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.VertexAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["VERTEXAI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the VertexAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.BedrockEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["BEDROCK_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Bedrock embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.AzureOpenAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.CohereEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.GeminiEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.HuggingFaceInferenceAPIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.OpenAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.VertexAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.BedrockEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["AZURE_EMBEDDING"]
        | Literal["COHERE_EMBEDDING"]
        | Literal["GEMINI_EMBEDDING"]
        | Literal["HUGGINGFACE_API_EMBEDDING"]
        | Literal["OPENAI_EMBEDDING"]
        | Literal["VERTEXAI_EMBEDDING"]
        | Literal["BEDROCK_EMBEDDING"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        return self._post(
            "/api/v1/validate-integrations/validate-embedding-connection",
            body=maybe_transform(
                {
                    "component": component,
                    "type": type,
                },
                validate_integration_validate_embedding_connection_params.ValidateIntegrationValidateEmbeddingConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pipeline_id": pipeline_id},
                    validate_integration_validate_embedding_connection_params.ValidateIntegrationValidateEmbeddingConnectionParams,
                ),
            ),
            cast_to=BaseConnectionValidation,
        )


class AsyncValidateIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidateIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncValidateIntegrationsResourceWithStreamingResponse(self)

    async def validate_data_sink_connection(
        self,
        *,
        component: validate_integration_validate_data_sink_connection_params.Component,
        name: str,
        sink_type: ConfigurableDataSinkNames,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate a data sink connection.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/validate-integrations/validate-data-sink-connection",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "sink_type": sink_type,
                },
                validate_integration_validate_data_sink_connection_params.ValidateIntegrationValidateDataSinkConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseConnectionValidation,
        )

    async def validate_data_source_connection(
        self,
        *,
        component: validate_integration_validate_data_source_connection_params.Component,
        name: str,
        source_type: ConfigurableDataSourceNames,
        existing_data_source_id: Optional[str] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate a data source connection.

        Args:
          component: Component that implements the data source

          name: The name of the data source.

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/validate-integrations/validate-data-source-connection",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "source_type": source_type,
                    "custom_metadata": custom_metadata,
                },
                validate_integration_validate_data_source_connection_params.ValidateIntegrationValidateDataSourceConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"existing_data_source_id": existing_data_source_id},
                    validate_integration_validate_data_source_connection_params.ValidateIntegrationValidateDataSourceConnectionParams,
                ),
            ),
            cast_to=BaseConnectionValidation,
        )

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.AzureOpenAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["AZURE_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Azure OpenAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.CohereEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["COHERE_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Cohere embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.GeminiEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["GEMINI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Gemini embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.HuggingFaceInferenceAPIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["HUGGINGFACE_API_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the HuggingFace Inference API embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.OpenAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["OPENAI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the OpenAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.VertexAIEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["VERTEXAI_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the VertexAI embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.BedrockEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["BEDROCK_EMBEDDING"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        """
        Validate an embedding connection.

        Args: embedding_config: The embedding configuration to validate. pipeline_id: If
        provided, the embedding connection will be validated for the pipeline. user: The
        user to validate the embedding connection for. db: The database session.

        Returns: A BaseConnectionValidation object indicating the result of the
        validation.

        Args:
          component: Configuration for the Bedrock embedding model.

          type: Type of the embedding model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def validate_embedding_connection(
        self,
        *,
        pipeline_id: Optional[str] | Omit = omit,
        component: validate_integration_validate_embedding_connection_params.AzureOpenAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.CohereEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.GeminiEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.HuggingFaceInferenceAPIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.OpenAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.VertexAIEmbeddingConfigComponent
        | validate_integration_validate_embedding_connection_params.BedrockEmbeddingConfigComponent
        | Omit = omit,
        type: Literal["AZURE_EMBEDDING"]
        | Literal["COHERE_EMBEDDING"]
        | Literal["GEMINI_EMBEDDING"]
        | Literal["HUGGINGFACE_API_EMBEDDING"]
        | Literal["OPENAI_EMBEDDING"]
        | Literal["VERTEXAI_EMBEDDING"]
        | Literal["BEDROCK_EMBEDDING"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseConnectionValidation:
        return await self._post(
            "/api/v1/validate-integrations/validate-embedding-connection",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "type": type,
                },
                validate_integration_validate_embedding_connection_params.ValidateIntegrationValidateEmbeddingConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pipeline_id": pipeline_id},
                    validate_integration_validate_embedding_connection_params.ValidateIntegrationValidateEmbeddingConnectionParams,
                ),
            ),
            cast_to=BaseConnectionValidation,
        )


class ValidateIntegrationsResourceWithRawResponse:
    def __init__(self, validate_integrations: ValidateIntegrationsResource) -> None:
        self._validate_integrations = validate_integrations

        self.validate_data_sink_connection = to_raw_response_wrapper(
            validate_integrations.validate_data_sink_connection,
        )
        self.validate_data_source_connection = to_raw_response_wrapper(
            validate_integrations.validate_data_source_connection,
        )
        self.validate_embedding_connection = to_raw_response_wrapper(
            validate_integrations.validate_embedding_connection,
        )


class AsyncValidateIntegrationsResourceWithRawResponse:
    def __init__(self, validate_integrations: AsyncValidateIntegrationsResource) -> None:
        self._validate_integrations = validate_integrations

        self.validate_data_sink_connection = async_to_raw_response_wrapper(
            validate_integrations.validate_data_sink_connection,
        )
        self.validate_data_source_connection = async_to_raw_response_wrapper(
            validate_integrations.validate_data_source_connection,
        )
        self.validate_embedding_connection = async_to_raw_response_wrapper(
            validate_integrations.validate_embedding_connection,
        )


class ValidateIntegrationsResourceWithStreamingResponse:
    def __init__(self, validate_integrations: ValidateIntegrationsResource) -> None:
        self._validate_integrations = validate_integrations

        self.validate_data_sink_connection = to_streamed_response_wrapper(
            validate_integrations.validate_data_sink_connection,
        )
        self.validate_data_source_connection = to_streamed_response_wrapper(
            validate_integrations.validate_data_source_connection,
        )
        self.validate_embedding_connection = to_streamed_response_wrapper(
            validate_integrations.validate_embedding_connection,
        )


class AsyncValidateIntegrationsResourceWithStreamingResponse:
    def __init__(self, validate_integrations: AsyncValidateIntegrationsResource) -> None:
        self._validate_integrations = validate_integrations

        self.validate_data_sink_connection = async_to_streamed_response_wrapper(
            validate_integrations.validate_data_sink_connection,
        )
        self.validate_data_source_connection = async_to_streamed_response_wrapper(
            validate_integrations.validate_data_source_connection,
        )
        self.validate_embedding_connection = async_to_streamed_response_wrapper(
            validate_integrations.validate_embedding_connection,
        )
