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
    "ItemsPageFailedStructuredPage",
    "Markdown",
    "MarkdownPage",
    "MarkdownPageMarkdownResultPage",
    "MarkdownPageFailedMarkdownPage",
    "Text",
    "TextPage",
]


class Job(BaseModel):
    """Parse job status and metadata (always included)"""

    id: str
    """Unique identifier for the parse job"""

    parameters: Dict[str, object]
    """Job-specific parameters as JSON"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["pending", "running", "completed", "failed", "cancelled"]
    """
    Current status of the job (e.g., pending, running, completed, failed, cancelled)
    """

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    updated_at: Optional[datetime] = None
    """Update datetime"""


class ItemsPageStructuredResultPageItemTextItem(BaseModel):
    value: str
    """Text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


class ItemsPageStructuredResultPageItemHeadingItem(BaseModel):
    level: int
    """Heading level (1-6)"""

    value: str
    """Heading text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["heading"]] = None
    """Heading item type"""


class ItemsPageStructuredResultPageItemListItemItemTextItem(BaseModel):
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


ItemsPageStructuredResultPageItem: TypeAlias = Annotated[
    Union[
        ItemsPageStructuredResultPageItemTextItem,
        ItemsPageStructuredResultPageItemHeadingItem,
        ItemsPageStructuredResultPageItemListItem,
        ItemsPageStructuredResultPageItemCodeItem,
        ItemsPageStructuredResultPageItemTableItem,
        ItemsPageStructuredResultPageItemImageItem,
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
    """Combined parse result response with job status and optional result data.

    The job field is always present with status information. Other fields are only included
    if requested via the corresponding flags in ParseResultRequest.
    """

    job: Job
    """Parse job status and metadata (always included)"""

    items: Optional[Items] = None
    """Structured JSON result (if requested)"""

    markdown: Optional[Markdown] = None
    """Markdown result (if requested)"""

    text: Optional[Text] = None
    """Plain text result (if requested)"""
