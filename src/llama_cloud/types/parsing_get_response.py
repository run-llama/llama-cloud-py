# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ParsingGetResponse",
    "Metadata",
    "Markdown",
    "MarkdownPage",
    "MarkdownPageMarkdownResultPage",
    "MarkdownPageFailedMarkdownPage",
    "Structured",
    "StructuredPage",
    "StructuredPageStructuredResultPage",
    "StructuredPageStructuredResultPageItem",
    "StructuredPageStructuredResultPageItemTextItem",
    "StructuredPageStructuredResultPageItemHeadingItem",
    "StructuredPageStructuredResultPageItemListItem",
    "StructuredPageStructuredResultPageItemListItemItem",
    "StructuredPageStructuredResultPageItemListItemItemTextItem",
    "StructuredPageStructuredResultPageItemCodeItem",
    "StructuredPageStructuredResultPageItemTableItem",
    "StructuredPageStructuredResultPageItemImageItem",
    "StructuredPageFailedStructuredPage",
    "Text",
    "TextPage",
]


class Metadata(BaseModel):
    """Job metadata (always included)"""

    job_id: str
    """Parse job ID"""

    status: str
    """Job status"""

    credits_used: Optional[int] = None
    """Credits consumed by this job"""

    error_message: Optional[str] = None
    """Error message if job failed"""

    pages: Optional[int] = None
    """Number of pages processed"""


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


class StructuredPageStructuredResultPageItemTextItem(BaseModel):
    value: str
    """Text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


class StructuredPageStructuredResultPageItemHeadingItem(BaseModel):
    level: int
    """Heading level (1-6)"""

    value: str
    """Heading text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["heading"]] = None
    """Heading item type"""


class StructuredPageStructuredResultPageItemListItemItemTextItem(BaseModel):
    value: str
    """Text content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["text"]] = None
    """Text item type"""


StructuredPageStructuredResultPageItemListItemItem: TypeAlias = Union[
    StructuredPageStructuredResultPageItemListItemItemTextItem, object
]


class StructuredPageStructuredResultPageItemListItem(BaseModel):
    items: List[StructuredPageStructuredResultPageItemListItemItem]
    """List of nested text or list items"""

    ordered: bool
    """Whether the list is ordered or unordered"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["list"]] = None
    """List item type"""


class StructuredPageStructuredResultPageItemCodeItem(BaseModel):
    value: str
    """Code content"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    language: Optional[str] = None
    """Programming language identifier"""

    type: Optional[Literal["code"]] = None
    """Code block item type"""


class StructuredPageStructuredResultPageItemTableItem(BaseModel):
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


class StructuredPageStructuredResultPageItemImageItem(BaseModel):
    name: str
    """Image filename or identifier"""

    b_box: Optional[List[object]] = FieldInfo(alias="bBox", default=None)
    """Bounding box coordinates [x1, y1, x2, y2]"""

    type: Optional[Literal["image"]] = None
    """Image item type"""


StructuredPageStructuredResultPageItem: TypeAlias = Annotated[
    Union[
        StructuredPageStructuredResultPageItemTextItem,
        StructuredPageStructuredResultPageItemHeadingItem,
        StructuredPageStructuredResultPageItemListItem,
        StructuredPageStructuredResultPageItemCodeItem,
        StructuredPageStructuredResultPageItemTableItem,
        StructuredPageStructuredResultPageItemImageItem,
    ],
    PropertyInfo(discriminator="type"),
]


class StructuredPageStructuredResultPage(BaseModel):
    items: List[StructuredPageStructuredResultPageItem]
    """List of structured items on the page"""

    page_number: int
    """Page number of the document"""

    success: Optional[Literal[True]] = None
    """Success indicator"""


class StructuredPageFailedStructuredPage(BaseModel):
    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Optional[bool] = None
    """Failure indicator"""


StructuredPage: TypeAlias = Union[StructuredPageStructuredResultPage, StructuredPageFailedStructuredPage]


class Structured(BaseModel):
    """Structured JSON result (if requested)"""

    pages: List[StructuredPage]
    """List of structured pages or failed page entries"""


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
    """Combined parse result response with metadata and optional result data.

    The metadata field is always present. Other fields are only included if requested
    via the corresponding flags in ParseResultRequest.
    """

    metadata: Metadata
    """Job metadata (always included)"""

    json_output: Optional[Dict[str, object]] = None
    """JSON output result (if requested)"""

    markdown: Optional[Markdown] = None
    """Markdown result (if requested)"""

    structured: Optional[Structured] = None
    """Structured JSON result (if requested)"""

    text: Optional[Text] = None
    """Plain text result (if requested)"""
