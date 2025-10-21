# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1.extraction import ExtractJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtraction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: LlamacloudProd) -> None:
        extraction = client.v1.extraction.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: LlamacloudProd) -> None:
        extraction = client.v1.extraction.run(
            config={
                "chunk_mode": "PAGE",
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
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file={
                "data": "data",
                "mime_type": "mime_type",
            },
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.with_raw_response.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.with_streaming_response.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractJob, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtraction:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncLlamacloudProd) -> None:
        extraction = await async_client.v1.extraction.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        extraction = await async_client.v1.extraction.run(
            config={
                "chunk_mode": "PAGE",
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
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file={
                "data": "data",
                "mime_type": "mime_type",
            },
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.with_raw_response.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractJob, extraction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.with_streaming_response.run(
            config={},
            data_schema={"foo": {"foo": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractJob, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True
