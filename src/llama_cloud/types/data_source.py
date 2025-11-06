# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .cloud_s3_data_source import CloudS3DataSource
from .cloud_box_data_source import CloudBoxDataSource
from .cloud_jira_data_source import CloudJiraDataSource
from .cloud_slack_data_source import CloudSlackDataSource
from .cloud_jira_data_source_v2 import CloudJiraDataSourceV2
from .cloud_one_drive_data_source import CloudOneDriveDataSource
from .cloud_confluence_data_source import CloudConfluenceDataSource
from .cloud_sharepoint_data_source import CloudSharepointDataSource
from .cloud_notion_page_data_source import CloudNotionPageDataSource
from .configurable_data_source_names import ConfigurableDataSourceNames
from .cloud_az_storage_blob_data_source import CloudAzStorageBlobDataSource
from .data_source_reader_version_metadata import DataSourceReaderVersionMetadata

__all__ = ["DataSource", "Component"]

Component: TypeAlias = Union[
    Dict[str, object],
    CloudS3DataSource,
    CloudAzStorageBlobDataSource,
    CloudOneDriveDataSource,
    CloudSharepointDataSource,
    CloudSlackDataSource,
    CloudNotionPageDataSource,
    CloudConfluenceDataSource,
    CloudJiraDataSource,
    CloudJiraDataSourceV2,
    CloudBoxDataSource,
]


class DataSource(BaseModel):
    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data source"""

    name: str
    """The name of the data source."""

    project_id: str

    source_type: ConfigurableDataSourceNames

    created_at: Optional[datetime] = None
    """Creation datetime"""

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Custom metadata that will be present on all data loaded from the data source"""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    version_metadata: Optional[DataSourceReaderVersionMetadata] = None
    """Version metadata for the data source"""
