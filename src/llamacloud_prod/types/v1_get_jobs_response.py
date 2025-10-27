# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .delete_params import DeleteParams
from .v1.status_enum import StatusEnum
from .v1.parsing_mode import ParsingMode
from .v1.fail_page_mode import FailPageMode
from .v1.parser_languages import ParserLanguages
from .v1.extraction.webhook_configuration import WebhookConfiguration

__all__ = [
    "V1GetJobsResponse",
    "Job",
    "JobJobRecord",
    "JobJobRecordParameters",
    "JobJobRecordParametersParseJobConfig",
    "JobJobRecordParametersLegacyParseJobConfig",
    "JobJobRecordParametersLoadFilesJobConfig",
    "JobJobRecordParametersLLamaParseTransformConfig",
    "JobJobRecordParametersPipelineManagedIngestionJobParams",
    "JobJobRecordParametersDataSourceUpdateDispatcherConfig",
    "JobJobRecordParametersPipelineFileUpdaterConfig",
    "JobJobRecordParametersDocumentIngestionJobParams",
    "JobUser",
    "JobUsageMetrics",
]


class JobJobRecordParametersParseJobConfig(BaseModel):
    file_key: str
    """The file key."""

    file_name: str
    """The file name."""

    lang: str
    """The language."""

    original_file_name: str
    """The original file name."""

    adaptive_long_table: Optional[bool] = None

    aggressive_table_extraction: Optional[bool] = None

    annotate_links: Optional[bool] = None

    auto_mode: Optional[bool] = None

    auto_mode_configuration_json: Optional[str] = None

    auto_mode_trigger_on_image_in_page: Optional[bool] = None

    auto_mode_trigger_on_regexp_in_page: Optional[str] = None

    auto_mode_trigger_on_table_in_page: Optional[bool] = None

    auto_mode_trigger_on_text_in_page: Optional[str] = None

    azure_openai_api_version: Optional[str] = None

    azure_openai_deployment_name: Optional[str] = None

    azure_openai_endpoint: Optional[str] = None

    azure_openai_key: Optional[str] = None

    bbox_bottom: Optional[float] = None

    bbox_left: Optional[float] = None

    bbox_right: Optional[float] = None

    bbox_top: Optional[float] = None

    bounding_box: Optional[str] = None

    compact_markdown_table: Optional[bool] = None

    complemental_formatting_instruction: Optional[str] = None

    content_guideline_instruction: Optional[str] = None

    continuous_mode: Optional[bool] = None

    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the documents."""

    disable_image_extraction: Optional[bool] = None

    disable_ocr: Optional[bool] = None

    disable_reconstruction: Optional[bool] = None

    do_not_cache: Optional[bool] = None

    do_not_unroll_columns: Optional[bool] = None

    extract_charts: Optional[bool] = None

    extract_layout: Optional[bool] = None

    fast_mode: Optional[bool] = None

    file_id: Optional[str] = None
    """The file ID."""

    formatting_instruction: Optional[str] = None

    gpt4o_api_key: Optional[str] = None

    gpt4o_mode: Optional[bool] = None

    guess_xlsx_sheet_name: Optional[bool] = None

    hide_footers: Optional[bool] = None

    hide_headers: Optional[bool] = None

    high_res_ocr: Optional[bool] = None

    html_make_all_elements_visible: Optional[bool] = None

    html_remove_fixed_elements: Optional[bool] = None

    html_remove_navigation_elements: Optional[bool] = None

    http_proxy: Optional[str] = None

    ignore_document_elements_for_layout_detection: Optional[bool] = None

    inline_images_in_markdown: Optional[bool] = None

    input_s3_path: Optional[str] = None
    """If specified, llamaParse will take the specified file.

    should be a valid s3:// url
    """

    input_s3_region: Optional[str] = None
    """The region for the input S3 bucket."""

    input_url: Optional[str] = None

    internal_is_screenshot_job: Optional[bool] = None

    invalidate_cache: Optional[bool] = None

    is_formatting_instruction: Optional[bool] = None

    job_timeout_extra_time_per_page_in_seconds: Optional[float] = None

    job_timeout_in_seconds: Optional[float] = None

    keep_page_separator_when_merging_tables: Optional[bool] = None

    languages: Optional[List[ParserLanguages]] = None

    layout_aware: Optional[bool] = None

    markdown_table_multiline_header_separator: Optional[str] = None

    max_pages: Optional[int] = None

    max_pages_enforced: Optional[int] = None

    merge_tables_across_pages_in_markdown: Optional[bool] = None

    model: Optional[str] = None

    outlined_table_extraction: Optional[bool] = None

    output_pdf_of_document: Optional[bool] = None

    output_s3_path_prefix: Optional[str] = None
    """If specified, llamaParse will save the output to the specified path.

    All output file will use this 'prefix' should be a valid s3:// url
    """

    output_s3_region: Optional[str] = None
    """The region for the output S3 bucket."""

    output_tables_as_html: Optional[bool] = FieldInfo(alias="output_tables_as_HTML", default=None)

    output_bucket: Optional[str] = FieldInfo(alias="outputBucket", default=None)
    """The output bucket."""

    page_error_tolerance: Optional[float] = None

    page_footer_prefix: Optional[str] = None

    page_footer_suffix: Optional[str] = None

    page_header_prefix: Optional[str] = None

    page_header_suffix: Optional[str] = None

    page_prefix: Optional[str] = None

    page_separator: Optional[str] = None

    page_suffix: Optional[str] = None

    parse_mode: Optional[ParsingMode] = None
    """Enum for representing the mode of parsing to be used"""

    parsing_instruction: Optional[str] = None

    pipeline_id: Optional[str] = None
    """The pipeline ID."""

    precise_bounding_box: Optional[bool] = None

    premium_mode: Optional[bool] = None

    preserve_layout_alignment_across_pages: Optional[bool] = None

    preserve_very_small_text: Optional[bool] = None

    preset: Optional[str] = None

    priority: Optional[Literal["low", "medium", "high", "critical"]] = None
    """The priority for the request.

    This field may be ignored or overwritten depending on the organization tier.
    """

    project_id: Optional[str] = None

    remove_hidden_text: Optional[bool] = None

    replace_failed_page_mode: Optional[FailPageMode] = None
    """Enum for representing the different available page error handling modes"""

    replace_failed_page_with_error_message_prefix: Optional[str] = None

    replace_failed_page_with_error_message_suffix: Optional[str] = None

    resource_info: Optional[Dict[str, object]] = None
    """The resource info about the file"""

    save_images: Optional[bool] = None

    skip_diagonal_text: Optional[bool] = None

    specialized_chart_parsing_agentic: Optional[bool] = None

    specialized_chart_parsing_efficient: Optional[bool] = None

    specialized_chart_parsing_plus: Optional[bool] = None

    specialized_image_parsing: Optional[bool] = None

    spreadsheet_extract_sub_tables: Optional[bool] = None

    spreadsheet_force_formula_computation: Optional[bool] = None

    strict_mode_buggy_font: Optional[bool] = None

    strict_mode_image_extraction: Optional[bool] = None

    strict_mode_image_ocr: Optional[bool] = None

    strict_mode_reconstruction: Optional[bool] = None

    structured_output: Optional[bool] = None

    structured_output_json_schema: Optional[str] = None

    structured_output_json_schema_name: Optional[str] = None

    system_prompt: Optional[str] = None

    system_prompt_append: Optional[str] = None

    take_screenshot: Optional[bool] = None

    target_pages: Optional[str] = None

    type: Optional[Literal["parse"]] = None

    use_vendor_multimodal_model: Optional[bool] = None

    user_prompt: Optional[str] = None

    vendor_multimodal_api_key: Optional[str] = None

    vendor_multimodal_model_name: Optional[str] = None

    webhook_configurations: Optional[List[WebhookConfiguration]] = None
    """The outbound webhook configurations"""

    webhook_url: Optional[str] = None


class JobJobRecordParametersLegacyParseJobConfig(BaseModel):
    file_key: str = FieldInfo(alias="fileKey")
    """The file key."""

    file_name: str = FieldInfo(alias="fileName")
    """The file name."""

    invalidate_cache: bool = FieldInfo(alias="invalidateCache")
    """Whether to invalidate the cache."""

    lang: str
    """The language."""

    open_aiapi_key: str = FieldInfo(alias="openAIAPIKey")
    """The OpenAI API key."""

    original_file_name: str = FieldInfo(alias="originalFileName")
    """The original file name."""

    user_id: str = FieldInfo(alias="userId")
    """The user ID."""

    adaptive_long_table: Optional[bool] = FieldInfo(alias="adaptiveLongTable", default=None)
    """Adaptive long table.

    LlamaParse will try to detect long table and adapt the output.
    """

    annotate_links: Optional[bool] = FieldInfo(alias="annotateLinks", default=None)
    """Annotate links in markdown.

    LlamaParse will try to add links from document into the markdown.
    """

    auto_mode: Optional[bool] = FieldInfo(alias="autoMode", default=None)
    """Whether to use auto mode."""

    auto_mode_configuration_json: Optional[str] = FieldInfo(alias="autoModeConfigurationJSON", default=None)
    """The auto mode configuration JSON.

    This is a JSON string that contains the configuration for the auto mode.
    """

    auto_mode_trigger_on_image_in_page: Optional[bool] = FieldInfo(alias="autoModeTriggerOnImageInPage", default=None)
    """Whether to trigger on image in page."""

    auto_mode_trigger_on_regexp_in_page: Optional[str] = FieldInfo(alias="autoModeTriggerOnRegexpInPage", default=None)
    """The regexp to trigger on."""

    auto_mode_trigger_on_table_in_page: Optional[bool] = FieldInfo(alias="autoModeTriggerOnTableInPage", default=None)
    """Whether to trigger on table in page."""

    auto_mode_trigger_on_text_in_page: Optional[str] = FieldInfo(alias="autoModeTriggerOnTextInPage", default=None)
    """The text to trigger on."""

    azure_openai_api_version: Optional[str] = FieldInfo(alias="azureOpenAiApiVersion", default=None)
    """Custom azure API version."""

    azure_openai_deployment_name: Optional[str] = FieldInfo(alias="azureOpenAiDeploymentName", default=None)
    """Custom azure deployment name."""

    azure_openai_endpoint: Optional[str] = FieldInfo(alias="azureOpenAiEndpoint", default=None)
    """Custom azure endpoint."""

    azure_openai_key: Optional[str] = FieldInfo(alias="azureOpenAiKey", default=None)
    """Custom azure API key."""

    bbox_bottom: Optional[float] = FieldInfo(alias="bboxBottom", default=None)
    """The bottom side of the bounding box."""

    bbox_left: Optional[float] = FieldInfo(alias="bboxLeft", default=None)
    """The left side of the bounding box."""

    bbox_right: Optional[float] = FieldInfo(alias="bboxRight", default=None)
    """The right side of the bounding box."""

    bbox_top: Optional[float] = FieldInfo(alias="bboxTop", default=None)
    """The top side of the bounding box."""

    bounding_box: Optional[str] = FieldInfo(alias="boundingBox", default=None)
    """A string describing a bounding box to use to parse the document.

    Contain 4 value between 0 to 1 representing in clock wise order the margin top,
    right, bottom, left of the selection bounding box in ratio of the document.
    """

    compact_markdown_table: Optional[bool] = FieldInfo(alias="compactMarkdownTable", default=None)
    """Compact markdown table.

    LlamaParse will compact the markdown table to not include too many spaces.
    """

    complemental_formatting_instruction: Optional[str] = FieldInfo(
        alias="complementalFormattingInstruction", default=None
    )
    """
    A natural language instruction on how to format the result that complement
    LlamaParse default instruction.
    """

    content_guideline_instruction: Optional[str] = FieldInfo(alias="contentGuidelineInstruction", default=None)
    """
    A natural language instruction on how to transform the content of the result
    (not the format).
    """

    continuous_mode: Optional[bool] = FieldInfo(alias="continuousMode", default=None)
    """Whether to use continuousMode pipeline."""

    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the documents."""

    disable_image_extraction: Optional[bool] = FieldInfo(alias="disableImageExtraction", default=None)
    """Disable the image extraction from the document.

    LlamaParse will not extract any image from the document.
    """

    disable_ocr: Optional[bool] = FieldInfo(alias="disableOcr", default=None)
    """Disable the OCR on the document.

    LlamaParse will only extract the copyable text from the document
    """

    disable_reconstruction: Optional[bool] = FieldInfo(alias="disableReconstruction", default=None)
    """Whether to disable markdown reconstruction."""

    do_not_cache: Optional[bool] = FieldInfo(alias="doNotCache", default=None)
    """Whether to cache."""

    do_not_unroll_columns: Optional[bool] = FieldInfo(alias="doNotUnrollColumns", default=None)
    """Whether to unroll columns."""

    extract_charts: Optional[bool] = FieldInfo(alias="extractCharts", default=None)
    """Extract charts from the document."""

    extract_layout: Optional[bool] = FieldInfo(alias="extractLayout", default=None)
    """Whether to perform layout extraction."""

    fast_mode: Optional[bool] = FieldInfo(alias="fastMode", default=None)
    """Whether to use fast mode."""

    file_id: Optional[str] = FieldInfo(alias="fileId", default=None)
    """The file ID."""

    formatting_instruction: Optional[str] = FieldInfo(alias="formattingInstruction", default=None)
    """A natural language instruction on how to format the result.

    Override LlamaParse default instruction.
    """

    from_l_lama_cloud: Optional[bool] = FieldInfo(alias="fromLLamaCloud", default=None)
    """Whether the file is from LLama cloud."""

    full_file_path: Optional[str] = FieldInfo(alias="fullFilePath", default=None)
    """The full file path."""

    gpt4o: Optional[bool] = None
    """Whether to use GPT4o."""

    guess_xlsx_sheet_name: Optional[bool] = FieldInfo(alias="guessXLSXSheetName", default=None)
    """Whether to guess the XLSX sheet name when generation output xlsx."""

    hide_footers: Optional[bool] = FieldInfo(alias="hideFooters", default=None)
    """Whether to hide footers in the output."""

    hide_headers: Optional[bool] = FieldInfo(alias="hideHeaders", default=None)
    """Whether to hide headers in the output."""

    high_res_ocr: Optional[bool] = FieldInfo(alias="highResOcr", default=None)
    """Whether to use high resolution OCR (Slow)."""

    html_make_all_elements_visible: Optional[bool] = FieldInfo(alias="htmlMakeAllElementsVisible", default=None)
    """Whether to make all elements visible."""

    html_remove_fixed_elements: Optional[bool] = FieldInfo(alias="htmlRemoveFixedElements", default=None)
    """Whether to remove fixed elements."""

    html_remove_navigation_elements: Optional[bool] = FieldInfo(alias="htmlRemoveNavigationElements", default=None)
    """Whether to remove navigation elements."""

    http_proxy: Optional[str] = FieldInfo(alias="httpProxy", default=None)
    """The HTTP proxy."""

    ignore_document_elements_for_layout_detection: Optional[bool] = FieldInfo(
        alias="ignoreDocumentElementsForLayoutDetection", default=None
    )
    """
    If true, the job will ignore document element for layout detection, and instead
    just rely on a visual model, only apply to layout detection.
    """

    input_s3_path: Optional[str] = FieldInfo(alias="inputS3Path", default=None)
    """If specified, llamaParse will take the specified file.

    should be a valid s3:// url
    """

    input_s3_region: Optional[str] = FieldInfo(alias="inputS3Region", default=None)
    """The region for the input S3 bucket."""

    input_url: Optional[str] = FieldInfo(alias="inputUrl", default=None)
    """The input URL."""

    is_formatting_instruction: Optional[bool] = FieldInfo(alias="isFormattingInstruction", default=None)
    """Allow the parsing instruction to also format the output."""

    job_timeout_extra_time_per_page_in_seconds: Optional[float] = FieldInfo(
        alias="jobTimeoutExtraTimePerPageInSeconds", default=None
    )
    """Manually set additional time per page for timeout in second for a job."""

    job_timeout_in_seconds: Optional[float] = FieldInfo(alias="jobTimeoutInSeconds", default=None)
    """Manually set a timeout in second for a job. Minimum is 120"""

    max_pages: Optional[int] = FieldInfo(alias="maxPages", default=None)
    """The maximum number of pages to parse."""

    merge_tables_across_pages_in_markdown: Optional[bool] = FieldInfo(
        alias="mergeTablesAcrossPagesInMarkdown", default=None
    )
    """Whether to merge tables across pages in markdown"""

    model: Optional[str] = None
    """The model to use."""

    multimodal_model: Optional[str] = FieldInfo(alias="multimodalModel", default=None)
    """The multimodal model to use."""

    multimodal_pipeline: Optional[bool] = FieldInfo(alias="multimodalPipeline", default=None)
    """True if parsing happen in multimodal mode."""

    outlined_table_extraction: Optional[bool] = FieldInfo(alias="outlinedTableExtraction", default=None)
    """Whether to try to extract outlined tables"""

    output_bucket: Optional[str] = FieldInfo(alias="outputBucket", default=None)
    """The output bucket."""

    output_pdf_of_document: Optional[bool] = FieldInfo(alias="outputPDFOfDocument", default=None)
    """Whether to output PDF of document"""

    output_s3_path_prefix: Optional[str] = FieldInfo(alias="outputS3PathPrefix", default=None)
    """If specified, llamaParse will save the output to the specified path.

    All output file will use this 'prefix' should be a valid s3:// url
    """

    output_s3_region: Optional[str] = FieldInfo(alias="outputS3Region", default=None)
    """The region for the output S3 bucket."""

    output_tables_as_html: Optional[bool] = FieldInfo(alias="outputTablesAsHTML", default=None)
    """
    If true, the job will output tables as HTML in the markdown output, useful for
    merged cells.
    """

    page_footer_prefix: Optional[str] = FieldInfo(alias="pageFooterPrefix", default=None)
    """The page footer prefix."""

    page_footer_suffix: Optional[str] = FieldInfo(alias="pageFooterSuffix", default=None)
    """The page footer suffix."""

    page_header_prefix: Optional[str] = FieldInfo(alias="pageHeaderPrefix", default=None)
    """The page header prefix."""

    page_header_suffix: Optional[str] = FieldInfo(alias="pageHeaderSuffix", default=None)
    """The page header suffix."""

    page_prefix: Optional[str] = FieldInfo(alias="pagePrefix", default=None)
    """A page prefix to add before each page."""

    page_separator: Optional[str] = FieldInfo(alias="pageSeparator", default=None)
    """The page separator."""

    page_suffix: Optional[str] = FieldInfo(alias="pageSuffix", default=None)
    """A page suffix to add after each page."""

    parse_mode: Optional[str] = FieldInfo(alias="parseMode", default=None)
    """The parsing mode."""

    pipeline_id: Optional[str] = FieldInfo(alias="pipelineId", default=None)
    """The pipeline ID."""

    premium_mode: Optional[bool] = FieldInfo(alias="premiumMode", default=None)
    """Whether to use premiumMode pipeline."""

    preserve_layout_alignment_across_pages: Optional[bool] = FieldInfo(
        alias="preserveLayoutAlignmentAcrossPages", default=None
    )
    """Whether to preserve layout alignment across pages."""

    preserve_very_small_text: Optional[bool] = FieldInfo(alias="preserveVerySmallText", default=None)
    """Whether to preserve very small text lines."""

    preset: Optional[str] = None
    """The preset of options to be used."""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """The project ID."""

    remove_hidden_text: Optional[bool] = FieldInfo(alias="removeHiddenText", default=None)
    """
    If true, hidden (nonvisible) text in the document will be removed from the
    output.
    """

    resource_info: Optional[Dict[str, object]] = None
    """The resource info about the file"""

    save_images: Optional[bool] = FieldInfo(alias="saveImages", default=None)
    """Whether to output images contained in the document"""

    skip_diagonal_text: Optional[bool] = FieldInfo(alias="skipDiagonalText", default=None)
    """Whether to skip diagonal text."""

    spread_sheet_extract_sub_tables: Optional[bool] = FieldInfo(alias="spreadSheetExtractSubTables", default=None)
    """Whether to extract subTables from spreadsheet."""

    spread_sheet_force_formula_computation: Optional[bool] = FieldInfo(
        alias="spreadSheetForceFormulaComputation", default=None
    )
    """Whether to force re-computation of spreadsheet cells containing formulas."""

    strict_mode_buggy_font: Optional[bool] = FieldInfo(alias="strictModeBuggyFont", default=None)
    """
    If true, the job will fail when we are not able to extract a glyph from the
    document due to buggy font.
    """

    strict_mode_image_extraction: Optional[bool] = FieldInfo(alias="strictModeImageExtraction", default=None)
    """
    If true, the job will fail when we are not able to extract an image from a
    document.
    """

    strict_mode_image_ocr: Optional[bool] = FieldInfo(alias="strictModeImageOCR", default=None)
    """
    If true, the job will fail when we are not able to OCR an image from a document.
    """

    strict_mode_reconstruction: Optional[bool] = FieldInfo(alias="strictModeReconstruction", default=None)
    """
    If true, the job will fail when we are not able to transform a page to Markdown
    in a document.
    """

    structured_output: Optional[bool] = FieldInfo(alias="structuredOutput", default=None)
    """Whether to use structured output."""

    structured_output_json_schema: Optional[str] = FieldInfo(alias="structuredOutputJSONSchema", default=None)
    """The structured output JSON schema."""

    structured_output_json_schema_name: Optional[str] = FieldInfo(alias="structuredOutputJSONSchemaName", default=None)
    """The structured output JSON schema name."""

    system_prompt: Optional[str] = FieldInfo(alias="systemPrompt", default=None)
    """The system prompt."""

    system_prompt_append: Optional[str] = FieldInfo(alias="systemPromptAppend", default=None)
    """The append to system prompt."""

    take_screenshot: Optional[bool] = FieldInfo(alias="takeScreenshot", default=None)
    """Force to capture an image of each pages"""

    target_pages: Optional[str] = FieldInfo(alias="targetPages", default=None)
    """
    A string containing a list of comma separated containing the page number to
    extract. If not specified all pages are extracted from the document. The first
    page is the page 0.
    """

    template: Optional[str] = None
    """The parsing instruction."""

    type: Optional[Literal["legacy_parse"]] = None

    user_prompt: Optional[str] = FieldInfo(alias="userPrompt", default=None)
    """The user prompt."""

    vendor_api_key: Optional[str] = FieldInfo(alias="vendorAPIKey", default=None)
    """The multimodal vendor API key."""

    webhook_url: Optional[str] = FieldInfo(alias="webhookUrl", default=None)
    """The URL that needs to be called at the end of the parsing job."""


class JobJobRecordParametersLoadFilesJobConfig(BaseModel):
    file_ids: Optional[List[str]] = None
    """The names of the files this execution should run against."""

    type: Optional[Literal["load_files"]] = None


class JobJobRecordParametersLLamaParseTransformConfig(BaseModel):
    file_output: str
    """Whether to delete the files"""

    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the documents."""

    resource_info: Optional[Dict[str, object]] = None
    """The resource info about the file"""

    type: Optional[Literal["llama_parse_transform"]] = None


class JobJobRecordParametersPipelineManagedIngestionJobParams(BaseModel):
    delete_info: Optional[DeleteParams] = None
    """Schema for the parameters of a delete job."""

    should_delete: Optional[bool] = None
    """Whether to delete the data sources from the pipeline"""

    type: Optional[Literal["pipeline_managed_ingestion"]] = None


class JobJobRecordParametersDataSourceUpdateDispatcherConfig(BaseModel):
    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the data source."""

    delete_info: Optional[DeleteParams] = None
    """Schema for the parameters of a delete job."""

    pipeline_file_ids: Optional[List[str]] = None
    """Optional: limit sync to these pipeline file IDs only."""

    should_delete: Optional[bool] = None
    """Whether to delete the data source from the pipeline"""

    type: Optional[Literal["data_source_update_dispatcher"]] = None


class JobJobRecordParametersPipelineFileUpdaterConfig(BaseModel):
    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the documents."""

    data_source_project_file_changed: Optional[bool] = None
    """Whether the data source project file has changed"""

    delete_info: Optional[DeleteParams] = None
    """Schema for the parameters of a delete job."""

    is_new_file: Optional[bool] = None
    """Whether the file is new"""

    resource_info: Optional[Dict[str, object]] = None
    """The resource info about the file"""

    should_delete: Optional[bool] = None
    """Whether to delete the files"""

    should_parse: Optional[bool] = None
    """Whether to parse the files"""

    type: Optional[Literal["pipeline_file_updater"]] = None


class JobJobRecordParametersDocumentIngestionJobParams(BaseModel):
    custom_metadata: Optional[Dict[str, object]] = None
    """The custom metadata to attach to the documents."""

    delete_info: Optional[DeleteParams] = None
    """Schema for the parameters of a delete job."""

    document_ids: Optional[List[str]] = None
    """The IDs for the Documents this execution ran against."""

    is_new_file: Optional[bool] = None
    """Whether the file is new"""

    page_count: Optional[int] = None
    """The number of pages in the file. Only used if used llama-parse"""

    pipeline_file_id: Optional[str] = None
    """The ID for the File this execution ran against."""

    resource_info: Optional[Dict[str, object]] = None
    """The resource info about the file"""

    should_delete: Optional[bool] = None
    """Whether to delete the documents"""

    type: Optional[Literal["document_ingestion"]] = None


JobJobRecordParameters: TypeAlias = Annotated[
    Union[
        JobJobRecordParametersParseJobConfig,
        JobJobRecordParametersLegacyParseJobConfig,
        JobJobRecordParametersLoadFilesJobConfig,
        JobJobRecordParametersLLamaParseTransformConfig,
        JobJobRecordParametersPipelineManagedIngestionJobParams,
        JobJobRecordParametersDataSourceUpdateDispatcherConfig,
        JobJobRecordParametersPipelineFileUpdaterConfig,
        JobJobRecordParametersDocumentIngestionJobParams,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class JobJobRecord(BaseModel):
    created_at: datetime
    """Creation datetime"""

    job_name: Literal[
        "pipeline_managed_ingestion_job",
        "data_source_update_dispatcher_job",
        "pipeline_file_updater_job",
        "document_ingestion_job",
        "metadata_update_job",
        "extract_job",
        "parse_raw_file_job",
        "llama_parse_transform_job",
    ]
    """The name of the job."""

    partitions: Dict[str, str]
    """The partitions for this execution.

    Used for determining where to save job output.
    """

    status: StatusEnum
    """Enum for representing the status of a job"""

    id: Optional[str] = None
    """Unique identifier"""

    attempts: Optional[int] = None
    """The number of times this job has been attempted"""

    correlation_id: Optional[str] = None
    """The correlation ID for this job. Used for tracking the job across services."""

    ended_at: Optional[datetime] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    parameters: Optional[JobJobRecordParameters] = None
    """Additional metadata for the job execution."""

    parent_job_execution_id: Optional[str] = None
    """The ID of the parent job execution."""

    project_id: Optional[str] = None
    """The ID of the project this job belongs to."""

    session_id: Optional[str] = None
    """The upstream request ID that created this job.

    Used for tracking the job across services.
    """

    started_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None
    """Update datetime"""

    user_id: Optional[str] = None
    """The ID of the user that created this job"""

    webhook_configurations: Optional[List[WebhookConfiguration]] = None
    """The outbound webhook configurations"""


class JobUser(BaseModel):
    id: str
    """The user id from who triggered the job"""

    name: str
    """The name of the user"""


class JobUsageMetrics(BaseModel):
    day: str

    feature_usage: Dict[str, object]

    job_id: str

    source: str


class Job(BaseModel):
    job_record: JobJobRecord
    """Schema for a job's metadata."""

    user: JobUser

    usage_metrics: Optional[JobUsageMetrics] = None


class V1GetJobsResponse(BaseModel):
    jobs: List[Job]

    limit: int

    offset: int

    total_count: int
