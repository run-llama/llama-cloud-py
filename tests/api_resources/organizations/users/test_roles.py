# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.organizations.users import UserOrganizationRole

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        role = client.organizations.users.roles.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(UserOrganizationRole, role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.organizations.users.roles.with_raw_response.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(UserOrganizationRole, role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.organizations.users.roles.with_streaming_response.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(UserOrganizationRole, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_organization_id` but received ''"):
            client.organizations.users.roles.with_raw_response.create(
                path_organization_id="",
                body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        role = client.organizations.users.roles.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        role = client.organizations.users.roles.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.organizations.users.roles.with_raw_response.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.organizations.users.roles.with_streaming_response.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.roles.with_raw_response.list(
                organization_id="",
            )


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        role = await async_client.organizations.users.roles.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )
        assert_matches_type(UserOrganizationRole, role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.organizations.users.roles.with_raw_response.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(UserOrganizationRole, role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.organizations.users.roles.with_streaming_response.create(
            path_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(UserOrganizationRole, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_organization_id` but received ''"):
            await async_client.organizations.users.roles.with_raw_response.create(
                path_organization_id="",
                body_organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        role = await async_client.organizations.users.roles.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        role = await async_client.organizations.users.roles.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.organizations.users.roles.with_raw_response.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.organizations.users.roles.with_streaming_response.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Optional[UserOrganizationRole], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.roles.with_raw_response.list(
                organization_id="",
            )
