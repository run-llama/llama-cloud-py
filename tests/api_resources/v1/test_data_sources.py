# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1 import (
    DataSource,
    DataSourceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.v1.data_sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
            component={"foo": "bar"},
            custom_metadata={"foo": {"foo": "bar"}},
            name="name",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.v1.data_sources.with_raw_response.update(
                data_source_id="",
                source_type="S3",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.list()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert data_source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert data_source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert data_source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.v1.data_sources.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: LlamacloudProd) -> None:
        data_source = client.v1.data_sources.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LlamacloudProd) -> None:
        response = client.v1.data_sources.with_raw_response.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LlamacloudProd) -> None:
        with client.v1.data_sources.with_streaming_response.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.create(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.v1.data_sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
            component={"foo": "bar"},
            custom_metadata={"foo": {"foo": "bar"}},
            name="name",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.v1.data_sources.with_raw_response.update(
                data_source_id="",
                source_type="S3",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.list()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceListResponse, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceListResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert data_source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert data_source is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert data_source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.v1.data_sources.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        data_source = await async_client.v1.data_sources.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.data_sources.with_raw_response.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSource, data_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.data_sources.with_streaming_response.upsert(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSource, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True
