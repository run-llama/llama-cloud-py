# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1 import (
    EmbeddingModelConfig,
    EmbeddingModelConfigListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddingModelConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.create(
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamacloudProd) -> None:
        response = client.v1.embedding_model_configs.with_raw_response.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamacloudProd) -> None:
        with client.v1.embedding_model_configs.with_streaming_response.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamacloudProd) -> None:
        response = client.v1.embedding_model_configs.with_raw_response.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamacloudProd) -> None:
        with client.v1.embedding_model_configs.with_streaming_response.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamacloudProd) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `embedding_model_config_id` but received ''"
        ):
            client.v1.embedding_model_configs.with_raw_response.update(
                embedding_model_config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.list()
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamacloudProd) -> None:
        response = client.v1.embedding_model_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = response.parse()
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamacloudProd) -> None:
        with client.v1.embedding_model_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = response.parse()
            assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamacloudProd) -> None:
        response = client.v1.embedding_model_configs.with_raw_response.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = response.parse()
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamacloudProd) -> None:
        with client.v1.embedding_model_configs.with_streaming_response.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = response.parse()
            assert embedding_model_config is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamacloudProd) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `embedding_model_config_id` but received ''"
        ):
            client.v1.embedding_model_configs.with_raw_response.delete(
                embedding_model_config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.upsert()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: LlamacloudProd) -> None:
        embedding_model_config = client.v1.embedding_model_configs.upsert(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LlamacloudProd) -> None:
        response = client.v1.embedding_model_configs.with_raw_response.upsert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LlamacloudProd) -> None:
        with client.v1.embedding_model_configs.with_streaming_response.upsert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddingModelConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.create(
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.embedding_model_configs.with_raw_response.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = await response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.embedding_model_configs.with_streaming_response.create(
            embedding_config={"type": "AZURE_EMBEDDING"},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = await response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.embedding_model_configs.with_raw_response.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = await response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.embedding_model_configs.with_streaming_response.update(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = await response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `embedding_model_config_id` but received ''"
        ):
            await async_client.v1.embedding_model_configs.with_raw_response.update(
                embedding_model_config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.list()
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.embedding_model_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = await response.parse()
        assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.embedding_model_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = await response.parse()
            assert_matches_type(EmbeddingModelConfigListResponse, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.embedding_model_configs.with_raw_response.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = await response.parse()
        assert embedding_model_config is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.embedding_model_configs.with_streaming_response.delete(
            embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = await response.parse()
            assert embedding_model_config is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `embedding_model_config_id` but received ''"
        ):
            await async_client.v1.embedding_model_configs.with_raw_response.delete(
                embedding_model_config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.upsert()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        embedding_model_config = await async_client.v1.embedding_model_configs.upsert(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            embedding_config={
                "component": {
                    "additional_kwargs": {"foo": "bar"},
                    "api_base": "api_base",
                    "api_key": "api_key",
                    "api_version": "api_version",
                    "azure_deployment": "azure_deployment",
                    "azure_endpoint": "azure_endpoint",
                    "class_name": "class_name",
                    "default_headers": {"foo": "string"},
                    "dimensions": 0,
                    "embed_batch_size": 1,
                    "max_retries": 0,
                    "model_name": "model_name",
                    "num_workers": 0,
                    "reuse_client": True,
                    "timeout": 0,
                },
                "type": "AZURE_EMBEDDING",
            },
            name="name",
        )
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.embedding_model_configs.with_raw_response.upsert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding_model_config = await response.parse()
        assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.embedding_model_configs.with_streaming_response.upsert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding_model_config = await response.parse()
            assert_matches_type(EmbeddingModelConfig, embedding_model_config, path=["response"])

        assert cast(Any, response.is_closed) is True
