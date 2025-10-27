# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1.extraction import (
    ExtractJob,
    JobListResponse,
    JobBatchResponse,
    JobRetrieveResultResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_ui=True,
            config_override={
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
    def test_raw_response_create(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.create(
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
    def test_method_retrieve(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.v1.extraction.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            from_ui=True,
            config_override={
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
            data_schema_override={"foo": {"foo": "bar"}},
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file_with_all_params(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            from_ui=True,
            config_override="config_override",
            data_schema_override="data_schema_override",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_file(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_file(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.file(
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
    def test_method_retrieve_result(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_result_with_all_params(self, client: LlamacloudProd) -> None:
        job = client.v1.extraction.jobs.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_result(self, client: LlamacloudProd) -> None:
        response = client.v1.extraction.jobs.with_raw_response.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_result(self, client: LlamacloudProd) -> None:
        with client.v1.extraction.jobs.with_streaming_response.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_result(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.v1.extraction.jobs.with_raw_response.retrieve_result(
                job_id="",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_ui=True,
            config_override={
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
    async def test_raw_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.create(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.create(
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
    async def test_method_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ExtractJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.v1.extraction.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.list(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            from_ui=True,
            config_override={
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
            data_schema_override={"foo": {"foo": "bar"}},
            webhook_configurations=[
                {
                    "webhook_events": ["extract.pending"],
                    "webhook_headers": {"foo": "string"},
                    "webhook_output_format": "webhook_output_format",
                    "webhook_url": "webhook_url",
                }
            ],
        )
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.batch(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
            from_ui=True,
            config_override="config_override",
            data_schema_override="data_schema_override",
        )
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_file(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.file(
            extraction_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ExtractJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.file(
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
    async def test_method_retrieve_result(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_result_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        job = await async_client.v1.extraction.jobs.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_result(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.extraction.jobs.with_raw_response.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_result(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.extraction.jobs.with_streaming_response.retrieve_result(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveResultResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_result(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.v1.extraction.jobs.with_raw_response.retrieve_result(
                job_id="",
            )
