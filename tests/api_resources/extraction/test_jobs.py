# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.extraction import (
    ExtractJob,
    JobListResponse,
    JobGetResultResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_ui=True,
            config_override={
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
            data_schema_override={"foo": {"foo": "bar"}},
            priority="low",
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.extraction.jobs.with_raw_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.extraction.jobs.with_streaming_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.extraction.jobs.with_raw_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.extraction.jobs.with_streaming_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file_with_all_params(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            from_ui=True,
            config_override="config_override",
            data_schema_override="data_schema_override",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_file(self, client: LlamaCloud) -> None:
        response = client.extraction.jobs.with_raw_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_file(self, client: LlamaCloud) -> None:
        with client.extraction.jobs.with_streaming_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.extraction.jobs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.extraction.jobs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extraction.jobs.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_result(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_result_with_all_params(self, client: LlamaCloud) -> None:
        job = client.extraction.jobs.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_result(self, client: LlamaCloud) -> None:
        response = client.extraction.jobs.with_raw_response.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_result(self, client: LlamaCloud) -> None:
        with client.extraction.jobs.with_streaming_response.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobGetResultResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_result(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extraction.jobs.with_raw_response.get_result(
                job_id="",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_ui=True,
            config_override={
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
            data_schema_override={"foo": {"foo": "bar"}},
            priority="low",
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.jobs.with_raw_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.jobs.with_streaming_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.jobs.with_raw_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.jobs.with_streaming_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            from_ui=True,
            config_override="config_override",
            data_schema_override="data_schema_override",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_file(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.jobs.with_raw_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.jobs.with_streaming_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.jobs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.jobs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extraction.jobs.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_result(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_result_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.extraction.jobs.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_result(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extraction.jobs.with_raw_response.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_result(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extraction.jobs.with_streaming_response.get_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobGetResultResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_result(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extraction.jobs.with_raw_response.get_result(
                job_id="",
            )
