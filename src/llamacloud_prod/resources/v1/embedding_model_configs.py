# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    embedding_model_config_list_params,
    embedding_model_config_create_params,
    embedding_model_config_delete_params,
    embedding_model_config_update_params,
    embedding_model_config_upsert_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.embedding_model_config import EmbeddingModelConfig
from ...types.v1.embedding_model_config_list_response import EmbeddingModelConfigListResponse

__all__ = ["EmbeddingModelConfigsResource", "AsyncEmbeddingModelConfigsResource"]


class EmbeddingModelConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingModelConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddingModelConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingModelConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return EmbeddingModelConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        embedding_config: embedding_model_config_create_params.EmbeddingConfig,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """
        Create a new embedding model configuration within a specified project.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/embedding-model-configs",
            body=maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_create_params.EmbeddingModelConfigCreateParams,
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
                    embedding_model_config_create_params.EmbeddingModelConfigCreateParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )

    def update(
        self,
        embedding_model_config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        embedding_config: Optional[embedding_model_config_update_params.EmbeddingConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """
        Update an embedding model config by ID.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not embedding_model_config_id:
            raise ValueError(
                f"Expected a non-empty value for `embedding_model_config_id` but received {embedding_model_config_id!r}"
            )
        return self._put(
            f"/api/v1/embedding-model-configs/{embedding_model_config_id}",
            body=maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_update_params.EmbeddingModelConfigUpdateParams,
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
                    embedding_model_config_update_params.EmbeddingModelConfigUpdateParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )

    def list(
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
    ) -> EmbeddingModelConfigListResponse:
        """
        List Embedding Model Configs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/embedding-model-configs",
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
                    embedding_model_config_list_params.EmbeddingModelConfigListParams,
                ),
            ),
            cast_to=EmbeddingModelConfigListResponse,
        )

    def delete(
        self,
        embedding_model_config_id: str,
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
        Delete an embedding model config by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not embedding_model_config_id:
            raise ValueError(
                f"Expected a non-empty value for `embedding_model_config_id` but received {embedding_model_config_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/embedding-model-configs/{embedding_model_config_id}",
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
                    embedding_model_config_delete_params.EmbeddingModelConfigDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def upsert(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        embedding_config: Optional[embedding_model_config_upsert_params.EmbeddingConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """Upserts an embedding model config.

        Updates if an embedding model config with the
        same name and project_id already exists. Otherwise, creates a new embedding
        model config.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/embedding-model-configs",
            body=maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_upsert_params.EmbeddingModelConfigUpsertParams,
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
                    embedding_model_config_upsert_params.EmbeddingModelConfigUpsertParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )


class AsyncEmbeddingModelConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingModelConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingModelConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingModelConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncEmbeddingModelConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        embedding_config: embedding_model_config_create_params.EmbeddingConfig,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """
        Create a new embedding model configuration within a specified project.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/embedding-model-configs",
            body=await async_maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_create_params.EmbeddingModelConfigCreateParams,
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
                    embedding_model_config_create_params.EmbeddingModelConfigCreateParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )

    async def update(
        self,
        embedding_model_config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        embedding_config: Optional[embedding_model_config_update_params.EmbeddingConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """
        Update an embedding model config by ID.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not embedding_model_config_id:
            raise ValueError(
                f"Expected a non-empty value for `embedding_model_config_id` but received {embedding_model_config_id!r}"
            )
        return await self._put(
            f"/api/v1/embedding-model-configs/{embedding_model_config_id}",
            body=await async_maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_update_params.EmbeddingModelConfigUpdateParams,
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
                    embedding_model_config_update_params.EmbeddingModelConfigUpdateParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )

    async def list(
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
    ) -> EmbeddingModelConfigListResponse:
        """
        List Embedding Model Configs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/embedding-model-configs",
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
                    embedding_model_config_list_params.EmbeddingModelConfigListParams,
                ),
            ),
            cast_to=EmbeddingModelConfigListResponse,
        )

    async def delete(
        self,
        embedding_model_config_id: str,
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
        Delete an embedding model config by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not embedding_model_config_id:
            raise ValueError(
                f"Expected a non-empty value for `embedding_model_config_id` but received {embedding_model_config_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/embedding-model-configs/{embedding_model_config_id}",
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
                    embedding_model_config_delete_params.EmbeddingModelConfigDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def upsert(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        embedding_config: Optional[embedding_model_config_upsert_params.EmbeddingConfig] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingModelConfig:
        """Upserts an embedding model config.

        Updates if an embedding model config with the
        same name and project_id already exists. Otherwise, creates a new embedding
        model config.

        Args:
          embedding_config: The embedding configuration for the embedding model config.

          name: The name of the embedding model config.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/embedding-model-configs",
            body=await async_maybe_transform(
                {
                    "embedding_config": embedding_config,
                    "name": name,
                },
                embedding_model_config_upsert_params.EmbeddingModelConfigUpsertParams,
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
                    embedding_model_config_upsert_params.EmbeddingModelConfigUpsertParams,
                ),
            ),
            cast_to=EmbeddingModelConfig,
        )


class EmbeddingModelConfigsResourceWithRawResponse:
    def __init__(self, embedding_model_configs: EmbeddingModelConfigsResource) -> None:
        self._embedding_model_configs = embedding_model_configs

        self.create = to_raw_response_wrapper(
            embedding_model_configs.create,
        )
        self.update = to_raw_response_wrapper(
            embedding_model_configs.update,
        )
        self.list = to_raw_response_wrapper(
            embedding_model_configs.list,
        )
        self.delete = to_raw_response_wrapper(
            embedding_model_configs.delete,
        )
        self.upsert = to_raw_response_wrapper(
            embedding_model_configs.upsert,
        )


class AsyncEmbeddingModelConfigsResourceWithRawResponse:
    def __init__(self, embedding_model_configs: AsyncEmbeddingModelConfigsResource) -> None:
        self._embedding_model_configs = embedding_model_configs

        self.create = async_to_raw_response_wrapper(
            embedding_model_configs.create,
        )
        self.update = async_to_raw_response_wrapper(
            embedding_model_configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            embedding_model_configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            embedding_model_configs.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            embedding_model_configs.upsert,
        )


class EmbeddingModelConfigsResourceWithStreamingResponse:
    def __init__(self, embedding_model_configs: EmbeddingModelConfigsResource) -> None:
        self._embedding_model_configs = embedding_model_configs

        self.create = to_streamed_response_wrapper(
            embedding_model_configs.create,
        )
        self.update = to_streamed_response_wrapper(
            embedding_model_configs.update,
        )
        self.list = to_streamed_response_wrapper(
            embedding_model_configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            embedding_model_configs.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            embedding_model_configs.upsert,
        )


class AsyncEmbeddingModelConfigsResourceWithStreamingResponse:
    def __init__(self, embedding_model_configs: AsyncEmbeddingModelConfigsResource) -> None:
        self._embedding_model_configs = embedding_model_configs

        self.create = async_to_streamed_response_wrapper(
            embedding_model_configs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            embedding_model_configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            embedding_model_configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            embedding_model_configs.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            embedding_model_configs.upsert,
        )
