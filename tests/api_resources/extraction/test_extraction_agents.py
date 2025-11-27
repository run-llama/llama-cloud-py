# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.extraction import (
    ExtractAgent,
    ExtractionAgentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtractionAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.create(
            config={
                "chunk_mode": "PAGE",
                "citation_bbox": True,
                "cite_sources": True,
                "confidence_scores": True,
                "extract_model": "openai-gpt-4-1",
                "extraction_mode": "FAST",
                "extraction_target": "PER_DOC",
                "high_resolution_mode": True,
                "invalidate_cache": True,
                "multimodal_fast_mode": True,
                "num_pages_context": 1,
                "page_range": "page_range",
                "parse_model": "openai-gpt-4o",
                "priority": "low",
                "system_prompt": "system_prompt",
                "use_reasoning": True,
            },
            data_schema={"foo": {"foo": "bar"}},
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.with_raw_response.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.with_streaming_response.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "chunk_mode": "PAGE",
                "citation_bbox": True,
                "cite_sources": True,
                "confidence_scores": True,
                "extract_model": "openai-gpt-4-1",
                "extraction_mode": "FAST",
                "extraction_target": "PER_DOC",
                "high_resolution_mode": True,
                "invalidate_cache": True,
                "multimodal_fast_mode": True,
                "num_pages_context": 1,
                "page_range": "page_range",
                "parse_model": "openai-gpt-4o",
                "priority": "low",
                "system_prompt": "system_prompt",
                "use_reasoning": True,
            },
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.with_raw_response.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.with_streaming_response.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            client.extraction.extraction_agents.with_raw_response.update(
                extraction_agent_id="",
                config={},
                data_schema={"foo": {"foo": "bar"}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.list()
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.list(
            include_default=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = response.parse()
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = response.parse()
            assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = response.parse()
        assert_matches_type(object, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = response.parse()
            assert_matches_type(object, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            client.extraction.extraction_agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        extraction_agent = client.extraction.extraction_agents.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.extraction.extraction_agents.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.extraction.extraction_agents.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            client.extraction.extraction_agents.with_raw_response.get(
                "",
            )


class TestAsyncExtractionAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.create(
            config={
                "chunk_mode": "PAGE",
                "citation_bbox": True,
                "cite_sources": True,
                "confidence_scores": True,
                "extract_model": "openai-gpt-4-1",
                "extraction_mode": "FAST",
                "extraction_target": "PER_DOC",
                "high_resolution_mode": True,
                "invalidate_cache": True,
                "multimodal_fast_mode": True,
                "num_pages_context": 1,
                "page_range": "page_range",
                "parse_model": "openai-gpt-4o",
                "priority": "low",
                "system_prompt": "system_prompt",
                "use_reasoning": True,
            },
            data_schema={"foo": {"foo": "bar"}},
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.with_raw_response.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = await response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.with_streaming_response.create(
            config={},
            data_schema={"foo": {"foo": "bar"}},
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = await response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "chunk_mode": "PAGE",
                "citation_bbox": True,
                "cite_sources": True,
                "confidence_scores": True,
                "extract_model": "openai-gpt-4-1",
                "extraction_mode": "FAST",
                "extraction_target": "PER_DOC",
                "high_resolution_mode": True,
                "invalidate_cache": True,
                "multimodal_fast_mode": True,
                "num_pages_context": 1,
                "page_range": "page_range",
                "parse_model": "openai-gpt-4o",
                "priority": "low",
                "system_prompt": "system_prompt",
                "use_reasoning": True,
            },
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.with_raw_response.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = await response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.with_streaming_response.update(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = await response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            await async_client.extraction.extraction_agents.with_raw_response.update(
                extraction_agent_id="",
                config={},
                data_schema={"foo": {"foo": "bar"}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.list()
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.list(
            include_default=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = await response.parse()
        assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = await response.parse()
            assert_matches_type(ExtractionAgentListResponse, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = await response.parse()
        assert_matches_type(object, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = await response.parse()
            assert_matches_type(object, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            await async_client.extraction.extraction_agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        extraction_agent = await async_client.extraction.extraction_agents.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.extraction_agents.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction_agent = await response.parse()
        assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.extraction_agents.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction_agent = await response.parse()
            assert_matches_type(ExtractAgent, extraction_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `extraction_agent_id` but received ''"):
            await async_client.extraction.extraction_agents.with_raw_response.get(
                "",
            )
