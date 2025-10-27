# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1 import (
    ParsingJob,
    ParsingGetParsingHistoryResponse,
    ParsingGetSupportedFileExtensionsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParsing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_screenshot(self, client: LlamacloudProd) -> None:
        parsing = client.v1.parsing.create_screenshot()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_screenshot_with_all_params(self, client: LlamacloudProd) -> None:
        parsing = client.v1.parsing.create_screenshot(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            do_not_cache=True,
            file=b"raw file contents",
            http_proxy="http_proxy",
            input_s3_path="input_s3_path",
            input_s3_region="input_s3_region",
            input_url="input_url",
            invalidate_cache=True,
            job_timeout_extra_time_per_page_in_seconds=0,
            job_timeout_in_seconds=0,
            max_pages=0,
            output_s3_path_prefix="output_s3_path_prefix",
            output_s3_region="output_s3_region",
            target_pages="target_pages",
            webhook_configurations="webhook_configurations",
            webhook_url="webhook_url",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_screenshot(self, client: LlamacloudProd) -> None:
        response = client.v1.parsing.with_raw_response.create_screenshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_screenshot(self, client: LlamacloudProd) -> None:
        with client.v1.parsing.with_streaming_response.create_screenshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_parsing_history(self, client: LlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            parsing = client.v1.parsing.get_parsing_history()

        assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_parsing_history(self, client: LlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.v1.parsing.with_raw_response.get_parsing_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_parsing_history(self, client: LlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            with client.v1.parsing.with_streaming_response.get_parsing_history() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                parsing = response.parse()
                assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_supported_file_extensions(self, client: LlamacloudProd) -> None:
        parsing = client.v1.parsing.get_supported_file_extensions()
        assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_supported_file_extensions(self, client: LlamacloudProd) -> None:
        response = client.v1.parsing.with_raw_response.get_supported_file_extensions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_supported_file_extensions(self, client: LlamacloudProd) -> None:
        with client.v1.parsing.with_streaming_response.get_supported_file_extensions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: LlamacloudProd) -> None:
        parsing = client.v1.parsing.upload_file()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file_with_all_params(self, client: LlamacloudProd) -> None:
        parsing = client.v1.parsing.upload_file(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            adaptive_long_table=True,
            aggressive_table_extraction=True,
            annotate_links=True,
            auto_mode=True,
            auto_mode_configuration_json="auto_mode_configuration_json",
            auto_mode_trigger_on_image_in_page=True,
            auto_mode_trigger_on_regexp_in_page="auto_mode_trigger_on_regexp_in_page",
            auto_mode_trigger_on_table_in_page=True,
            auto_mode_trigger_on_text_in_page="auto_mode_trigger_on_text_in_page",
            azure_openai_api_version="azure_openai_api_version",
            azure_openai_deployment_name="azure_openai_deployment_name",
            azure_openai_endpoint="azure_openai_endpoint",
            azure_openai_key="azure_openai_key",
            bbox_bottom=0,
            bbox_left=0,
            bbox_right=0,
            bbox_top=0,
            bounding_box="bounding_box",
            compact_markdown_table=True,
            complemental_formatting_instruction="complemental_formatting_instruction",
            content_guideline_instruction="content_guideline_instruction",
            continuous_mode=True,
            disable_image_extraction=True,
            disable_ocr=True,
            disable_reconstruction=True,
            do_not_cache=True,
            do_not_unroll_columns=True,
            extract_charts=True,
            extract_layout=True,
            fast_mode=True,
            file=b"raw file contents",
            formatting_instruction="formatting_instruction",
            gpt4o_api_key="gpt4o_api_key",
            gpt4o_mode=True,
            guess_xlsx_sheet_name=True,
            hide_footers=True,
            hide_headers=True,
            high_res_ocr=True,
            html_make_all_elements_visible=True,
            html_remove_fixed_elements=True,
            html_remove_navigation_elements=True,
            http_proxy="http_proxy",
            ignore_document_elements_for_layout_detection=True,
            inline_images_in_markdown=True,
            input_s3_path="input_s3_path",
            input_s3_region="input_s3_region",
            input_url="input_url",
            invalidate_cache=True,
            is_formatting_instruction=True,
            job_timeout_extra_time_per_page_in_seconds=0,
            job_timeout_in_seconds=0,
            keep_page_separator_when_merging_tables=True,
            language=["af"],
            layout_aware=True,
            markdown_table_multiline_header_separator="markdown_table_multiline_header_separator",
            max_pages=0,
            merge_tables_across_pages_in_markdown=True,
            model="model",
            outlined_table_extraction=True,
            output_pdf_of_document=True,
            output_s3_path_prefix="output_s3_path_prefix",
            output_s3_region="output_s3_region",
            output_tables_as_html=True,
            page_error_tolerance=0,
            page_footer_prefix="page_footer_prefix",
            page_footer_suffix="page_footer_suffix",
            page_header_prefix="page_header_prefix",
            page_header_suffix="page_header_suffix",
            page_prefix="page_prefix",
            page_separator="page_separator",
            page_suffix="page_suffix",
            parse_mode="parse_page_without_llm",
            parsing_instruction="parsing_instruction",
            precise_bounding_box=True,
            premium_mode=True,
            preserve_layout_alignment_across_pages=True,
            preserve_very_small_text=True,
            preset="preset",
            remove_hidden_text=True,
            replace_failed_page_mode="raw_text",
            replace_failed_page_with_error_message_prefix="replace_failed_page_with_error_message_prefix",
            replace_failed_page_with_error_message_suffix="replace_failed_page_with_error_message_suffix",
            save_images=True,
            skip_diagonal_text=True,
            specialized_chart_parsing_agentic=True,
            specialized_chart_parsing_efficient=True,
            specialized_chart_parsing_plus=True,
            specialized_image_parsing=True,
            spreadsheet_extract_sub_tables=True,
            spreadsheet_force_formula_computation=True,
            strict_mode_buggy_font=True,
            strict_mode_image_extraction=True,
            strict_mode_image_ocr=True,
            strict_mode_reconstruction=True,
            structured_output=True,
            structured_output_json_schema="structured_output_json_schema",
            structured_output_json_schema_name="structured_output_json_schema_name",
            system_prompt="system_prompt",
            system_prompt_append="system_prompt_append",
            take_screenshot=True,
            target_pages="target_pages",
            use_vendor_multimodal_model=True,
            user_prompt="user_prompt",
            vendor_multimodal_api_key="vendor_multimodal_api_key",
            vendor_multimodal_model_name="vendor_multimodal_model_name",
            webhook_configurations="webhook_configurations",
            webhook_url="webhook_url",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: LlamacloudProd) -> None:
        response = client.v1.parsing.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: LlamacloudProd) -> None:
        with client.v1.parsing.with_streaming_response.upload_file() as response:
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
    async def test_method_create_screenshot(self, async_client: AsyncLlamacloudProd) -> None:
        parsing = await async_client.v1.parsing.create_screenshot()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_screenshot_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        parsing = await async_client.v1.parsing.create_screenshot(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            do_not_cache=True,
            file=b"raw file contents",
            http_proxy="http_proxy",
            input_s3_path="input_s3_path",
            input_s3_region="input_s3_region",
            input_url="input_url",
            invalidate_cache=True,
            job_timeout_extra_time_per_page_in_seconds=0,
            job_timeout_in_seconds=0,
            max_pages=0,
            output_s3_path_prefix="output_s3_path_prefix",
            output_s3_region="output_s3_region",
            target_pages="target_pages",
            webhook_configurations="webhook_configurations",
            webhook_url="webhook_url",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_screenshot(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.parsing.with_raw_response.create_screenshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_screenshot(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.parsing.with_streaming_response.create_screenshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_parsing_history(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            parsing = await async_client.v1.parsing.get_parsing_history()

        assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_parsing_history(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.v1.parsing.with_raw_response.get_parsing_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_parsing_history(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.v1.parsing.with_streaming_response.get_parsing_history() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                parsing = await response.parse()
                assert_matches_type(ParsingGetParsingHistoryResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_supported_file_extensions(self, async_client: AsyncLlamacloudProd) -> None:
        parsing = await async_client.v1.parsing.get_supported_file_extensions()
        assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_supported_file_extensions(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.parsing.with_raw_response.get_supported_file_extensions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_supported_file_extensions(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.parsing.with_streaming_response.get_supported_file_extensions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingGetSupportedFileExtensionsResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncLlamacloudProd) -> None:
        parsing = await async_client.v1.parsing.upload_file()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        parsing = await async_client.v1.parsing.upload_file(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            adaptive_long_table=True,
            aggressive_table_extraction=True,
            annotate_links=True,
            auto_mode=True,
            auto_mode_configuration_json="auto_mode_configuration_json",
            auto_mode_trigger_on_image_in_page=True,
            auto_mode_trigger_on_regexp_in_page="auto_mode_trigger_on_regexp_in_page",
            auto_mode_trigger_on_table_in_page=True,
            auto_mode_trigger_on_text_in_page="auto_mode_trigger_on_text_in_page",
            azure_openai_api_version="azure_openai_api_version",
            azure_openai_deployment_name="azure_openai_deployment_name",
            azure_openai_endpoint="azure_openai_endpoint",
            azure_openai_key="azure_openai_key",
            bbox_bottom=0,
            bbox_left=0,
            bbox_right=0,
            bbox_top=0,
            bounding_box="bounding_box",
            compact_markdown_table=True,
            complemental_formatting_instruction="complemental_formatting_instruction",
            content_guideline_instruction="content_guideline_instruction",
            continuous_mode=True,
            disable_image_extraction=True,
            disable_ocr=True,
            disable_reconstruction=True,
            do_not_cache=True,
            do_not_unroll_columns=True,
            extract_charts=True,
            extract_layout=True,
            fast_mode=True,
            file=b"raw file contents",
            formatting_instruction="formatting_instruction",
            gpt4o_api_key="gpt4o_api_key",
            gpt4o_mode=True,
            guess_xlsx_sheet_name=True,
            hide_footers=True,
            hide_headers=True,
            high_res_ocr=True,
            html_make_all_elements_visible=True,
            html_remove_fixed_elements=True,
            html_remove_navigation_elements=True,
            http_proxy="http_proxy",
            ignore_document_elements_for_layout_detection=True,
            inline_images_in_markdown=True,
            input_s3_path="input_s3_path",
            input_s3_region="input_s3_region",
            input_url="input_url",
            invalidate_cache=True,
            is_formatting_instruction=True,
            job_timeout_extra_time_per_page_in_seconds=0,
            job_timeout_in_seconds=0,
            keep_page_separator_when_merging_tables=True,
            language=["af"],
            layout_aware=True,
            markdown_table_multiline_header_separator="markdown_table_multiline_header_separator",
            max_pages=0,
            merge_tables_across_pages_in_markdown=True,
            model="model",
            outlined_table_extraction=True,
            output_pdf_of_document=True,
            output_s3_path_prefix="output_s3_path_prefix",
            output_s3_region="output_s3_region",
            output_tables_as_html=True,
            page_error_tolerance=0,
            page_footer_prefix="page_footer_prefix",
            page_footer_suffix="page_footer_suffix",
            page_header_prefix="page_header_prefix",
            page_header_suffix="page_header_suffix",
            page_prefix="page_prefix",
            page_separator="page_separator",
            page_suffix="page_suffix",
            parse_mode="parse_page_without_llm",
            parsing_instruction="parsing_instruction",
            precise_bounding_box=True,
            premium_mode=True,
            preserve_layout_alignment_across_pages=True,
            preserve_very_small_text=True,
            preset="preset",
            remove_hidden_text=True,
            replace_failed_page_mode="raw_text",
            replace_failed_page_with_error_message_prefix="replace_failed_page_with_error_message_prefix",
            replace_failed_page_with_error_message_suffix="replace_failed_page_with_error_message_suffix",
            save_images=True,
            skip_diagonal_text=True,
            specialized_chart_parsing_agentic=True,
            specialized_chart_parsing_efficient=True,
            specialized_chart_parsing_plus=True,
            specialized_image_parsing=True,
            spreadsheet_extract_sub_tables=True,
            spreadsheet_force_formula_computation=True,
            strict_mode_buggy_font=True,
            strict_mode_image_extraction=True,
            strict_mode_image_ocr=True,
            strict_mode_reconstruction=True,
            structured_output=True,
            structured_output_json_schema="structured_output_json_schema",
            structured_output_json_schema_name="structured_output_json_schema_name",
            system_prompt="system_prompt",
            system_prompt_append="system_prompt_append",
            take_screenshot=True,
            target_pages="target_pages",
            use_vendor_multimodal_model=True,
            user_prompt="user_prompt",
            vendor_multimodal_api_key="vendor_multimodal_api_key",
            vendor_multimodal_model_name="vendor_multimodal_model_name",
            webhook_configurations="webhook_configurations",
            webhook_url="webhook_url",
        )
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.parsing.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingJob, parsing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.parsing.with_streaming_response.upload_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingJob, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True
