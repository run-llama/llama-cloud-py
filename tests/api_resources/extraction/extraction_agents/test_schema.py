# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.extraction.extraction_agents import (
    SchemaGenerateSchemaResponse,
    SchemaValidateSchemaResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_schema(self, client: LlamaCloud) -> None:
        schema = client.extraction.extraction_agents.schema.generate_schema()
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_schema_with_all_params(self, client: LlamaCloud) -> None:
        schema = client.extraction.extraction_agents.schema.generate_schema(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_schema={"foo": {"foo": "bar"}},
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_schema(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.schema.with_raw_response.generate_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_schema(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.schema.with_streaming_response.generate_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_schema(self, client: LlamaCloud) -> None:
        schema = client.extraction.extraction_agents.schema.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_schema(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.schema.with_raw_response.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_schema(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.schema.with_streaming_response.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSchema:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        schema = await async_client.extraction.extraction_agents.schema.generate_schema()
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_schema_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        schema = await async_client.extraction.extraction_agents.schema.generate_schema(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_schema={"foo": {"foo": "bar"}},
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            prompt="prompt",
        )
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.schema.with_raw_response.generate_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        async with (
            async_client.extraction.extraction_agents.schema.with_streaming_response.generate_schema()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaGenerateSchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        schema = await async_client.extraction.extraction_agents.schema.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.schema.with_raw_response.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.schema.with_streaming_response.validate_schema(
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaValidateSchemaResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True
