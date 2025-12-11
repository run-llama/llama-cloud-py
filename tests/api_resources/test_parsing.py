# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    ParsingJob,
    ParsingGetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParsing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        parsing = client.parsing.create(
            tier="fast",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.create(
            tier="fast",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agentic_options={"custom_prompt": "custom_prompt"},
            client_name="client_name",
            crop_box={
                "bottom": 0,
                "left": 0,
                "right": 0,
                "top": 0,
            },
            disable_cache=True,
            fast_options={},
            file_id="file_id",
            http_proxy="https:",
            input_options={
                "html": {
                    "make_all_elements_visible": True,
                    "remove_fixed_elements": True,
                    "remove_navigation_elements": True,
                },
                "pdf": {},
                "presentation": {
                    "out_of_bounds_content": True,
                    "skip_embedded_data": True,
                },
                "spreadsheet": {
                    "detect_sub_tables_in_sheets": True,
                    "force_formula_computation_in_sheets": True,
                },
            },
            output_options={
                "embedded_images": {"enable": True},
                "export_pdf": {"enable": True},
                "extract_printed_page_number": True,
                "markdown": {
                    "annotate_links": True,
                    "pages": {"merge_tables_across_pages_in_markdown": True},
                    "tables": {
                        "compact_markdown_tables": True,
                        "markdown_table_multiline_separator": "markdown_table_multiline_separator",
                        "output_tables_as_markdown": True,
                    },
                },
                "screenshots": {"enable": True},
                "spatial_text": {
                    "do_not_unroll_columns": True,
                    "pages": {"merge_tables_across_pages_in_markdown": True},
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                },
                "tables_as_spreadsheet": {
                    "enable": True,
                    "guess_sheet_name": True,
                },
            },
            page_ranges={
                "max_pages": 1,
                "target_pages": "target_pages",
            },
            processing_control={
                "job_failure_conditions": {
                    "allowed_page_failure_ratio": 1,
                    "fail_on_buggy_font": True,
                    "fail_on_image_extraction_error": True,
                    "fail_on_image_ocr_error": True,
                    "fail_on_markdown_reconstruction_error": True,
                },
                "timeouts": {
                    "base_in_seconds": 1,
                    "extra_time_per_page_in_seconds": 1,
                },
            },
            processing_options={
                "aggressive_table_extraction": True,
                "ignore": {
                    "ignore_diagonal_text": True,
                    "ignore_hidden_text": True,
                    "ignore_text_in_image": True,
                },
                "ocr_parameters": {"languages": ["af"]},
            },
            source_url="https:",
            version="2025-12-11",
            webhook_configurations=[
                {
                    "webhook_events": ["string"],
                    "webhook_headers": {"foo": "bar"},
                    "webhook_url": "https:",
                }
            ],
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.create(
            tier="fast",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.create(
            tier="fast",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        parsing = client.parsing.get(
            job_id="job_id",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.get(
            job_id="job_id",
            include_json_output=True,
            include_markdown=True,
            include_structured=True,
            include_text=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingGetResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: LlamaCloud) -> None:
        parsing = client.parsing.upload_file()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.upload_file(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.upload_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParsing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.create(
            tier="fast",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.create(
            tier="fast",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agentic_options={"custom_prompt": "custom_prompt"},
            client_name="client_name",
            crop_box={
                "bottom": 0,
                "left": 0,
                "right": 0,
                "top": 0,
            },
            disable_cache=True,
            fast_options={},
            file_id="file_id",
            http_proxy="https:",
            input_options={
                "html": {
                    "make_all_elements_visible": True,
                    "remove_fixed_elements": True,
                    "remove_navigation_elements": True,
                },
                "pdf": {},
                "presentation": {
                    "out_of_bounds_content": True,
                    "skip_embedded_data": True,
                },
                "spreadsheet": {
                    "detect_sub_tables_in_sheets": True,
                    "force_formula_computation_in_sheets": True,
                },
            },
            output_options={
                "embedded_images": {"enable": True},
                "export_pdf": {"enable": True},
                "extract_printed_page_number": True,
                "markdown": {
                    "annotate_links": True,
                    "pages": {"merge_tables_across_pages_in_markdown": True},
                    "tables": {
                        "compact_markdown_tables": True,
                        "markdown_table_multiline_separator": "markdown_table_multiline_separator",
                        "output_tables_as_markdown": True,
                    },
                },
                "screenshots": {"enable": True},
                "spatial_text": {
                    "do_not_unroll_columns": True,
                    "pages": {"merge_tables_across_pages_in_markdown": True},
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                },
                "tables_as_spreadsheet": {
                    "enable": True,
                    "guess_sheet_name": True,
                },
            },
            page_ranges={
                "max_pages": 1,
                "target_pages": "target_pages",
            },
            processing_control={
                "job_failure_conditions": {
                    "allowed_page_failure_ratio": 1,
                    "fail_on_buggy_font": True,
                    "fail_on_image_extraction_error": True,
                    "fail_on_image_ocr_error": True,
                    "fail_on_markdown_reconstruction_error": True,
                },
                "timeouts": {
                    "base_in_seconds": 1,
                    "extra_time_per_page_in_seconds": 1,
                },
            },
            processing_options={
                "aggressive_table_extraction": True,
                "ignore": {
                    "ignore_diagonal_text": True,
                    "ignore_hidden_text": True,
                    "ignore_text_in_image": True,
                },
                "ocr_parameters": {"languages": ["af"]},
            },
            source_url="https:",
            version="2025-12-11",
            webhook_configurations=[
                {
                    "webhook_events": ["string"],
                    "webhook_headers": {"foo": "bar"},
                    "webhook_url": "https:",
                }
            ],
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.create(
            tier="fast",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.create(
            tier="fast",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.get(
            job_id="job_id",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.get(
            job_id="job_id",
            include_json_output=True,
            include_markdown=True,
            include_structured=True,
            include_text=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingGetResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.upload_file()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.upload_file(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.upload_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True
