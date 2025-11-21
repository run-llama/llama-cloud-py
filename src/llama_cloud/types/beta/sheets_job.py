# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..file import File
from ..._models import BaseModel
from ..status_enum import StatusEnum
from .sheets_parsing_config import SheetsParsingConfig

__all__ = ["SheetsJob", "Region", "WorksheetMetadata"]


class Region(BaseModel):
    location: str
    """Location of the region in the spreadsheet"""

    region_type: str
    """Type of the extracted region"""

    sheet_name: str
    """Worksheet name where region was found"""

    description: Optional[str] = None
    """Generated description for the region"""

    region_id: Optional[str] = None
    """Unique identifier for this region within the file"""

    title: Optional[str] = None
    """Generated title for the region"""


class WorksheetMetadata(BaseModel):
    sheet_name: str
    """Name of the worksheet"""

    description: Optional[str] = None
    """Generated description of the worksheet"""

    title: Optional[str] = None
    """Generated title for the worksheet"""


class SheetsJob(BaseModel):
    id: str
    """The ID of the job"""

    config: SheetsParsingConfig
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

    regions: Optional[List[Region]] = None
    """All extracted regions (populated when job is complete)"""

    success: Optional[bool] = None
    """Whether the job completed successfully"""

    worksheet_metadata: Optional[List[WorksheetMetadata]] = None
    """Metadata for each processed worksheet (populated when job is complete)"""
