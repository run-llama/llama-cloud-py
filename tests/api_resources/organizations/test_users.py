# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.organizations import UserListResponse, UserCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        user = client.organizations.users.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.organizations.users.with_raw_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.organizations.users.with_streaming_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.create(
                organization_id="",
                body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        user = client.organizations.users.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.organizations.users.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.organizations.users.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        user = client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        user = client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.organizations.users.with_raw_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.organizations.users.with_streaming_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                member_user_id="member_user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_user_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                member_user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        user = await async_client.organizations.users.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.organizations.users.with_raw_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.organizations.users.with_streaming_response.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.create(
                organization_id="",
                body=[{"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        user = await async_client.organizations.users.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.organizations.users.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.organizations.users.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        user = await async_client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        user = await async_client.organizations.users.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.organizations.users.with_raw_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.organizations.users.with_streaming_response.delete(
            member_user_id="member_user_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                member_user_id="member_user_id",
                organization_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                member_user_id="",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
