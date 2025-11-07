# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...file import File
from ...._models import BaseModel
from ...status_enum import StatusEnum
from .spreadsheet_parsing_config import SpreadsheetParsingConfig

__all__ = ["SpreadsheetJob", "Table", "WorksheetMetadata"]


class Table(BaseModel):
    sheet_name: str
    """Worksheet name where table was found"""

    table_location: str
    """Location of the table in the spreadsheet"""

    metadata_json: Optional[str] = None
    """JSON metadata with detailed table information"""

    table_id: Optional[str] = None
    """Unique identifier for this table within the file"""


class WorksheetMetadata(BaseModel):
    sheet_name: str
    """Name of the worksheet"""

    description: Optional[str] = None
    """Generated description of the worksheet"""

    title: Optional[str] = None
    """Generated title for the worksheet"""


class SpreadsheetJob(BaseModel):
    id: str
    """The ID of the job"""

    config: SpreadsheetParsingConfig
    """Configuration for the parsing job"""

    created_at: str
    """When the job was created"""

    file: File
    """The file to process"""

    project_id: str
    """The ID of the project"""

    status: StatusEnum
    """The status of the parsing job"""

    updated_at: str
    """When the job was last updated"""

    user_id: str
    """The ID of the user"""

    errors: Optional[List[str]] = None
    """Any errors encountered"""

    success: Optional[bool] = None
    """Whether the job completed successfully"""

    tables: Optional[List[Table]] = None
    """All extracted tables (populated when job is complete)"""

    worksheet_metadata: Optional[List[WorksheetMetadata]] = None
    """Metadata for each processed worksheet (populated when job is complete)"""
