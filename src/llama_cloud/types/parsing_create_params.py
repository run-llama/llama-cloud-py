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
    "OutputOptionsEmbeddedImages",
    "OutputOptionsExportPdf",
    "OutputOptionsMarkdown",
    "OutputOptionsMarkdownPages",
    "OutputOptionsMarkdownTables",
    "OutputOptionsScreenshots",
    "OutputOptionsSpatialText",
    "OutputOptionsSpatialTextPages",
    "OutputOptionsTablesAsSpreadsheet",
    "PageRanges",
    "ProcessingControl",
    "ProcessingControlJobFailureConditions",
    "ProcessingControlTimeouts",
    "ProcessingOptions",
    "ProcessingOptionsIgnore",
    "ProcessingOptionsOcrParameters",
    "WebhookConfiguration",
]


class ParsingCreateParams(TypedDict, total=False):
    tier: Required[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]
    """The parsing tier to use"""

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

    version: Union[Literal["2025-12-18", "2025-12-11", "latest"], str]
    """Version of the tier configuration"""

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


class OutputOptionsEmbeddedImages(TypedDict, total=False):
    """Embedded image extraction options"""

    enable: Optional[bool]
    """Whether this option is enabled"""


class OutputOptionsExportPdf(TypedDict, total=False):
    """PDF export options"""

    enable: Optional[bool]
    """Whether this option is enabled"""


class OutputOptionsMarkdownPages(TypedDict, total=False):
    """Page formatting options for markdown"""

    merge_tables_across_pages_in_markdown: Optional[bool]
    """Merge tables that span across pages in markdown output"""


class OutputOptionsMarkdownTables(TypedDict, total=False):
    """Table formatting options for markdown"""

    compact_markdown_tables: Optional[bool]
    """Use compact formatting for markdown tables"""

    markdown_table_multiline_separator: Optional[str]
    """Separator for multiline content in markdown tables"""

    output_tables_as_markdown: Optional[bool]
    """Output tables in markdown format"""


class OutputOptionsMarkdown(TypedDict, total=False):
    """Markdown output formatting options"""

    annotate_links: Optional[bool]
    """Add annotations to links in markdown output"""

    pages: OutputOptionsMarkdownPages
    """Page formatting options for markdown"""

    tables: OutputOptionsMarkdownTables
    """Table formatting options for markdown"""


class OutputOptionsScreenshots(TypedDict, total=False):
    """Screenshot generation options"""

    enable: Optional[bool]
    """Whether this option is enabled"""


class OutputOptionsSpatialTextPages(TypedDict, total=False):
    """Page formatting options for spatial text"""

    merge_tables_across_pages_in_markdown: Optional[bool]
    """Merge tables that span across pages in markdown output"""


class OutputOptionsSpatialText(TypedDict, total=False):
    """Spatial text output options"""

    do_not_unroll_columns: Optional[bool]
    """Keep column structure intact without unrolling"""

    pages: Optional[OutputOptionsSpatialTextPages]
    """Page formatting options for spatial text"""

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

    embedded_images: OutputOptionsEmbeddedImages
    """Embedded image extraction options"""

    export_pdf: OutputOptionsExportPdf
    """PDF export options"""

    extract_printed_page_number: Optional[bool]
    """Extract printed page numbers from the document"""

    markdown: OutputOptionsMarkdown
    """Markdown output formatting options"""

    screenshots: OutputOptionsScreenshots
    """Screenshot generation options"""

    spatial_text: OutputOptionsSpatialText
    """Spatial text output options"""

    tables_as_spreadsheet: OutputOptionsTablesAsSpreadsheet
    """Table export as spreadsheet options"""


class PageRanges(TypedDict, total=False):
    """Page range selection options"""

    max_pages: Optional[int]
    """Maximum number of pages to process"""

    target_pages: Optional[str]
    """Specific pages to process (e.g., '1,3,5-10')"""


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

    ignore: ProcessingOptionsIgnore
    """Options for ignoring specific text types"""

    ocr_parameters: ProcessingOptionsOcrParameters
    """OCR configuration parameters"""


class WebhookConfiguration(TypedDict, total=False):
    webhook_events: Optional[SequenceNotStr[str]]
    """List of events that trigger webhook notifications"""

    webhook_headers: Optional[Dict[str, object]]
    """Custom headers to include in webhook requests"""

    webhook_url: Optional[str]
    """Webhook URL for receiving parsing notifications"""
