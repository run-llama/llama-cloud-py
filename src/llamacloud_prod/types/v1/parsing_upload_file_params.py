# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo
from .parsing_mode import ParsingMode
from .fail_page_mode import FailPageMode
from .parser_languages import ParserLanguages

__all__ = ["ParsingUploadFileParams"]


class ParsingUploadFileParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    adaptive_long_table: bool

    aggressive_table_extraction: bool

    annotate_links: bool

    auto_mode: bool

    auto_mode_configuration_json: str

    auto_mode_trigger_on_image_in_page: bool

    auto_mode_trigger_on_regexp_in_page: str

    auto_mode_trigger_on_table_in_page: bool

    auto_mode_trigger_on_text_in_page: str

    azure_openai_api_version: str

    azure_openai_deployment_name: str

    azure_openai_endpoint: str

    azure_openai_key: str

    bbox_bottom: float

    bbox_left: float

    bbox_right: float

    bbox_top: float

    bounding_box: str

    compact_markdown_table: bool

    complemental_formatting_instruction: str

    content_guideline_instruction: str

    continuous_mode: bool

    disable_image_extraction: bool

    disable_ocr: bool

    disable_reconstruction: bool

    do_not_cache: bool

    do_not_unroll_columns: bool

    extract_charts: bool

    extract_layout: bool

    fast_mode: bool

    file: Optional[FileTypes]

    formatting_instruction: str

    gpt4o_api_key: str

    gpt4o_mode: bool

    guess_xlsx_sheet_name: bool

    hide_footers: bool

    hide_headers: bool

    high_res_ocr: bool

    html_make_all_elements_visible: bool

    html_remove_fixed_elements: bool

    html_remove_navigation_elements: bool

    http_proxy: str

    ignore_document_elements_for_layout_detection: bool

    inline_images_in_markdown: bool

    input_s3_path: str

    input_s3_region: str

    input_url: str

    invalidate_cache: bool

    is_formatting_instruction: bool

    job_timeout_extra_time_per_page_in_seconds: float

    job_timeout_in_seconds: float

    keep_page_separator_when_merging_tables: bool

    language: List[ParserLanguages]

    layout_aware: bool

    markdown_table_multiline_header_separator: str

    max_pages: Optional[int]

    merge_tables_across_pages_in_markdown: bool

    model: str

    outlined_table_extraction: bool

    output_pdf_of_document: bool

    output_s3_path_prefix: str

    output_s3_region: str

    output_tables_as_html: Annotated[bool, PropertyInfo(alias="output_tables_as_HTML")]

    page_error_tolerance: float

    page_footer_prefix: str

    page_footer_suffix: str

    page_header_prefix: str

    page_header_suffix: str

    page_prefix: str

    page_separator: str

    page_suffix: str

    parse_mode: Optional[ParsingMode]
    """Enum for representing the mode of parsing to be used"""

    parsing_instruction: str

    precise_bounding_box: bool

    premium_mode: bool

    preserve_layout_alignment_across_pages: bool

    preserve_very_small_text: bool

    preset: str

    remove_hidden_text: bool

    replace_failed_page_mode: Optional[FailPageMode]
    """Enum for representing the different available page error handling modes"""

    replace_failed_page_with_error_message_prefix: str

    replace_failed_page_with_error_message_suffix: str

    save_images: bool

    skip_diagonal_text: bool

    specialized_chart_parsing_agentic: bool

    specialized_chart_parsing_efficient: bool

    specialized_chart_parsing_plus: bool

    specialized_image_parsing: bool

    spreadsheet_extract_sub_tables: bool

    spreadsheet_force_formula_computation: bool

    strict_mode_buggy_font: bool

    strict_mode_image_extraction: bool

    strict_mode_image_ocr: bool

    strict_mode_reconstruction: bool

    structured_output: bool

    structured_output_json_schema: str

    structured_output_json_schema_name: str

    system_prompt: str

    system_prompt_append: str

    take_screenshot: bool

    target_pages: str

    use_vendor_multimodal_model: bool

    user_prompt: str

    vendor_multimodal_api_key: str

    vendor_multimodal_model_name: str

    webhook_configurations: str

    webhook_url: str
