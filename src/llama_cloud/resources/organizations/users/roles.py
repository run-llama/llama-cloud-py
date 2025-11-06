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
from ....types.organizations.users import role_list_params, role_create_params
from ....types.organizations.users.user_organization_role import UserOrganizationRole

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def create(
        self,
        path_organization_id: str,
        *,
        body_organization_id: str,
        role_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserOrganizationRole:
        """
        Assign a role to a user in an organization.

        Args:
          body_organization_id: The organization's ID.

          role_id: The role's ID.

          user_id: The user's ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_organization_id:
            raise ValueError(
                f"Expected a non-empty value for `path_organization_id` but received {path_organization_id!r}"
            )
        return self._put(
            f"/api/v1/organizations/{path_organization_id}/users/roles",
            body=maybe_transform(
                {
                    "body_organization_id": body_organization_id,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserOrganizationRole,
        )

    def list(
        self,
        organization_id: str,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserOrganizationRole]:
        """
        Get the role of a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/api/v1/organizations/{organization_id}/users/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, role_list_params.RoleListParams),
            ),
            cast_to=UserOrganizationRole,
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    async def create(
        self,
        path_organization_id: str,
        *,
        body_organization_id: str,
        role_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserOrganizationRole:
        """
        Assign a role to a user in an organization.

        Args:
          body_organization_id: The organization's ID.

          role_id: The role's ID.

          user_id: The user's ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_organization_id:
            raise ValueError(
                f"Expected a non-empty value for `path_organization_id` but received {path_organization_id!r}"
            )
        return await self._put(
            f"/api/v1/organizations/{path_organization_id}/users/roles",
            body=await async_maybe_transform(
                {
                    "body_organization_id": body_organization_id,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserOrganizationRole,
        )

    async def list(
        self,
        organization_id: str,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserOrganizationRole]:
        """
        Get the role of a user in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/api/v1/organizations/{organization_id}/users/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, role_list_params.RoleListParams),
            ),
            cast_to=UserOrganizationRole,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_raw_response_wrapper(
            roles.create,
        )
        self.list = to_raw_response_wrapper(
            roles.list,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_raw_response_wrapper(
            roles.create,
        )
        self.list = async_to_raw_response_wrapper(
            roles.list,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_streamed_response_wrapper(
            roles.create,
        )
        self.list = to_streamed_response_wrapper(
            roles.list,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_streamed_response_wrapper(
            roles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
