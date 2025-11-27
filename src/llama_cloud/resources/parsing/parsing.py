# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, Optional, cast
from typing_extensions import Unpack, Literal

import httpx

from ...types import ParsingMode, FailPageMode, parsing_upload_file_params, parsing_create_screenshot_params
from .job.job import (
    JobResource,
    AsyncJobResource,
    JobResourceWithRawResponse,
    AsyncJobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
    AsyncJobResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._polling import BackoffStrategy
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.parsing_job import ParsingJob
from ...types.parsing_mode import ParsingMode
from ...types.fail_page_mode import FailPageMode
from ...types.parser_languages import ParserLanguages
from ...types.parsing_upload_file_params import ParsingUploadFileParams
from ...types.parsing.job.parsing_job_json_result import ParsingJobJsonResult
from ...types.parsing.job.parsing_job_text_result import ParsingJobTextResult
from ...types.parsing.job.parsing_job_markdown_result import ParsingJobMarkdownResult
from ...types.parsing.job.parsing_job_structured_result import ParsingJobStructuredResult
from ...types.parsing_get_supported_file_extensions_response import ParsingGetSupportedFileExtensionsResponse

__all__ = ["ParsingResource", "AsyncParsingResource"]


class ParsingResource(SyncAPIResource):
    @cached_property
    def job(self) -> JobResource:
        return JobResource(self._client)

    @cached_property
    def with_raw_response(self) -> ParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return ParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return ParsingResourceWithStreamingResponse(self)

    def create_screenshot(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        do_not_cache: bool | Omit = omit,
        file: Optional[FileTypes] | Omit = omit,
        http_proxy: str | Omit = omit,
        input_s3_path: str | Omit = omit,
        input_s3_region: str | Omit = omit,
        input_url: str | Omit = omit,
        invalidate_cache: bool | Omit = omit,
        job_timeout_extra_time_per_page_in_seconds: float | Omit = omit,
        job_timeout_in_seconds: float | Omit = omit,
        max_pages: Optional[int] | Omit = omit,
        output_s3_path_prefix: str | Omit = omit,
        output_s3_region: str | Omit = omit,
        target_pages: str | Omit = omit,
        webhook_configurations: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Screenshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "do_not_cache": do_not_cache,
                "file": file,
                "http_proxy": http_proxy,
                "input_s3_path": input_s3_path,
                "input_s3_region": input_s3_region,
                "input_url": input_url,
                "invalidate_cache": invalidate_cache,
                "job_timeout_extra_time_per_page_in_seconds": job_timeout_extra_time_per_page_in_seconds,
                "job_timeout_in_seconds": job_timeout_in_seconds,
                "max_pages": max_pages,
                "output_s3_path_prefix": output_s3_path_prefix,
                "output_s3_region": output_s3_region,
                "target_pages": target_pages,
                "webhook_configurations": webhook_configurations,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/parsing/screenshot",
            body=maybe_transform(body, parsing_create_screenshot_params.ParsingCreateScreenshotParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_create_screenshot_params.ParsingCreateScreenshotParams,
                ),
            ),
            cast_to=ParsingJob,
        )

    def get_supported_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetSupportedFileExtensionsResponse:
        """Get a list of supported file extensions"""
        return self._get(
            "/api/v1/parsing/supported_file_extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingGetSupportedFileExtensionsResponse,
        )

    def upload_file(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        adaptive_long_table: bool | Omit = omit,
        aggressive_table_extraction: bool | Omit = omit,
        annotate_links: bool | Omit = omit,
        auto_mode: bool | Omit = omit,
        auto_mode_configuration_json: str | Omit = omit,
        auto_mode_trigger_on_image_in_page: bool | Omit = omit,
        auto_mode_trigger_on_regexp_in_page: str | Omit = omit,
        auto_mode_trigger_on_table_in_page: bool | Omit = omit,
        auto_mode_trigger_on_text_in_page: str | Omit = omit,
        azure_openai_api_version: str | Omit = omit,
        azure_openai_deployment_name: str | Omit = omit,
        azure_openai_endpoint: str | Omit = omit,
        azure_openai_key: str | Omit = omit,
        bbox_bottom: float | Omit = omit,
        bbox_left: float | Omit = omit,
        bbox_right: float | Omit = omit,
        bbox_top: float | Omit = omit,
        bounding_box: str | Omit = omit,
        compact_markdown_table: bool | Omit = omit,
        complemental_formatting_instruction: str | Omit = omit,
        content_guideline_instruction: str | Omit = omit,
        continuous_mode: bool | Omit = omit,
        disable_image_extraction: bool | Omit = omit,
        disable_ocr: bool | Omit = omit,
        disable_reconstruction: bool | Omit = omit,
        do_not_cache: bool | Omit = omit,
        do_not_unroll_columns: bool | Omit = omit,
        extract_charts: bool | Omit = omit,
        extract_layout: bool | Omit = omit,
        extract_printed_page_number: bool | Omit = omit,
        fast_mode: bool | Omit = omit,
        file: Optional[FileTypes] | Omit = omit,
        formatting_instruction: str | Omit = omit,
        gpt4o_api_key: str | Omit = omit,
        gpt4o_mode: bool | Omit = omit,
        guess_xlsx_sheet_name: bool | Omit = omit,
        hide_footers: bool | Omit = omit,
        hide_headers: bool | Omit = omit,
        high_res_ocr: bool | Omit = omit,
        html_make_all_elements_visible: bool | Omit = omit,
        html_remove_fixed_elements: bool | Omit = omit,
        html_remove_navigation_elements: bool | Omit = omit,
        http_proxy: str | Omit = omit,
        ignore_document_elements_for_layout_detection: bool | Omit = omit,
        inline_images_in_markdown: bool | Omit = omit,
        input_s3_path: str | Omit = omit,
        input_s3_region: str | Omit = omit,
        input_url: str | Omit = omit,
        invalidate_cache: bool | Omit = omit,
        is_formatting_instruction: bool | Omit = omit,
        job_timeout_extra_time_per_page_in_seconds: float | Omit = omit,
        job_timeout_in_seconds: float | Omit = omit,
        keep_page_separator_when_merging_tables: bool | Omit = omit,
        language: List[ParserLanguages] | Omit = omit,
        layout_aware: bool | Omit = omit,
        line_level_bounding_box: bool | Omit = omit,
        markdown_table_multiline_header_separator: str | Omit = omit,
        max_pages: Optional[int] | Omit = omit,
        merge_tables_across_pages_in_markdown: bool | Omit = omit,
        model: str | Omit = omit,
        outlined_table_extraction: bool | Omit = omit,
        output_pdf_of_document: bool | Omit = omit,
        output_s3_path_prefix: str | Omit = omit,
        output_s3_region: str | Omit = omit,
        output_tables_as_html: bool | Omit = omit,
        page_error_tolerance: float | Omit = omit,
        page_footer_prefix: str | Omit = omit,
        page_footer_suffix: str | Omit = omit,
        page_header_prefix: str | Omit = omit,
        page_header_suffix: str | Omit = omit,
        page_prefix: str | Omit = omit,
        page_separator: str | Omit = omit,
        page_suffix: str | Omit = omit,
        parse_mode: Optional[ParsingMode] | Omit = omit,
        parsing_instruction: str | Omit = omit,
        precise_bounding_box: bool | Omit = omit,
        premium_mode: bool | Omit = omit,
        presentation_out_of_bounds_content: bool | Omit = omit,
        preserve_layout_alignment_across_pages: bool | Omit = omit,
        preserve_very_small_text: bool | Omit = omit,
        preset: str | Omit = omit,
        remove_hidden_text: bool | Omit = omit,
        replace_failed_page_mode: Optional[FailPageMode] | Omit = omit,
        replace_failed_page_with_error_message_prefix: str | Omit = omit,
        replace_failed_page_with_error_message_suffix: str | Omit = omit,
        save_images: bool | Omit = omit,
        skip_diagonal_text: bool | Omit = omit,
        specialized_chart_parsing_agentic: bool | Omit = omit,
        specialized_chart_parsing_efficient: bool | Omit = omit,
        specialized_chart_parsing_plus: bool | Omit = omit,
        specialized_image_parsing: bool | Omit = omit,
        spreadsheet_extract_sub_tables: bool | Omit = omit,
        spreadsheet_force_formula_computation: bool | Omit = omit,
        strict_mode_buggy_font: bool | Omit = omit,
        strict_mode_image_extraction: bool | Omit = omit,
        strict_mode_image_ocr: bool | Omit = omit,
        strict_mode_reconstruction: bool | Omit = omit,
        structured_output: bool | Omit = omit,
        structured_output_json_schema: str | Omit = omit,
        structured_output_json_schema_name: str | Omit = omit,
        system_prompt: str | Omit = omit,
        system_prompt_append: str | Omit = omit,
        take_screenshot: bool | Omit = omit,
        target_pages: str | Omit = omit,
        tier: str | Omit = omit,
        use_vendor_multimodal_model: bool | Omit = omit,
        user_prompt: str | Omit = omit,
        vendor_multimodal_api_key: str | Omit = omit,
        vendor_multimodal_model_name: str | Omit = omit,
        version: str | Omit = omit,
        webhook_configurations: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Upload File

        Args:
          parse_mode: Enum for representing the mode of parsing to be used

          replace_failed_page_mode: Enum for representing the different available page error handling modes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "adaptive_long_table": adaptive_long_table,
                "aggressive_table_extraction": aggressive_table_extraction,
                "annotate_links": annotate_links,
                "auto_mode": auto_mode,
                "auto_mode_configuration_json": auto_mode_configuration_json,
                "auto_mode_trigger_on_image_in_page": auto_mode_trigger_on_image_in_page,
                "auto_mode_trigger_on_regexp_in_page": auto_mode_trigger_on_regexp_in_page,
                "auto_mode_trigger_on_table_in_page": auto_mode_trigger_on_table_in_page,
                "auto_mode_trigger_on_text_in_page": auto_mode_trigger_on_text_in_page,
                "azure_openai_api_version": azure_openai_api_version,
                "azure_openai_deployment_name": azure_openai_deployment_name,
                "azure_openai_endpoint": azure_openai_endpoint,
                "azure_openai_key": azure_openai_key,
                "bbox_bottom": bbox_bottom,
                "bbox_left": bbox_left,
                "bbox_right": bbox_right,
                "bbox_top": bbox_top,
                "bounding_box": bounding_box,
                "compact_markdown_table": compact_markdown_table,
                "complemental_formatting_instruction": complemental_formatting_instruction,
                "content_guideline_instruction": content_guideline_instruction,
                "continuous_mode": continuous_mode,
                "disable_image_extraction": disable_image_extraction,
                "disable_ocr": disable_ocr,
                "disable_reconstruction": disable_reconstruction,
                "do_not_cache": do_not_cache,
                "do_not_unroll_columns": do_not_unroll_columns,
                "extract_charts": extract_charts,
                "extract_layout": extract_layout,
                "extract_printed_page_number": extract_printed_page_number,
                "fast_mode": fast_mode,
                "file": file,
                "formatting_instruction": formatting_instruction,
                "gpt4o_api_key": gpt4o_api_key,
                "gpt4o_mode": gpt4o_mode,
                "guess_xlsx_sheet_name": guess_xlsx_sheet_name,
                "hide_footers": hide_footers,
                "hide_headers": hide_headers,
                "high_res_ocr": high_res_ocr,
                "html_make_all_elements_visible": html_make_all_elements_visible,
                "html_remove_fixed_elements": html_remove_fixed_elements,
                "html_remove_navigation_elements": html_remove_navigation_elements,
                "http_proxy": http_proxy,
                "ignore_document_elements_for_layout_detection": ignore_document_elements_for_layout_detection,
                "inline_images_in_markdown": inline_images_in_markdown,
                "input_s3_path": input_s3_path,
                "input_s3_region": input_s3_region,
                "input_url": input_url,
                "invalidate_cache": invalidate_cache,
                "is_formatting_instruction": is_formatting_instruction,
                "job_timeout_extra_time_per_page_in_seconds": job_timeout_extra_time_per_page_in_seconds,
                "job_timeout_in_seconds": job_timeout_in_seconds,
                "keep_page_separator_when_merging_tables": keep_page_separator_when_merging_tables,
                "language": language,
                "layout_aware": layout_aware,
                "line_level_bounding_box": line_level_bounding_box,
                "markdown_table_multiline_header_separator": markdown_table_multiline_header_separator,
                "max_pages": max_pages,
                "merge_tables_across_pages_in_markdown": merge_tables_across_pages_in_markdown,
                "model": model,
                "outlined_table_extraction": outlined_table_extraction,
                "output_pdf_of_document": output_pdf_of_document,
                "output_s3_path_prefix": output_s3_path_prefix,
                "output_s3_region": output_s3_region,
                "output_tables_as_html": output_tables_as_html,
                "page_error_tolerance": page_error_tolerance,
                "page_footer_prefix": page_footer_prefix,
                "page_footer_suffix": page_footer_suffix,
                "page_header_prefix": page_header_prefix,
                "page_header_suffix": page_header_suffix,
                "page_prefix": page_prefix,
                "page_separator": page_separator,
                "page_suffix": page_suffix,
                "parse_mode": parse_mode,
                "parsing_instruction": parsing_instruction,
                "precise_bounding_box": precise_bounding_box,
                "premium_mode": premium_mode,
                "presentation_out_of_bounds_content": presentation_out_of_bounds_content,
                "preserve_layout_alignment_across_pages": preserve_layout_alignment_across_pages,
                "preserve_very_small_text": preserve_very_small_text,
                "preset": preset,
                "remove_hidden_text": remove_hidden_text,
                "replace_failed_page_mode": replace_failed_page_mode,
                "replace_failed_page_with_error_message_prefix": replace_failed_page_with_error_message_prefix,
                "replace_failed_page_with_error_message_suffix": replace_failed_page_with_error_message_suffix,
                "save_images": save_images,
                "skip_diagonal_text": skip_diagonal_text,
                "specialized_chart_parsing_agentic": specialized_chart_parsing_agentic,
                "specialized_chart_parsing_efficient": specialized_chart_parsing_efficient,
                "specialized_chart_parsing_plus": specialized_chart_parsing_plus,
                "specialized_image_parsing": specialized_image_parsing,
                "spreadsheet_extract_sub_tables": spreadsheet_extract_sub_tables,
                "spreadsheet_force_formula_computation": spreadsheet_force_formula_computation,
                "strict_mode_buggy_font": strict_mode_buggy_font,
                "strict_mode_image_extraction": strict_mode_image_extraction,
                "strict_mode_image_ocr": strict_mode_image_ocr,
                "strict_mode_reconstruction": strict_mode_reconstruction,
                "structured_output": structured_output,
                "structured_output_json_schema": structured_output_json_schema,
                "structured_output_json_schema_name": structured_output_json_schema_name,
                "system_prompt": system_prompt,
                "system_prompt_append": system_prompt_append,
                "take_screenshot": take_screenshot,
                "target_pages": target_pages,
                "tier": tier,
                "use_vendor_multimodal_model": use_vendor_multimodal_model,
                "user_prompt": user_prompt,
                "vendor_multimodal_api_key": vendor_multimodal_api_key,
                "vendor_multimodal_model_name": vendor_multimodal_model_name,
                "version": version,
                "webhook_configurations": webhook_configurations,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/parsing/upload",
            body=maybe_transform(body, parsing_upload_file_params.ParsingUploadFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_upload_file_params.ParsingUploadFileParams,
                ),
            ),
            cast_to=ParsingJob,
        )

    def parse(
        self,
        *,
        result_type: Literal["markdown", "text", "json", "structured"] = "markdown",
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        **upload_params: Unpack[ParsingUploadFileParams],
    ) -> Union[ParsingJobMarkdownResult, ParsingJobTextResult, ParsingJobJsonResult, ParsingJobStructuredResult]:
        """
        Upload a file for parsing and wait for it to complete, returning the result.

        This is a convenience method that combines upload_file(), wait_for_completion(),
        and result.get_*() into a single call for the most common end-to-end workflow.

        Args:
            result_type: The type of result to return. Options:
                - "markdown": Return markdown formatted result (default)
                - "text": Return plain text result
                - "json": Return JSON formatted result
                - "structured": Return structured data result

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            **upload_params: All parameters accepted by upload_file(), including:
                - file: The file to parse
                - organization_id: Optional organization ID
                - project_id: Optional project ID
                - parse_mode: Parsing mode to use
                - And 100+ other parsing configuration options

        Returns:
            The parsing result in the requested format

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: upload, wait, and get markdown result
            result = client.parsing.upload_file_and_wait(
                file=open("document.pdf", "rb"), result_type="markdown", verbose=True
            )

            print(result.markdown)
            ```
        """
        # Upload the file
        job = self.upload_file(**upload_params)

        # Wait for completion
        self.job.wait_for_completion(
            job.id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )

        # Get and return the result in the requested format
        organization_id = upload_params.get("organization_id")
        if job.status != "SUCCESS":
            return self.job.result.get_json(job.id, organization_id=organization_id)
        elif result_type == "markdown":
            return self.job.result.get_markdown(job.id, organization_id=organization_id)
        elif result_type == "text":
            return self.job.result.get_text(job.id, organization_id=organization_id)
        elif result_type == "json":
            return self.job.result.get_json(job.id, organization_id=organization_id)
        elif result_type == "structured":
            return self.job.result.get_structured(job.id, organization_id=organization_id)
        else:
            raise ValueError(f"Invalid result_type: {result_type}")


class AsyncParsingResource(AsyncAPIResource):
    @cached_property
    def job(self) -> AsyncJobResource:
        return AsyncJobResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#accessing-raw-response-data-eg-headers
        """
        return AsyncParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-cloud-py#with_streaming_response
        """
        return AsyncParsingResourceWithStreamingResponse(self)

    async def create_screenshot(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        do_not_cache: bool | Omit = omit,
        file: Optional[FileTypes] | Omit = omit,
        http_proxy: str | Omit = omit,
        input_s3_path: str | Omit = omit,
        input_s3_region: str | Omit = omit,
        input_url: str | Omit = omit,
        invalidate_cache: bool | Omit = omit,
        job_timeout_extra_time_per_page_in_seconds: float | Omit = omit,
        job_timeout_in_seconds: float | Omit = omit,
        max_pages: Optional[int] | Omit = omit,
        output_s3_path_prefix: str | Omit = omit,
        output_s3_region: str | Omit = omit,
        target_pages: str | Omit = omit,
        webhook_configurations: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Screenshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "do_not_cache": do_not_cache,
                "file": file,
                "http_proxy": http_proxy,
                "input_s3_path": input_s3_path,
                "input_s3_region": input_s3_region,
                "input_url": input_url,
                "invalidate_cache": invalidate_cache,
                "job_timeout_extra_time_per_page_in_seconds": job_timeout_extra_time_per_page_in_seconds,
                "job_timeout_in_seconds": job_timeout_in_seconds,
                "max_pages": max_pages,
                "output_s3_path_prefix": output_s3_path_prefix,
                "output_s3_region": output_s3_region,
                "target_pages": target_pages,
                "webhook_configurations": webhook_configurations,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/parsing/screenshot",
            body=await async_maybe_transform(body, parsing_create_screenshot_params.ParsingCreateScreenshotParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_create_screenshot_params.ParsingCreateScreenshotParams,
                ),
            ),
            cast_to=ParsingJob,
        )

    async def get_supported_file_extensions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetSupportedFileExtensionsResponse:
        """Get a list of supported file extensions"""
        return await self._get(
            "/api/v1/parsing/supported_file_extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingGetSupportedFileExtensionsResponse,
        )

    async def upload_file(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        adaptive_long_table: bool | Omit = omit,
        aggressive_table_extraction: bool | Omit = omit,
        annotate_links: bool | Omit = omit,
        auto_mode: bool | Omit = omit,
        auto_mode_configuration_json: str | Omit = omit,
        auto_mode_trigger_on_image_in_page: bool | Omit = omit,
        auto_mode_trigger_on_regexp_in_page: str | Omit = omit,
        auto_mode_trigger_on_table_in_page: bool | Omit = omit,
        auto_mode_trigger_on_text_in_page: str | Omit = omit,
        azure_openai_api_version: str | Omit = omit,
        azure_openai_deployment_name: str | Omit = omit,
        azure_openai_endpoint: str | Omit = omit,
        azure_openai_key: str | Omit = omit,
        bbox_bottom: float | Omit = omit,
        bbox_left: float | Omit = omit,
        bbox_right: float | Omit = omit,
        bbox_top: float | Omit = omit,
        bounding_box: str | Omit = omit,
        compact_markdown_table: bool | Omit = omit,
        complemental_formatting_instruction: str | Omit = omit,
        content_guideline_instruction: str | Omit = omit,
        continuous_mode: bool | Omit = omit,
        disable_image_extraction: bool | Omit = omit,
        disable_ocr: bool | Omit = omit,
        disable_reconstruction: bool | Omit = omit,
        do_not_cache: bool | Omit = omit,
        do_not_unroll_columns: bool | Omit = omit,
        extract_charts: bool | Omit = omit,
        extract_layout: bool | Omit = omit,
        extract_printed_page_number: bool | Omit = omit,
        fast_mode: bool | Omit = omit,
        file: Optional[FileTypes] | Omit = omit,
        formatting_instruction: str | Omit = omit,
        gpt4o_api_key: str | Omit = omit,
        gpt4o_mode: bool | Omit = omit,
        guess_xlsx_sheet_name: bool | Omit = omit,
        hide_footers: bool | Omit = omit,
        hide_headers: bool | Omit = omit,
        high_res_ocr: bool | Omit = omit,
        html_make_all_elements_visible: bool | Omit = omit,
        html_remove_fixed_elements: bool | Omit = omit,
        html_remove_navigation_elements: bool | Omit = omit,
        http_proxy: str | Omit = omit,
        ignore_document_elements_for_layout_detection: bool | Omit = omit,
        inline_images_in_markdown: bool | Omit = omit,
        input_s3_path: str | Omit = omit,
        input_s3_region: str | Omit = omit,
        input_url: str | Omit = omit,
        invalidate_cache: bool | Omit = omit,
        is_formatting_instruction: bool | Omit = omit,
        job_timeout_extra_time_per_page_in_seconds: float | Omit = omit,
        job_timeout_in_seconds: float | Omit = omit,
        keep_page_separator_when_merging_tables: bool | Omit = omit,
        language: List[ParserLanguages] | Omit = omit,
        layout_aware: bool | Omit = omit,
        line_level_bounding_box: bool | Omit = omit,
        markdown_table_multiline_header_separator: str | Omit = omit,
        max_pages: Optional[int] | Omit = omit,
        merge_tables_across_pages_in_markdown: bool | Omit = omit,
        model: str | Omit = omit,
        outlined_table_extraction: bool | Omit = omit,
        output_pdf_of_document: bool | Omit = omit,
        output_s3_path_prefix: str | Omit = omit,
        output_s3_region: str | Omit = omit,
        output_tables_as_html: bool | Omit = omit,
        page_error_tolerance: float | Omit = omit,
        page_footer_prefix: str | Omit = omit,
        page_footer_suffix: str | Omit = omit,
        page_header_prefix: str | Omit = omit,
        page_header_suffix: str | Omit = omit,
        page_prefix: str | Omit = omit,
        page_separator: str | Omit = omit,
        page_suffix: str | Omit = omit,
        parse_mode: Optional[ParsingMode] | Omit = omit,
        parsing_instruction: str | Omit = omit,
        precise_bounding_box: bool | Omit = omit,
        premium_mode: bool | Omit = omit,
        presentation_out_of_bounds_content: bool | Omit = omit,
        preserve_layout_alignment_across_pages: bool | Omit = omit,
        preserve_very_small_text: bool | Omit = omit,
        preset: str | Omit = omit,
        remove_hidden_text: bool | Omit = omit,
        replace_failed_page_mode: Optional[FailPageMode] | Omit = omit,
        replace_failed_page_with_error_message_prefix: str | Omit = omit,
        replace_failed_page_with_error_message_suffix: str | Omit = omit,
        save_images: bool | Omit = omit,
        skip_diagonal_text: bool | Omit = omit,
        specialized_chart_parsing_agentic: bool | Omit = omit,
        specialized_chart_parsing_efficient: bool | Omit = omit,
        specialized_chart_parsing_plus: bool | Omit = omit,
        specialized_image_parsing: bool | Omit = omit,
        spreadsheet_extract_sub_tables: bool | Omit = omit,
        spreadsheet_force_formula_computation: bool | Omit = omit,
        strict_mode_buggy_font: bool | Omit = omit,
        strict_mode_image_extraction: bool | Omit = omit,
        strict_mode_image_ocr: bool | Omit = omit,
        strict_mode_reconstruction: bool | Omit = omit,
        structured_output: bool | Omit = omit,
        structured_output_json_schema: str | Omit = omit,
        structured_output_json_schema_name: str | Omit = omit,
        system_prompt: str | Omit = omit,
        system_prompt_append: str | Omit = omit,
        take_screenshot: bool | Omit = omit,
        target_pages: str | Omit = omit,
        tier: str | Omit = omit,
        use_vendor_multimodal_model: bool | Omit = omit,
        user_prompt: str | Omit = omit,
        vendor_multimodal_api_key: str | Omit = omit,
        vendor_multimodal_model_name: str | Omit = omit,
        version: str | Omit = omit,
        webhook_configurations: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Upload File

        Args:
          parse_mode: Enum for representing the mode of parsing to be used

          replace_failed_page_mode: Enum for representing the different available page error handling modes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "adaptive_long_table": adaptive_long_table,
                "aggressive_table_extraction": aggressive_table_extraction,
                "annotate_links": annotate_links,
                "auto_mode": auto_mode,
                "auto_mode_configuration_json": auto_mode_configuration_json,
                "auto_mode_trigger_on_image_in_page": auto_mode_trigger_on_image_in_page,
                "auto_mode_trigger_on_regexp_in_page": auto_mode_trigger_on_regexp_in_page,
                "auto_mode_trigger_on_table_in_page": auto_mode_trigger_on_table_in_page,
                "auto_mode_trigger_on_text_in_page": auto_mode_trigger_on_text_in_page,
                "azure_openai_api_version": azure_openai_api_version,
                "azure_openai_deployment_name": azure_openai_deployment_name,
                "azure_openai_endpoint": azure_openai_endpoint,
                "azure_openai_key": azure_openai_key,
                "bbox_bottom": bbox_bottom,
                "bbox_left": bbox_left,
                "bbox_right": bbox_right,
                "bbox_top": bbox_top,
                "bounding_box": bounding_box,
                "compact_markdown_table": compact_markdown_table,
                "complemental_formatting_instruction": complemental_formatting_instruction,
                "content_guideline_instruction": content_guideline_instruction,
                "continuous_mode": continuous_mode,
                "disable_image_extraction": disable_image_extraction,
                "disable_ocr": disable_ocr,
                "disable_reconstruction": disable_reconstruction,
                "do_not_cache": do_not_cache,
                "do_not_unroll_columns": do_not_unroll_columns,
                "extract_charts": extract_charts,
                "extract_layout": extract_layout,
                "extract_printed_page_number": extract_printed_page_number,
                "fast_mode": fast_mode,
                "file": file,
                "formatting_instruction": formatting_instruction,
                "gpt4o_api_key": gpt4o_api_key,
                "gpt4o_mode": gpt4o_mode,
                "guess_xlsx_sheet_name": guess_xlsx_sheet_name,
                "hide_footers": hide_footers,
                "hide_headers": hide_headers,
                "high_res_ocr": high_res_ocr,
                "html_make_all_elements_visible": html_make_all_elements_visible,
                "html_remove_fixed_elements": html_remove_fixed_elements,
                "html_remove_navigation_elements": html_remove_navigation_elements,
                "http_proxy": http_proxy,
                "ignore_document_elements_for_layout_detection": ignore_document_elements_for_layout_detection,
                "inline_images_in_markdown": inline_images_in_markdown,
                "input_s3_path": input_s3_path,
                "input_s3_region": input_s3_region,
                "input_url": input_url,
                "invalidate_cache": invalidate_cache,
                "is_formatting_instruction": is_formatting_instruction,
                "job_timeout_extra_time_per_page_in_seconds": job_timeout_extra_time_per_page_in_seconds,
                "job_timeout_in_seconds": job_timeout_in_seconds,
                "keep_page_separator_when_merging_tables": keep_page_separator_when_merging_tables,
                "language": language,
                "layout_aware": layout_aware,
                "line_level_bounding_box": line_level_bounding_box,
                "markdown_table_multiline_header_separator": markdown_table_multiline_header_separator,
                "max_pages": max_pages,
                "merge_tables_across_pages_in_markdown": merge_tables_across_pages_in_markdown,
                "model": model,
                "outlined_table_extraction": outlined_table_extraction,
                "output_pdf_of_document": output_pdf_of_document,
                "output_s3_path_prefix": output_s3_path_prefix,
                "output_s3_region": output_s3_region,
                "output_tables_as_html": output_tables_as_html,
                "page_error_tolerance": page_error_tolerance,
                "page_footer_prefix": page_footer_prefix,
                "page_footer_suffix": page_footer_suffix,
                "page_header_prefix": page_header_prefix,
                "page_header_suffix": page_header_suffix,
                "page_prefix": page_prefix,
                "page_separator": page_separator,
                "page_suffix": page_suffix,
                "parse_mode": parse_mode,
                "parsing_instruction": parsing_instruction,
                "precise_bounding_box": precise_bounding_box,
                "premium_mode": premium_mode,
                "presentation_out_of_bounds_content": presentation_out_of_bounds_content,
                "preserve_layout_alignment_across_pages": preserve_layout_alignment_across_pages,
                "preserve_very_small_text": preserve_very_small_text,
                "preset": preset,
                "remove_hidden_text": remove_hidden_text,
                "replace_failed_page_mode": replace_failed_page_mode,
                "replace_failed_page_with_error_message_prefix": replace_failed_page_with_error_message_prefix,
                "replace_failed_page_with_error_message_suffix": replace_failed_page_with_error_message_suffix,
                "save_images": save_images,
                "skip_diagonal_text": skip_diagonal_text,
                "specialized_chart_parsing_agentic": specialized_chart_parsing_agentic,
                "specialized_chart_parsing_efficient": specialized_chart_parsing_efficient,
                "specialized_chart_parsing_plus": specialized_chart_parsing_plus,
                "specialized_image_parsing": specialized_image_parsing,
                "spreadsheet_extract_sub_tables": spreadsheet_extract_sub_tables,
                "spreadsheet_force_formula_computation": spreadsheet_force_formula_computation,
                "strict_mode_buggy_font": strict_mode_buggy_font,
                "strict_mode_image_extraction": strict_mode_image_extraction,
                "strict_mode_image_ocr": strict_mode_image_ocr,
                "strict_mode_reconstruction": strict_mode_reconstruction,
                "structured_output": structured_output,
                "structured_output_json_schema": structured_output_json_schema,
                "structured_output_json_schema_name": structured_output_json_schema_name,
                "system_prompt": system_prompt,
                "system_prompt_append": system_prompt_append,
                "take_screenshot": take_screenshot,
                "target_pages": target_pages,
                "tier": tier,
                "use_vendor_multimodal_model": use_vendor_multimodal_model,
                "user_prompt": user_prompt,
                "vendor_multimodal_api_key": vendor_multimodal_api_key,
                "vendor_multimodal_model_name": vendor_multimodal_model_name,
                "version": version,
                "webhook_configurations": webhook_configurations,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/parsing/upload",
            body=await async_maybe_transform(body, parsing_upload_file_params.ParsingUploadFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_upload_file_params.ParsingUploadFileParams,
                ),
            ),
            cast_to=ParsingJob,
        )

    async def parse(
        self,
        *,
        result_type: Literal["markdown", "text", "json", "structured"] = "markdown",
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = 2000.0,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        **upload_params: Unpack[ParsingUploadFileParams],
    ) -> Union[ParsingJobMarkdownResult, ParsingJobTextResult, ParsingJobJsonResult, ParsingJobStructuredResult]:
        """
        Upload a file for parsing and wait for it to complete, returning the result.

        This is a convenience method that combines upload_file(), wait_for_completion(),
        and result.get_*() into a single call for the most common end-to-end workflow.

        Args:
            result_type: The type of result to return. Options:
                - "markdown": Return markdown formatted result (default)
                - "text": Return plain text result
                - "json": Return JSON formatted result
                - "structured": Return structured data result

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            **upload_params: All parameters accepted by upload_file(), including:
                - file: The file to parse
                - organization_id: Optional organization ID
                - project_id: Optional project ID
                - parse_mode: Parsing mode to use
                - And 100+ other parsing configuration options

        Returns:
            The parsing result in the requested format

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: upload, wait, and get markdown result
            result = await client.parsing.upload_file_and_wait(
                file=open("document.pdf", "rb"), result_type="markdown", verbose=True
            )

            print(result.markdown)
            ```
        """
        # Upload the file
        job = await self.upload_file(**upload_params)

        # Wait for completion
        job = await self.job.wait_for_completion(
            job.id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )

        # Get and return the result in the requested format
        organization_id = upload_params.get("organization_id")
        if job.status != "SUCCESS":
            return await self.job.result.get_json(job.id, organization_id=organization_id)
        elif result_type == "markdown":
            return await self.job.result.get_markdown(job.id, organization_id=organization_id)
        elif result_type == "text":
            return await self.job.result.get_text(job.id, organization_id=organization_id)
        elif result_type == "json":
            return await self.job.result.get_json(job.id, organization_id=organization_id)
        elif result_type == "structured":
            return await self.job.result.get_structured(job.id, organization_id=organization_id)
        else:
            raise ValueError(f"Invalid result_type: {result_type}")


class ParsingResourceWithRawResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create_screenshot = to_raw_response_wrapper(
            parsing.create_screenshot,
        )
        self.get_supported_file_extensions = to_raw_response_wrapper(
            parsing.get_supported_file_extensions,
        )
        self.upload_file = to_raw_response_wrapper(
            parsing.upload_file,
        )

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._parsing.job)


class AsyncParsingResourceWithRawResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create_screenshot = async_to_raw_response_wrapper(
            parsing.create_screenshot,
        )
        self.get_supported_file_extensions = async_to_raw_response_wrapper(
            parsing.get_supported_file_extensions,
        )
        self.upload_file = async_to_raw_response_wrapper(
            parsing.upload_file,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._parsing.job)


class ParsingResourceWithStreamingResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create_screenshot = to_streamed_response_wrapper(
            parsing.create_screenshot,
        )
        self.get_supported_file_extensions = to_streamed_response_wrapper(
            parsing.get_supported_file_extensions,
        )
        self.upload_file = to_streamed_response_wrapper(
            parsing.upload_file,
        )

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._parsing.job)


class AsyncParsingResourceWithStreamingResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create_screenshot = async_to_streamed_response_wrapper(
            parsing.create_screenshot,
        )
        self.get_supported_file_extensions = async_to_streamed_response_wrapper(
            parsing.get_supported_file_extensions,
        )
        self.upload_file = async_to_streamed_response_wrapper(
            parsing.upload_file,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._parsing.job)
