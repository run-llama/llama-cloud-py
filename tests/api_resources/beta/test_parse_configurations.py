# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.beta import (
    ParseConfiguration,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParseConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.create(
            name="name",
            parameters={},
            version="version",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.create(
            name="name",
            parameters={
                "adaptive_long_table": True,
                "aggressive_table_extraction": True,
                "annotate_links": True,
                "auto_mode": True,
                "auto_mode_configuration_json": "auto_mode_configuration_json",
                "auto_mode_trigger_on_image_in_page": True,
                "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                "auto_mode_trigger_on_table_in_page": True,
                "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                "azure_openai_api_version": "azure_openai_api_version",
                "azure_openai_deployment_name": "azure_openai_deployment_name",
                "azure_openai_endpoint": "azure_openai_endpoint",
                "azure_openai_key": "azure_openai_key",
                "bbox_bottom": 0,
                "bbox_left": 0,
                "bbox_right": 0,
                "bbox_top": 0,
                "bounding_box": "bounding_box",
                "compact_markdown_table": True,
                "complemental_formatting_instruction": "complemental_formatting_instruction",
                "content_guideline_instruction": "content_guideline_instruction",
                "continuous_mode": True,
                "disable_image_extraction": True,
                "disable_ocr": True,
                "disable_reconstruction": True,
                "do_not_cache": True,
                "do_not_unroll_columns": True,
                "enable_cost_optimizer": True,
                "extract_charts": True,
                "extract_layout": True,
                "extract_printed_page_number": True,
                "fast_mode": True,
                "formatting_instruction": "formatting_instruction",
                "gpt4o_api_key": "gpt4o_api_key",
                "gpt4o_mode": True,
                "guess_xlsx_sheet_name": True,
                "hide_footers": True,
                "hide_headers": True,
                "high_res_ocr": True,
                "html_make_all_elements_visible": True,
                "html_remove_fixed_elements": True,
                "html_remove_navigation_elements": True,
                "http_proxy": "http_proxy",
                "ignore_document_elements_for_layout_detection": True,
                "images_to_save": ["screenshot"],
                "inline_images_in_markdown": True,
                "input_s3_path": "input_s3_path",
                "input_s3_region": "input_s3_region",
                "input_url": "input_url",
                "internal_is_screenshot_job": True,
                "invalidate_cache": True,
                "is_formatting_instruction": True,
                "job_timeout_extra_time_per_page_in_seconds": 0,
                "job_timeout_in_seconds": 0,
                "keep_page_separator_when_merging_tables": True,
                "languages": ["af"],
                "layout_aware": True,
                "line_level_bounding_box": True,
                "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                "max_pages": 0,
                "max_pages_enforced": 0,
                "merge_tables_across_pages_in_markdown": True,
                "model": "model",
                "outlined_table_extraction": True,
                "output_pdf_of_document": True,
                "output_s3_path_prefix": "output_s3_path_prefix",
                "output_s3_region": "output_s3_region",
                "output_tables_as_html": True,
                "page_error_tolerance": 0,
                "page_footer_prefix": "page_footer_prefix",
                "page_footer_suffix": "page_footer_suffix",
                "page_header_prefix": "page_header_prefix",
                "page_header_suffix": "page_header_suffix",
                "page_prefix": "page_prefix",
                "page_separator": "page_separator",
                "page_suffix": "page_suffix",
                "parse_mode": "parse_page_without_llm",
                "parsing_instruction": "parsing_instruction",
                "precise_bounding_box": True,
                "premium_mode": True,
                "presentation_out_of_bounds_content": True,
                "presentation_skip_embedded_data": True,
                "preserve_layout_alignment_across_pages": True,
                "preserve_very_small_text": True,
                "preset": "preset",
                "priority": "low",
                "project_id": "project_id",
                "remove_hidden_text": True,
                "replace_failed_page_mode": "raw_text",
                "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                "save_images": True,
                "skip_diagonal_text": True,
                "specialized_chart_parsing_agentic": True,
                "specialized_chart_parsing_efficient": True,
                "specialized_chart_parsing_plus": True,
                "specialized_image_parsing": True,
                "spreadsheet_extract_sub_tables": True,
                "spreadsheet_force_formula_computation": True,
                "strict_mode_buggy_font": True,
                "strict_mode_image_extraction": True,
                "strict_mode_image_ocr": True,
                "strict_mode_reconstruction": True,
                "structured_output": True,
                "structured_output_json_schema": "structured_output_json_schema",
                "structured_output_json_schema_name": "structured_output_json_schema_name",
                "system_prompt": "system_prompt",
                "system_prompt_append": "system_prompt_append",
                "take_screenshot": True,
                "target_pages": "target_pages",
                "tier": "tier",
                "use_vendor_multimodal_model": True,
                "user_prompt": "user_prompt",
                "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                "version": "version",
                "webhook_configurations": [
                    {
                        "webhook_events": ["extract.pending"],
                        "webhook_headers": {"foo": "string"},
                        "webhook_output_format": "webhook_output_format",
                        "webhook_url": "webhook_url",
                    }
                ],
                "webhook_url": "webhook_url",
            },
            version="version",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            creator="creator",
            source_id="source_id",
            source_type="source_type",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.beta.parse_configurations.with_raw_response.create(
            name="name",
            parameters={},
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.beta.parse_configurations.with_streaming_response.create(
            name="name",
            parameters={},
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.update(
            config_id="config_id",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.update(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parameters={
                "adaptive_long_table": True,
                "aggressive_table_extraction": True,
                "annotate_links": True,
                "auto_mode": True,
                "auto_mode_configuration_json": "auto_mode_configuration_json",
                "auto_mode_trigger_on_image_in_page": True,
                "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                "auto_mode_trigger_on_table_in_page": True,
                "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                "azure_openai_api_version": "azure_openai_api_version",
                "azure_openai_deployment_name": "azure_openai_deployment_name",
                "azure_openai_endpoint": "azure_openai_endpoint",
                "azure_openai_key": "azure_openai_key",
                "bbox_bottom": 0,
                "bbox_left": 0,
                "bbox_right": 0,
                "bbox_top": 0,
                "bounding_box": "bounding_box",
                "compact_markdown_table": True,
                "complemental_formatting_instruction": "complemental_formatting_instruction",
                "content_guideline_instruction": "content_guideline_instruction",
                "continuous_mode": True,
                "disable_image_extraction": True,
                "disable_ocr": True,
                "disable_reconstruction": True,
                "do_not_cache": True,
                "do_not_unroll_columns": True,
                "enable_cost_optimizer": True,
                "extract_charts": True,
                "extract_layout": True,
                "extract_printed_page_number": True,
                "fast_mode": True,
                "formatting_instruction": "formatting_instruction",
                "gpt4o_api_key": "gpt4o_api_key",
                "gpt4o_mode": True,
                "guess_xlsx_sheet_name": True,
                "hide_footers": True,
                "hide_headers": True,
                "high_res_ocr": True,
                "html_make_all_elements_visible": True,
                "html_remove_fixed_elements": True,
                "html_remove_navigation_elements": True,
                "http_proxy": "http_proxy",
                "ignore_document_elements_for_layout_detection": True,
                "images_to_save": ["screenshot"],
                "inline_images_in_markdown": True,
                "input_s3_path": "input_s3_path",
                "input_s3_region": "input_s3_region",
                "input_url": "input_url",
                "internal_is_screenshot_job": True,
                "invalidate_cache": True,
                "is_formatting_instruction": True,
                "job_timeout_extra_time_per_page_in_seconds": 0,
                "job_timeout_in_seconds": 0,
                "keep_page_separator_when_merging_tables": True,
                "languages": ["af"],
                "layout_aware": True,
                "line_level_bounding_box": True,
                "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                "max_pages": 0,
                "max_pages_enforced": 0,
                "merge_tables_across_pages_in_markdown": True,
                "model": "model",
                "outlined_table_extraction": True,
                "output_pdf_of_document": True,
                "output_s3_path_prefix": "output_s3_path_prefix",
                "output_s3_region": "output_s3_region",
                "output_tables_as_html": True,
                "page_error_tolerance": 0,
                "page_footer_prefix": "page_footer_prefix",
                "page_footer_suffix": "page_footer_suffix",
                "page_header_prefix": "page_header_prefix",
                "page_header_suffix": "page_header_suffix",
                "page_prefix": "page_prefix",
                "page_separator": "page_separator",
                "page_suffix": "page_suffix",
                "parse_mode": "parse_page_without_llm",
                "parsing_instruction": "parsing_instruction",
                "precise_bounding_box": True,
                "premium_mode": True,
                "presentation_out_of_bounds_content": True,
                "presentation_skip_embedded_data": True,
                "preserve_layout_alignment_across_pages": True,
                "preserve_very_small_text": True,
                "preset": "preset",
                "priority": "low",
                "project_id": "project_id",
                "remove_hidden_text": True,
                "replace_failed_page_mode": "raw_text",
                "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                "save_images": True,
                "skip_diagonal_text": True,
                "specialized_chart_parsing_agentic": True,
                "specialized_chart_parsing_efficient": True,
                "specialized_chart_parsing_plus": True,
                "specialized_image_parsing": True,
                "spreadsheet_extract_sub_tables": True,
                "spreadsheet_force_formula_computation": True,
                "strict_mode_buggy_font": True,
                "strict_mode_image_extraction": True,
                "strict_mode_image_ocr": True,
                "strict_mode_reconstruction": True,
                "structured_output": True,
                "structured_output_json_schema": "structured_output_json_schema",
                "structured_output_json_schema_name": "structured_output_json_schema_name",
                "system_prompt": "system_prompt",
                "system_prompt_append": "system_prompt_append",
                "take_screenshot": True,
                "target_pages": "target_pages",
                "tier": "tier",
                "use_vendor_multimodal_model": True,
                "user_prompt": "user_prompt",
                "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                "version": "version",
                "webhook_configurations": [
                    {
                        "webhook_events": ["extract.pending"],
                        "webhook_headers": {"foo": "string"},
                        "webhook_output_format": "webhook_output_format",
                        "webhook_url": "webhook_url",
                    }
                ],
                "webhook_url": "webhook_url",
            },
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        response = client.beta.parse_configurations.with_raw_response.update(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with client.beta.parse_configurations.with_streaming_response.update(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.beta.parse_configurations.with_raw_response.update(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.list()
        assert_matches_type(SyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.list(
            creator="creator",
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(SyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.parse_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = response.parse()
        assert_matches_type(SyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.parse_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = response.parse()
            assert_matches_type(SyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.delete(
            config_id="config_id",
        )
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.delete(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.beta.parse_configurations.with_raw_response.delete(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = response.parse()
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.beta.parse_configurations.with_streaming_response.delete(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = response.parse()
            assert parse_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.beta.parse_configurations.with_raw_response.delete(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.get(
            config_id="config_id",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        parse_configuration = client.beta.parse_configurations.get(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.beta.parse_configurations.with_raw_response.get(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.beta.parse_configurations.with_streaming_response.get(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.beta.parse_configurations.with_raw_response.get(
                config_id="",
            )


class TestAsyncParseConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.create(
            name="name",
            parameters={},
            version="version",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.create(
            name="name",
            parameters={
                "adaptive_long_table": True,
                "aggressive_table_extraction": True,
                "annotate_links": True,
                "auto_mode": True,
                "auto_mode_configuration_json": "auto_mode_configuration_json",
                "auto_mode_trigger_on_image_in_page": True,
                "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                "auto_mode_trigger_on_table_in_page": True,
                "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                "azure_openai_api_version": "azure_openai_api_version",
                "azure_openai_deployment_name": "azure_openai_deployment_name",
                "azure_openai_endpoint": "azure_openai_endpoint",
                "azure_openai_key": "azure_openai_key",
                "bbox_bottom": 0,
                "bbox_left": 0,
                "bbox_right": 0,
                "bbox_top": 0,
                "bounding_box": "bounding_box",
                "compact_markdown_table": True,
                "complemental_formatting_instruction": "complemental_formatting_instruction",
                "content_guideline_instruction": "content_guideline_instruction",
                "continuous_mode": True,
                "disable_image_extraction": True,
                "disable_ocr": True,
                "disable_reconstruction": True,
                "do_not_cache": True,
                "do_not_unroll_columns": True,
                "enable_cost_optimizer": True,
                "extract_charts": True,
                "extract_layout": True,
                "extract_printed_page_number": True,
                "fast_mode": True,
                "formatting_instruction": "formatting_instruction",
                "gpt4o_api_key": "gpt4o_api_key",
                "gpt4o_mode": True,
                "guess_xlsx_sheet_name": True,
                "hide_footers": True,
                "hide_headers": True,
                "high_res_ocr": True,
                "html_make_all_elements_visible": True,
                "html_remove_fixed_elements": True,
                "html_remove_navigation_elements": True,
                "http_proxy": "http_proxy",
                "ignore_document_elements_for_layout_detection": True,
                "images_to_save": ["screenshot"],
                "inline_images_in_markdown": True,
                "input_s3_path": "input_s3_path",
                "input_s3_region": "input_s3_region",
                "input_url": "input_url",
                "internal_is_screenshot_job": True,
                "invalidate_cache": True,
                "is_formatting_instruction": True,
                "job_timeout_extra_time_per_page_in_seconds": 0,
                "job_timeout_in_seconds": 0,
                "keep_page_separator_when_merging_tables": True,
                "languages": ["af"],
                "layout_aware": True,
                "line_level_bounding_box": True,
                "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                "max_pages": 0,
                "max_pages_enforced": 0,
                "merge_tables_across_pages_in_markdown": True,
                "model": "model",
                "outlined_table_extraction": True,
                "output_pdf_of_document": True,
                "output_s3_path_prefix": "output_s3_path_prefix",
                "output_s3_region": "output_s3_region",
                "output_tables_as_html": True,
                "page_error_tolerance": 0,
                "page_footer_prefix": "page_footer_prefix",
                "page_footer_suffix": "page_footer_suffix",
                "page_header_prefix": "page_header_prefix",
                "page_header_suffix": "page_header_suffix",
                "page_prefix": "page_prefix",
                "page_separator": "page_separator",
                "page_suffix": "page_suffix",
                "parse_mode": "parse_page_without_llm",
                "parsing_instruction": "parsing_instruction",
                "precise_bounding_box": True,
                "premium_mode": True,
                "presentation_out_of_bounds_content": True,
                "presentation_skip_embedded_data": True,
                "preserve_layout_alignment_across_pages": True,
                "preserve_very_small_text": True,
                "preset": "preset",
                "priority": "low",
                "project_id": "project_id",
                "remove_hidden_text": True,
                "replace_failed_page_mode": "raw_text",
                "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                "save_images": True,
                "skip_diagonal_text": True,
                "specialized_chart_parsing_agentic": True,
                "specialized_chart_parsing_efficient": True,
                "specialized_chart_parsing_plus": True,
                "specialized_image_parsing": True,
                "spreadsheet_extract_sub_tables": True,
                "spreadsheet_force_formula_computation": True,
                "strict_mode_buggy_font": True,
                "strict_mode_image_extraction": True,
                "strict_mode_image_ocr": True,
                "strict_mode_reconstruction": True,
                "structured_output": True,
                "structured_output_json_schema": "structured_output_json_schema",
                "structured_output_json_schema_name": "structured_output_json_schema_name",
                "system_prompt": "system_prompt",
                "system_prompt_append": "system_prompt_append",
                "take_screenshot": True,
                "target_pages": "target_pages",
                "tier": "tier",
                "use_vendor_multimodal_model": True,
                "user_prompt": "user_prompt",
                "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                "version": "version",
                "webhook_configurations": [
                    {
                        "webhook_events": ["extract.pending"],
                        "webhook_headers": {"foo": "string"},
                        "webhook_output_format": "webhook_output_format",
                        "webhook_url": "webhook_url",
                    }
                ],
                "webhook_url": "webhook_url",
            },
            version="version",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            creator="creator",
            source_id="source_id",
            source_type="source_type",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.parse_configurations.with_raw_response.create(
            name="name",
            parameters={},
            version="version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = await response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.parse_configurations.with_streaming_response.create(
            name="name",
            parameters={},
            version="version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = await response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.update(
            config_id="config_id",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.update(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parameters={
                "adaptive_long_table": True,
                "aggressive_table_extraction": True,
                "annotate_links": True,
                "auto_mode": True,
                "auto_mode_configuration_json": "auto_mode_configuration_json",
                "auto_mode_trigger_on_image_in_page": True,
                "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                "auto_mode_trigger_on_table_in_page": True,
                "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                "azure_openai_api_version": "azure_openai_api_version",
                "azure_openai_deployment_name": "azure_openai_deployment_name",
                "azure_openai_endpoint": "azure_openai_endpoint",
                "azure_openai_key": "azure_openai_key",
                "bbox_bottom": 0,
                "bbox_left": 0,
                "bbox_right": 0,
                "bbox_top": 0,
                "bounding_box": "bounding_box",
                "compact_markdown_table": True,
                "complemental_formatting_instruction": "complemental_formatting_instruction",
                "content_guideline_instruction": "content_guideline_instruction",
                "continuous_mode": True,
                "disable_image_extraction": True,
                "disable_ocr": True,
                "disable_reconstruction": True,
                "do_not_cache": True,
                "do_not_unroll_columns": True,
                "enable_cost_optimizer": True,
                "extract_charts": True,
                "extract_layout": True,
                "extract_printed_page_number": True,
                "fast_mode": True,
                "formatting_instruction": "formatting_instruction",
                "gpt4o_api_key": "gpt4o_api_key",
                "gpt4o_mode": True,
                "guess_xlsx_sheet_name": True,
                "hide_footers": True,
                "hide_headers": True,
                "high_res_ocr": True,
                "html_make_all_elements_visible": True,
                "html_remove_fixed_elements": True,
                "html_remove_navigation_elements": True,
                "http_proxy": "http_proxy",
                "ignore_document_elements_for_layout_detection": True,
                "images_to_save": ["screenshot"],
                "inline_images_in_markdown": True,
                "input_s3_path": "input_s3_path",
                "input_s3_region": "input_s3_region",
                "input_url": "input_url",
                "internal_is_screenshot_job": True,
                "invalidate_cache": True,
                "is_formatting_instruction": True,
                "job_timeout_extra_time_per_page_in_seconds": 0,
                "job_timeout_in_seconds": 0,
                "keep_page_separator_when_merging_tables": True,
                "languages": ["af"],
                "layout_aware": True,
                "line_level_bounding_box": True,
                "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                "max_pages": 0,
                "max_pages_enforced": 0,
                "merge_tables_across_pages_in_markdown": True,
                "model": "model",
                "outlined_table_extraction": True,
                "output_pdf_of_document": True,
                "output_s3_path_prefix": "output_s3_path_prefix",
                "output_s3_region": "output_s3_region",
                "output_tables_as_html": True,
                "page_error_tolerance": 0,
                "page_footer_prefix": "page_footer_prefix",
                "page_footer_suffix": "page_footer_suffix",
                "page_header_prefix": "page_header_prefix",
                "page_header_suffix": "page_header_suffix",
                "page_prefix": "page_prefix",
                "page_separator": "page_separator",
                "page_suffix": "page_suffix",
                "parse_mode": "parse_page_without_llm",
                "parsing_instruction": "parsing_instruction",
                "precise_bounding_box": True,
                "premium_mode": True,
                "presentation_out_of_bounds_content": True,
                "presentation_skip_embedded_data": True,
                "preserve_layout_alignment_across_pages": True,
                "preserve_very_small_text": True,
                "preset": "preset",
                "priority": "low",
                "project_id": "project_id",
                "remove_hidden_text": True,
                "replace_failed_page_mode": "raw_text",
                "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                "save_images": True,
                "skip_diagonal_text": True,
                "specialized_chart_parsing_agentic": True,
                "specialized_chart_parsing_efficient": True,
                "specialized_chart_parsing_plus": True,
                "specialized_image_parsing": True,
                "spreadsheet_extract_sub_tables": True,
                "spreadsheet_force_formula_computation": True,
                "strict_mode_buggy_font": True,
                "strict_mode_image_extraction": True,
                "strict_mode_image_ocr": True,
                "strict_mode_reconstruction": True,
                "structured_output": True,
                "structured_output_json_schema": "structured_output_json_schema",
                "structured_output_json_schema_name": "structured_output_json_schema_name",
                "system_prompt": "system_prompt",
                "system_prompt_append": "system_prompt_append",
                "take_screenshot": True,
                "target_pages": "target_pages",
                "tier": "tier",
                "use_vendor_multimodal_model": True,
                "user_prompt": "user_prompt",
                "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                "version": "version",
                "webhook_configurations": [
                    {
                        "webhook_events": ["extract.pending"],
                        "webhook_headers": {"foo": "string"},
                        "webhook_output_format": "webhook_output_format",
                        "webhook_url": "webhook_url",
                    }
                ],
                "webhook_url": "webhook_url",
            },
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.parse_configurations.with_raw_response.update(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = await response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.parse_configurations.with_streaming_response.update(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = await response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.beta.parse_configurations.with_raw_response.update(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.list()
        assert_matches_type(AsyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.list(
            creator="creator",
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(AsyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.parse_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.parse_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[ParseConfiguration], parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.delete(
            config_id="config_id",
        )
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.delete(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.parse_configurations.with_raw_response.delete(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = await response.parse()
        assert parse_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.parse_configurations.with_streaming_response.delete(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = await response.parse()
            assert parse_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.beta.parse_configurations.with_raw_response.delete(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.get(
            config_id="config_id",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parse_configuration = await async_client.beta.parse_configurations.get(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.parse_configurations.with_raw_response.get(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse_configuration = await response.parse()
        assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.parse_configurations.with_streaming_response.get(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse_configuration = await response.parse()
            assert_matches_type(ParseConfiguration, parse_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.beta.parse_configurations.with_raw_response.get(
                config_id="",
            )
