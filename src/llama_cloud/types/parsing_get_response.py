# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ParsingGetResponse",
    "Job",
    "ImagesContentMetadata",
    "ImagesContentMetadataImage",
    "Items",
    "ItemsPage",
    "ItemsPageStructuredResultPage",
    "ItemsPageStructuredResultPageItem",
    "ItemsPageStructuredResultPageItemTextItem",
    "ItemsPageStructuredResultPageItemHeadingItem",
    "ItemsPageStructuredResultPageItemListItem",
    "ItemsPageStructuredResultPageItemListItemItem",
    "ItemsPageStructuredResultPageItemListItemItemTextItem",
    "ItemsPageStructuredResultPageItemCodeItem",
    "ItemsPageStructuredResultPageItemTableItem",
    "ItemsPageStructuredResultPageItemImageItem",
    "ItemsPageStructuredResultPageItemLinkItem",
    "ItemsPageFailedStructuredPage",
    "Markdown",
    "MarkdownPage",
    "MarkdownPageMarkdownResultPage",
    "MarkdownPageFailedMarkdownPage",
    "ResultContentMetadata",
    "Text",
    "TextPage",
]


class Job(BaseModel):
    """Parse job status and metadata"""

    id: str
    """Unique identifier for the parse job"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """
    Current status of the job (e.g., pending, running, completed, failed, cancelled)
    """

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class ImagesContentMetadataImage(BaseModel):
    """Metadata for a single extracted image."""

    filename: str
    """Image filename (e.g., 'image_0.png')"""

    index: int
    """Index of the image in the extraction order"""

    content_type: Optional[str] = None
    """MIME type of the image"""

    presigned_url: Optional[str] = None
    """Presigned URL to download the image"""

    size_bytes: Optional[int] = None
    """Size of the image file in bytes"""


class ImagesContentMetadata(BaseModel):
    """Metadata for all extracted images."""

    images: List[ImagesContentMetadataImage]
    """List of image metadata with presigned URLs"""

    total_count: int
    """Total number of extracted images"""


class ItemsPageStructuredResultPageItemTextItem(BaseModel):
    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


class ItemsPageStructuredResultPageItemHeadingItem(BaseModel):
    level: int
    """Heading level (1-6)"""

    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Heading text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["heading"]] = None
    """Heading item type"""


class ItemsPageStructuredResultPageItemListItemItemTextItem(BaseModel):
    md: str
    """Markdown representation preserving formatting"""

    value: str
    """Text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


ItemsPageStructuredResultPageItemListItemItem: TypeAlias = Union[
    ItemsPageStructuredResultPageItemListItemItemTextItem, object
]


class ItemsPageStructuredResultPageItemListItem(BaseModel):
    items: List[ItemsPageStructuredResultPageItemListItemItem]
    """List of nested text or list items"""

    ordered: bool
    """Whether the list is ordered or unordered"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["list"]] = None
    """List item type"""


class ItemsPageStructuredResultPageItemCodeItem(BaseModel):
    md: str
    """Markdown representation with code fences"""

    value: str
    """Code content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    language: Optional[str] = None
    """Programming language identifier"""

    type: Optional[Literal["code"]] = None
    """Code block item type"""


class ItemsPageStructuredResultPageItemTableItem(BaseModel):
    csv: str
    """CSV representation of the table"""

    html: str
    """HTML representation of the table"""

    md: str
    """Markdown representation of the table"""

    rows: List[List[str]]
    """Table data as array of string arrays"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["table"]] = None
    """Table item type"""


class ItemsPageStructuredResultPageItemImageItem(BaseModel):
    name: str
    """Image filename or identifier"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["image"]] = None
    """Image item type"""


class ItemsPageStructuredResultPageItemLinkItem(BaseModel):
    text: str
    """Display text of the link"""

    url: str
    """URL of the link"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["link"]] = None
    """Link item type"""


ItemsPageStructuredResultPageItem: TypeAlias = Annotated[
    Union[
        ItemsPageStructuredResultPageItemTextItem,
        ItemsPageStructuredResultPageItemHeadingItem,
        ItemsPageStructuredResultPageItemListItem,
        ItemsPageStructuredResultPageItemCodeItem,
        ItemsPageStructuredResultPageItemTableItem,
        ItemsPageStructuredResultPageItemImageItem,
        ItemsPageStructuredResultPageItemLinkItem,
    ],
    PropertyInfo(discriminator="type"),
]


class ItemsPageStructuredResultPage(BaseModel):
    items: List[ItemsPageStructuredResultPageItem]
    """List of structured items on the page"""

    page_number: int
    """Page number of the document"""

    success: Optional[Literal[True]] = None
    """Success indicator"""


class ItemsPageFailedStructuredPage(BaseModel):
    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Optional[bool] = None
    """Failure indicator"""


ItemsPage: TypeAlias = Union[ItemsPageStructuredResultPage, ItemsPageFailedStructuredPage]


class Items(BaseModel):
    """Structured JSON result (if requested)"""

    pages: List[ItemsPage]
    """List of structured pages or failed page entries"""


class MarkdownPageMarkdownResultPage(BaseModel):
    markdown: str
    """Markdown content of the page"""

    page_number: int
    """Page number of the document"""

    success: Optional[Literal[True]] = None
    """Success indicator"""


class MarkdownPageFailedMarkdownPage(BaseModel):
    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Optional[bool] = None
    """Failure indicator"""


MarkdownPage: TypeAlias = Union[MarkdownPageMarkdownResultPage, MarkdownPageFailedMarkdownPage]


class Markdown(BaseModel):
    """Markdown result (if requested)"""

    pages: List[MarkdownPage]
    """List of markdown pages or failed page entries"""


class ResultContentMetadata(BaseModel):
    """Metadata about a specific result type stored in S3."""

    size_bytes: int
    """Size of the result file in S3 (bytes)"""

    exists: Optional[bool] = None
    """Whether the result file exists in S3"""

    presigned_url: Optional[str] = None
    """Presigned URL to download the result file"""


class TextPage(BaseModel):
    page_number: int
    """Page number of the document"""

    text: str
    """Plain text content of the page"""


class Text(BaseModel):
    """Plain text result (if requested)"""

    pages: List[TextPage]
    """List of text pages"""


class ParsingGetResponse(BaseModel):
    """Parse result response with job status and optional content or metadata.

    The job field is always included. Other fields are included based on expand parameters.
    """

    job: Job
    """Parse job status and metadata"""

    images_content_metadata: Optional[ImagesContentMetadata] = None
    """Metadata for all extracted images."""

    items: Optional[Items] = None
    """Structured JSON result (if requested)"""

    markdown: Optional[Markdown] = None
    """Markdown result (if requested)"""

    result_content_metadata: Optional[Dict[str, ResultContentMetadata]] = None
    """Metadata including size, existence, and presigned URLs for result files"""

    text: Optional[Text] = None
    """Plain text result (if requested)"""
