# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .parsing_languages import ParsingLanguages

__all__ = [
    "ParsingCreateParams",
    "AgenticOptions",
    "CropBox",
    "InputOptions",
    "InputOptionsHTML",
    "InputOptionsPresentation",
    "InputOptionsSpreadsheet",
    "OutputOptions",
    "OutputOptionsMarkdown",
    "OutputOptionsMarkdownTables",
    "OutputOptionsSpatialText",
    "OutputOptionsTablesAsSpreadsheet",
    "PageRanges",
    "ProcessingControl",
    "ProcessingControlJobFailureConditions",
    "ProcessingControlTimeouts",
    "ProcessingOptions",
    "ProcessingOptionsAutoModeConfiguration",
    "ProcessingOptionsAutoModeConfigurationParsingConf",
    "ProcessingOptionsAutoModeConfigurationParsingConfCropBox",
    "ProcessingOptionsAutoModeConfigurationParsingConfIgnore",
    "ProcessingOptionsAutoModeConfigurationParsingConfPresentation",
    "ProcessingOptionsAutoModeConfigurationParsingConfSpatialText",
    "ProcessingOptionsCostOptimizer",
    "ProcessingOptionsIgnore",
    "ProcessingOptionsOcrParameters",
    "WebhookConfiguration",
]


class ParsingCreateParams(TypedDict, total=False):
    tier: Required[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]
    """The parsing tier to use"""

    version: Required[
        Union[
            Literal[
                "2026-01-08",
                "2025-12-31",
                "2025-12-18",
                "2025-12-11",
                "2026-01-16",
                "2026-01-21",
                "2026-01-22",
                "2026-01-24",
                "2026-01-29",
                "latest",
            ],
            str,
        ]
    ]
    """Version of the tier configuration"""

    organization_id: Optional[str]

    project_id: Optional[str]

    agentic_options: Optional[AgenticOptions]
    """Options for agentic tier parsing (with AI agents)."""

    client_name: Optional[str]
    """Name of the client making the parsing request"""

    crop_box: CropBox
    """Document crop box boundaries"""

    disable_cache: Optional[bool]
    """Whether to disable caching for this parsing job"""

    fast_options: Optional[object]
    """Options for fast tier parsing (without AI)."""

    file_id: Optional[str]
    """ID of an existing file in the project to parse"""

    http_proxy: Optional[str]
    """HTTP proxy URL for network requests (only used with source_url)"""

    input_options: InputOptions
    """Input format-specific parsing options"""

    output_options: OutputOptions
    """Output format and styling options"""

    page_ranges: PageRanges
    """Page range selection options"""

    processing_control: ProcessingControl
    """Job processing control and failure handling"""

    processing_options: ProcessingOptions
    """Processing options shared across all tiers"""

    source_url: Optional[str]
    """Source URL to fetch document from"""

    webhook_configurations: Iterable[WebhookConfiguration]
    """List of webhook configurations for notifications"""


class AgenticOptions(TypedDict, total=False):
    """Options for agentic tier parsing (with AI agents)."""

    custom_prompt: Optional[str]
    """Custom prompt for AI-powered parsing"""


class CropBox(TypedDict, total=False):
    """Document crop box boundaries"""

    bottom: Optional[float]
    """Bottom boundary of crop box as ratio (0-1)"""

    left: Optional[float]
    """Left boundary of crop box as ratio (0-1)"""

    right: Optional[float]
    """Right boundary of crop box as ratio (0-1)"""

    top: Optional[float]
    """Top boundary of crop box as ratio (0-1)"""


class InputOptionsHTML(TypedDict, total=False):
    """HTML-specific parsing options"""

    make_all_elements_visible: Optional[bool]
    """Make all HTML elements visible during parsing"""

    remove_fixed_elements: Optional[bool]
    """Remove fixed position elements from HTML"""

    remove_navigation_elements: Optional[bool]
    """Remove navigation elements from HTML"""


class InputOptionsPresentation(TypedDict, total=False):
    """Presentation-specific parsing options"""

    out_of_bounds_content: Optional[bool]
    """Extract out of bounds content in presentation slides"""

    skip_embedded_data: Optional[bool]
    """Skip extraction of embedded data for charts in presentation slides"""


class InputOptionsSpreadsheet(TypedDict, total=False):
    """Spreadsheet-specific parsing options"""

    detect_sub_tables_in_sheets: Optional[bool]
    """Detect and extract sub-tables within spreadsheet cells"""

    force_formula_computation_in_sheets: Optional[bool]
    """Force re-computation of spreadsheet cells containing formulas"""


class InputOptions(TypedDict, total=False):
    """Input format-specific parsing options"""

    html: InputOptionsHTML
    """HTML-specific parsing options"""

    pdf: object
    """PDF-specific parsing options"""

    presentation: InputOptionsPresentation
    """Presentation-specific parsing options"""

    spreadsheet: InputOptionsSpreadsheet
    """Spreadsheet-specific parsing options"""


class OutputOptionsMarkdownTables(TypedDict, total=False):
    """Table formatting options for markdown"""

    compact_markdown_tables: Optional[bool]
    """Use compact formatting for markdown tables"""

    markdown_table_multiline_separator: Optional[str]
    """Separator for multiline content in markdown tables"""

    merge_continued_tables: Optional[bool]
    """Merge tables that continue across or within pages. Affects markdown and items"""

    output_tables_as_markdown: Optional[bool]
    """Output tables in markdown format"""


class OutputOptionsMarkdown(TypedDict, total=False):
    """Markdown output formatting options"""

    annotate_links: Optional[bool]
    """Add annotations to links in markdown output"""

    inline_images: Optional[bool]
    """Instead of transcribing images, inline them in the markdown output"""

    tables: OutputOptionsMarkdownTables
    """Table formatting options for markdown"""


class OutputOptionsSpatialText(TypedDict, total=False):
    """Spatial text output options"""

    do_not_unroll_columns: Optional[bool]
    """Keep column structure intact without unrolling"""

    preserve_layout_alignment_across_pages: Optional[bool]
    """Preserve text alignment across page boundaries"""

    preserve_very_small_text: Optional[bool]
    """Include very small text in spatial output"""


class OutputOptionsTablesAsSpreadsheet(TypedDict, total=False):
    """Table export as spreadsheet options"""

    enable: Optional[bool]
    """Whether this option is enabled"""

    guess_sheet_name: bool
    """Automatically guess sheet names when exporting tables"""


class OutputOptions(TypedDict, total=False):
    """Output format and styling options"""

    extract_printed_page_number: Optional[bool]
    """Extract printed page numbers from the document"""

    images_to_save: List[Literal["screenshot", "embedded", "layout"]]
    """
    Image categories to save: 'screenshot' (full page), 'embedded' (images in
    document), 'layout' (cropped images from layout detection). Empty list means no
    images are saved.
    """

    markdown: OutputOptionsMarkdown
    """Markdown output formatting options"""

    spatial_text: OutputOptionsSpatialText
    """Spatial text output options"""

    tables_as_spreadsheet: OutputOptionsTablesAsSpreadsheet
    """Table export as spreadsheet options"""


class PageRanges(TypedDict, total=False):
    """Page range selection options"""

    max_pages: Optional[int]
    """Maximum number of pages to process"""

    target_pages: Optional[str]
    """Specific pages to process (e.g., '1,3,5-8') using 1-based indexing"""


class ProcessingControlJobFailureConditions(TypedDict, total=False):
    """Conditions that determine job failure"""

    allowed_page_failure_ratio: Optional[float]
    """Maximum ratio of pages allowed to fail (0-1)"""

    fail_on_buggy_font: Optional[bool]
    """Fail job if buggy fonts are detected"""

    fail_on_image_extraction_error: Optional[bool]
    """Fail job if image extraction encounters errors"""

    fail_on_image_ocr_error: Optional[bool]
    """Fail job if image OCR encounters errors"""

    fail_on_markdown_reconstruction_error: Optional[bool]
    """Fail job if markdown reconstruction encounters errors"""


class ProcessingControlTimeouts(TypedDict, total=False):
    """Timeout configuration for parsing jobs"""

    base_in_seconds: Optional[int]
    """Base timeout in seconds (max 30 minutes)"""

    extra_time_per_page_in_seconds: Optional[int]
    """Additional timeout per page in seconds (max 5 minutes)"""


class ProcessingControl(TypedDict, total=False):
    """Job processing control and failure handling"""

    job_failure_conditions: ProcessingControlJobFailureConditions
    """Conditions that determine job failure"""

    timeouts: ProcessingControlTimeouts
    """Timeout configuration for parsing jobs"""


class ProcessingOptionsAutoModeConfigurationParsingConfCropBox(TypedDict, total=False):
    """Crop box options for auto mode parsing configuration."""

    bottom: Optional[float]
    """Bottom boundary of crop box as ratio (0-1)"""

    left: Optional[float]
    """Left boundary of crop box as ratio (0-1)"""

    right: Optional[float]
    """Right boundary of crop box as ratio (0-1)"""

    top: Optional[float]
    """Top boundary of crop box as ratio (0-1)"""


class ProcessingOptionsAutoModeConfigurationParsingConfIgnore(TypedDict, total=False):
    """Ignore options for auto mode parsing configuration."""

    ignore_diagonal_text: Optional[bool]
    """Whether to ignore diagonal text in the document"""

    ignore_hidden_text: Optional[bool]
    """Whether to ignore hidden text in the document"""


class ProcessingOptionsAutoModeConfigurationParsingConfPresentation(TypedDict, total=False):
    """Presentation-specific options for auto mode parsing configuration."""

    out_of_bounds_content: Optional[bool]
    """Extract out of bounds content in presentation slides"""

    skip_embedded_data: Optional[bool]
    """Skip extraction of embedded data for charts in presentation slides"""


class ProcessingOptionsAutoModeConfigurationParsingConfSpatialText(TypedDict, total=False):
    """Spatial text options for auto mode parsing configuration."""

    do_not_unroll_columns: Optional[bool]
    """Keep column structure intact without unrolling"""

    preserve_layout_alignment_across_pages: Optional[bool]
    """Preserve text alignment across page boundaries"""

    preserve_very_small_text: Optional[bool]
    """Include very small text in spatial output"""


class ProcessingOptionsAutoModeConfigurationParsingConf(TypedDict, total=False):
    """Configuration for parsing in auto mode (V2 format).

    This uses V2 API naming conventions. The backend service will convert
    these to the V1 format expected by the llamaparse worker.
    """

    adaptive_long_table: Optional[bool]
    """Whether to use adaptive long table handling"""

    aggressive_table_extraction: Optional[bool]
    """Whether to use aggressive table extraction"""

    crop_box: Optional[ProcessingOptionsAutoModeConfigurationParsingConfCropBox]
    """Crop box options for auto mode parsing configuration."""

    custom_prompt: Optional[str]
    """Custom prompt for AI-powered parsing"""

    extract_layout: Optional[bool]
    """Whether to extract layout information"""

    high_res_ocr: Optional[bool]
    """Whether to use high resolution OCR"""

    ignore: Optional[ProcessingOptionsAutoModeConfigurationParsingConfIgnore]
    """Ignore options for auto mode parsing configuration."""

    language: Optional[str]
    """Primary language of the document"""

    outlined_table_extraction: Optional[bool]
    """Whether to use outlined table extraction"""

    presentation: Optional[ProcessingOptionsAutoModeConfigurationParsingConfPresentation]
    """Presentation-specific options for auto mode parsing configuration."""

    spatial_text: Optional[ProcessingOptionsAutoModeConfigurationParsingConfSpatialText]
    """Spatial text options for auto mode parsing configuration."""

    specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]
    """Enable specialized chart parsing with the specified mode"""

    tier: Optional[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]
    """The parsing tier to use"""

    version: Union[
        Literal[
            "2026-01-08",
            "2025-12-31",
            "2025-12-18",
            "2025-12-11",
            "2026-01-16",
            "2026-01-21",
            "2026-01-22",
            "2026-01-24",
            "2026-01-29",
            "latest",
        ],
        str,
        None,
    ]
    """Version of the tier configuration"""


class ProcessingOptionsAutoModeConfiguration(TypedDict, total=False):
    """A single entry in the auto mode configuration array."""

    parsing_conf: Required[ProcessingOptionsAutoModeConfigurationParsingConf]
    """Configuration for parsing in auto mode (V2 format).

    This uses V2 API naming conventions. The backend service will convert these to
    the V1 format expected by the llamaparse worker.
    """

    filename_match_glob: Optional[str]
    """Single glob pattern to match against filename"""

    filename_match_glob_list: Optional[SequenceNotStr[str]]
    """List of glob patterns to match against filename"""

    filename_regexp: Optional[str]
    """Regex pattern to match against filename"""

    filename_regexp_mode: Optional[str]
    """Regex mode flags (e.g., 'i' for case-insensitive)"""

    full_page_image_in_page: Optional[bool]
    """Trigger if page contains a full-page image (scanned page detection)"""

    full_page_image_in_page_threshold: Union[float, str, None]
    """Threshold for full page image detection (0.0-1.0, default 0.8)"""

    image_in_page: Optional[bool]
    """Trigger if page contains non-screenshot images"""

    layout_element_in_page: Optional[str]
    """Trigger if page contains this layout element type"""

    layout_element_in_page_confidence_threshold: Union[float, str, None]
    """Confidence threshold for layout element detection"""

    page_contains_at_least_n_charts: Union[int, str, None]
    """Trigger if page has more than N charts"""

    page_contains_at_least_n_images: Union[int, str, None]
    """Trigger if page has more than N images"""

    page_contains_at_least_n_layout_elements: Union[int, str, None]
    """Trigger if page has more than N layout elements"""

    page_contains_at_least_n_lines: Union[int, str, None]
    """Trigger if page has more than N lines"""

    page_contains_at_least_n_links: Union[int, str, None]
    """Trigger if page has more than N links"""

    page_contains_at_least_n_numbers: Union[int, str, None]
    """Trigger if page has more than N numeric words"""

    page_contains_at_least_n_percent_numbers: Union[int, str, None]
    """Trigger if page has more than N% numeric words"""

    page_contains_at_least_n_tables: Union[int, str, None]
    """Trigger if page has more than N tables"""

    page_contains_at_least_n_words: Union[int, str, None]
    """Trigger if page has more than N words"""

    page_contains_at_most_n_charts: Union[int, str, None]
    """Trigger if page has fewer than N charts"""

    page_contains_at_most_n_images: Union[int, str, None]
    """Trigger if page has fewer than N images"""

    page_contains_at_most_n_layout_elements: Union[int, str, None]
    """Trigger if page has fewer than N layout elements"""

    page_contains_at_most_n_lines: Union[int, str, None]
    """Trigger if page has fewer than N lines"""

    page_contains_at_most_n_links: Union[int, str, None]
    """Trigger if page has fewer than N links"""

    page_contains_at_most_n_numbers: Union[int, str, None]
    """Trigger if page has fewer than N numeric words"""

    page_contains_at_most_n_percent_numbers: Union[int, str, None]
    """Trigger if page has fewer than N% numeric words"""

    page_contains_at_most_n_tables: Union[int, str, None]
    """Trigger if page has fewer than N tables"""

    page_contains_at_most_n_words: Union[int, str, None]
    """Trigger if page has fewer than N words"""

    page_longer_than_n_chars: Union[int, str, None]
    """Trigger if page has more than N characters"""

    page_md_error: Optional[bool]
    """Trigger on pages with markdown extraction errors"""

    page_shorter_than_n_chars: Union[int, str, None]
    """Trigger if page has fewer than N characters"""

    regexp_in_page: Optional[str]
    """Regex pattern to match in page content"""

    regexp_in_page_mode: Optional[str]
    """Regex mode flags for regexp_in_page"""

    table_in_page: Optional[bool]
    """Trigger if page contains a table"""

    text_in_page: Optional[str]
    """Trigger if page text/markdown contains this string"""

    trigger_mode: Optional[str]
    """
    How to combine multiple trigger conditions: 'and' (all must match, default) or
    'or' (any can match)
    """


class ProcessingOptionsCostOptimizer(TypedDict, total=False):
    """Cost optimizer parameters for parsing configuration."""

    enable: Optional[bool]
    """Use cost-optimized parsing for the document.

    May negatively impact parsing speed and quality.
    """


class ProcessingOptionsIgnore(TypedDict, total=False):
    """Options for ignoring specific text types"""

    ignore_diagonal_text: Optional[bool]
    """Whether to ignore diagonal text in the document"""

    ignore_hidden_text: Optional[bool]
    """Whether to ignore hidden text in the document"""

    ignore_text_in_image: Optional[bool]
    """Whether to ignore text that appears within images"""


class ProcessingOptionsOcrParameters(TypedDict, total=False):
    """OCR configuration parameters"""

    languages: Optional[List[ParsingLanguages]]
    """List of languages to use for OCR processing"""


class ProcessingOptions(TypedDict, total=False):
    """Processing options shared across all tiers"""

    aggressive_table_extraction: Optional[bool]
    """Whether to use aggressive table extraction"""

    auto_mode_configuration: Optional[Iterable[ProcessingOptionsAutoModeConfiguration]]
    """Configuration for auto mode parsing with triggers and parsing options"""

    cost_optimizer: Optional[ProcessingOptionsCostOptimizer]
    """Cost optimizer parameters for parsing configuration."""

    disable_heuristics: Optional[bool]
    """
    Whether to disable heuristics like outlined table extraction and adaptive long
    table handling
    """

    ignore: ProcessingOptionsIgnore
    """Options for ignoring specific text types"""

    ocr_parameters: ProcessingOptionsOcrParameters
    """OCR configuration parameters"""

    specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]
    """Enable specialized chart parsing with the specified mode"""


class WebhookConfiguration(TypedDict, total=False):
    webhook_events: Optional[SequenceNotStr[str]]
    """List of events that trigger webhook notifications"""

    webhook_headers: Optional[Dict[str, object]]
    """Custom headers to include in webhook requests"""

    webhook_url: Optional[str]
    """Webhook URL for receiving parsing notifications"""
