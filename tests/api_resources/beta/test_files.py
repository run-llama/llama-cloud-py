# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import File
from llama_cloud._utils import parse_datetime
from llama_cloud.types.beta import FileQueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        file = client.beta.files.create(
            name="x",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.files.create(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_file_id="external_file_id",
            file_size=0,
            last_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            permission_info={"foo": {"foo": "bar"}},
            resource_info={"foo": {"foo": "bar"}},
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.beta.files.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.beta.files.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        file = client.beta.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.beta.files.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.beta.files.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.beta.files.with_raw_response.delete(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query(self, client: LlamaCloud) -> None:
        file = client.beta.files.query()
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: LlamaCloud) -> None:
        file = client.beta.files.query(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "external_file_id": "external_file_id",
                "file_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "file_name": "file_name",
                "only_manually_uploaded": True,
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            order_by="order_by",
            page_size=0,
            page_token="page_token",
        )
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: LlamaCloud) -> None:
        response = client.beta.files.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: LlamaCloud) -> None:
        with client.beta.files.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileQueryResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.create(
            name="x",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.create(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_file_id="external_file_id",
            file_size=0,
            last_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            permission_info={"foo": {"foo": "bar"}},
            resource_info={"foo": {"foo": "bar"}},
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.files.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.files.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.files.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.files.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.beta.files.with_raw_response.delete(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.query()
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        file = await async_client.beta.files.query(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={
                "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "external_file_id": "external_file_id",
                "file_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "file_name": "file_name",
                "only_manually_uploaded": True,
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            order_by="order_by",
            page_size=0,
            page_token="page_token",
        )
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.files.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileQueryResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.files.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileQueryResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
