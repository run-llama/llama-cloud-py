# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1 import (
    BaseConnectionValidation,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidateIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_data_sink_connection(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_data_sink_connection_with_all_params(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_data_sink_connection(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_data_sink_connection(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_data_source_connection(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_data_source_connection_with_all_params(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            existing_data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_data_source_connection(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_data_source_connection(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_1(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_1(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
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
            type="AZURE_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_1(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_1(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_2(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_2(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "api_key": "api_key",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "embedding_type": "embedding_type",
                "input_type": "input_type",
                "model_name": "model_name",
                "num_workers": 0,
                "truncate": "truncate",
            },
            type="COHERE_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_2(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_2(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_3(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_3(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "api_base": "api_base",
                "api_key": "api_key",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "model_name": "model_name",
                "num_workers": 0,
                "task_type": "task_type",
                "title": "title",
                "transport": "transport",
            },
            type="GEMINI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_3(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_3(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_4(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_4(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "token": "string",
                "class_name": "class_name",
                "cookies": {"foo": "string"},
                "embed_batch_size": 1,
                "headers": {"foo": "string"},
                "model_name": "model_name",
                "num_workers": 0,
                "pooling": "cls",
                "query_instruction": "query_instruction",
                "task": "task",
                "text_instruction": "text_instruction",
                "timeout": 0,
            },
            type="HUGGINGFACE_API_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_4(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_4(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_5(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_5(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "additional_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "api_key": "api_key",
                "api_version": "api_version",
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
            type="OPENAI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_5(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_5(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_6(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_6(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "client_email": "client_email",
                "location": "location",
                "private_key": "private_key",
                "private_key_id": "private_key_id",
                "project": "project",
                "token_uri": "token_uri",
                "additional_kwargs": {"foo": "bar"},
                "class_name": "class_name",
                "embed_batch_size": 1,
                "embed_mode": "default",
                "model_name": "model_name",
                "num_workers": 0,
            },
            type="VERTEXAI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_6(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_6(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_overload_7(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_embedding_connection_with_all_params_overload_7(self, client: LlamacloudProd) -> None:
        validate_integration = client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "additional_kwargs": {"foo": "bar"},
                "aws_access_key_id": "aws_access_key_id",
                "aws_secret_access_key": "aws_secret_access_key",
                "aws_session_token": "aws_session_token",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "max_retries": 1,
                "model_name": "model_name",
                "num_workers": 0,
                "profile_name": "profile_name",
                "region_name": "region_name",
                "timeout": 0,
            },
            type="BEDROCK_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_embedding_connection_overload_7(self, client: LlamacloudProd) -> None:
        response = client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_embedding_connection_overload_7(self, client: LlamacloudProd) -> None:
        with client.v1.validate_integrations.with_streaming_response.validate_embedding_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidateIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_data_sink_connection(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_data_sink_connection_with_all_params(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_data_sink_connection(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_data_sink_connection(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.validate_integrations.with_streaming_response.validate_data_sink_connection(
            component={"foo": "bar"},
            name="name",
            sink_type="PINECONE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_data_source_connection(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_data_source_connection_with_all_params(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
            existing_data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_metadata={"foo": {"foo": "bar"}},
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_data_source_connection(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_data_source_connection(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.validate_integrations.with_streaming_response.validate_data_source_connection(
            component={"foo": "bar"},
            name="name",
            source_type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_1(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_1(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
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
            type="AZURE_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_1(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_1(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_2(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_2(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "api_key": "api_key",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "embedding_type": "embedding_type",
                "input_type": "input_type",
                "model_name": "model_name",
                "num_workers": 0,
                "truncate": "truncate",
            },
            type="COHERE_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_2(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_2(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_3(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_3(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "api_base": "api_base",
                "api_key": "api_key",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "model_name": "model_name",
                "num_workers": 0,
                "task_type": "task_type",
                "title": "title",
                "transport": "transport",
            },
            type="GEMINI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_3(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_3(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_4(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_4(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "token": "string",
                "class_name": "class_name",
                "cookies": {"foo": "string"},
                "embed_batch_size": 1,
                "headers": {"foo": "string"},
                "model_name": "model_name",
                "num_workers": 0,
                "pooling": "cls",
                "query_instruction": "query_instruction",
                "task": "task",
                "text_instruction": "text_instruction",
                "timeout": 0,
            },
            type="HUGGINGFACE_API_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_4(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_4(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_5(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_5(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "additional_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "api_key": "api_key",
                "api_version": "api_version",
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
            type="OPENAI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_5(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_5(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_6(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_6(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "client_email": "client_email",
                "location": "location",
                "private_key": "private_key",
                "private_key_id": "private_key_id",
                "project": "project",
                "token_uri": "token_uri",
                "additional_kwargs": {"foo": "bar"},
                "class_name": "class_name",
                "embed_batch_size": 1,
                "embed_mode": "default",
                "model_name": "model_name",
                "num_workers": 0,
            },
            type="VERTEXAI_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_6(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_6(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_overload_7(self, async_client: AsyncLlamacloudProd) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_embedding_connection_with_all_params_overload_7(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        validate_integration = await async_client.v1.validate_integrations.validate_embedding_connection(
            pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            component={
                "additional_kwargs": {"foo": "bar"},
                "aws_access_key_id": "aws_access_key_id",
                "aws_secret_access_key": "aws_secret_access_key",
                "aws_session_token": "aws_session_token",
                "class_name": "class_name",
                "embed_batch_size": 1,
                "max_retries": 1,
                "model_name": "model_name",
                "num_workers": 0,
                "profile_name": "profile_name",
                "region_name": "region_name",
                "timeout": 0,
            },
            type="BEDROCK_EMBEDDING",
        )
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_embedding_connection_overload_7(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        response = await async_client.v1.validate_integrations.with_raw_response.validate_embedding_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_integration = await response.parse()
        assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_embedding_connection_overload_7(
        self, async_client: AsyncLlamacloudProd
    ) -> None:
        async with (
            async_client.v1.validate_integrations.with_streaming_response.validate_embedding_connection()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_integration = await response.parse()
            assert_matches_type(BaseConnectionValidation, validate_integration, path=["response"])

        assert cast(Any, response.is_closed) is True
