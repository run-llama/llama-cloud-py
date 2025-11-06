# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import APIKeyType
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
from ...types.beta import api_key_api_keys_params, api_key_retrieve_api_keys_params
from ..._base_client import make_request_options
from ...types.api_key import APIKey
from ...types.api_key_type import APIKeyType
from ...types.beta.api_key_retrieve_api_keys_response import APIKeyRetrieveAPIKeysResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def retrieve(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Get an API key by ID.

        Args: api_key_id: The ID of the API key user: Current user db: Database session

        Returns: The API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._get(
            f"/api/v1/beta/api-keys/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def delete(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an API key.

        If the API key belongs to a project, validates user has admin permissions for
        that project. If the API key has no project, validates it belongs to the current
        user.

        Args: api_key_id: The ID of the API key to delete user: Current user db:
        Database session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/beta/api-keys/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def api_keys(
        self,
        *,
        key_type: APIKeyType | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Create a new API key.

        If project_id is specified, validates user has admin permissions for that
        project.

        Args: api_key_create: API key creation data user: Current user db: Database
        session

        Returns: The created API key with the secret key visible in redacted_api_key
        field

        Args:
          project_id: The project ID to associate with the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/api-keys",
            body=maybe_transform(
                {
                    "key_type": key_type,
                    "name": name,
                    "project_id": project_id,
                },
                api_key_api_keys_params.APIKeyAPIKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def retrieve_api_keys(
        self,
        *,
        key_type: Optional[APIKeyType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveAPIKeysResponse:
        """
        List API keys.

        If project_id is provided, validates user has access to that project. If
        project_id is not provided, scopes results to the current user.

        Args: user: Current user db: Database session page_size: Number of items per
        page page_token: Token for pagination name: Filter by API key name project_id:
        Filter by project ID key_type: Filter by key type

        Returns: Paginated response with API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "key_type": key_type,
                        "name": name,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    api_key_retrieve_api_keys_params.APIKeyRetrieveAPIKeysParams,
                ),
            ),
            cast_to=APIKeyRetrieveAPIKeysResponse,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Get an API key by ID.

        Args: api_key_id: The ID of the API key user: Current user db: Database session

        Returns: The API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._get(
            f"/api/v1/beta/api-keys/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def delete(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an API key.

        If the API key belongs to a project, validates user has admin permissions for
        that project. If the API key has no project, validates it belongs to the current
        user.

        Args: api_key_id: The ID of the API key to delete user: Current user db:
        Database session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/beta/api-keys/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def api_keys(
        self,
        *,
        key_type: APIKeyType | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Create a new API key.

        If project_id is specified, validates user has admin permissions for that
        project.

        Args: api_key_create: API key creation data user: Current user db: Database
        session

        Returns: The created API key with the secret key visible in redacted_api_key
        field

        Args:
          project_id: The project ID to associate with the API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/api-keys",
            body=await async_maybe_transform(
                {
                    "key_type": key_type,
                    "name": name,
                    "project_id": project_id,
                },
                api_key_api_keys_params.APIKeyAPIKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def retrieve_api_keys(
        self,
        *,
        key_type: Optional[APIKeyType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveAPIKeysResponse:
        """
        List API keys.

        If project_id is provided, validates user has access to that project. If
        project_id is not provided, scopes results to the current user.

        Args: user: Current user db: Database session page_size: Number of items per
        page page_token: Token for pagination name: Filter by API key name project_id:
        Filter by project ID key_type: Filter by key type

        Returns: Paginated response with API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "key_type": key_type,
                        "name": name,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    api_key_retrieve_api_keys_params.APIKeyRetrieveAPIKeysParams,
                ),
            ),
            cast_to=APIKeyRetrieveAPIKeysResponse,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.retrieve = to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )
        self.api_keys = to_raw_response_wrapper(
            api_keys.api_keys,
        )
        self.retrieve_api_keys = to_raw_response_wrapper(
            api_keys.retrieve_api_keys,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.retrieve = async_to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )
        self.api_keys = async_to_raw_response_wrapper(
            api_keys.api_keys,
        )
        self.retrieve_api_keys = async_to_raw_response_wrapper(
            api_keys.retrieve_api_keys,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.retrieve = to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.api_keys = to_streamed_response_wrapper(
            api_keys.api_keys,
        )
        self.retrieve_api_keys = to_streamed_response_wrapper(
            api_keys.retrieve_api_keys,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.retrieve = async_to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.api_keys = async_to_streamed_response_wrapper(
            api_keys.api_keys,
        )
        self.retrieve_api_keys = async_to_streamed_response_wrapper(
            api_keys.retrieve_api_keys,
        )
