# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..data_source_reader_version_metadata import DataSourceReaderVersionMetadata

__all__ = [
    "PipelineDataSource",
    "Component",
    "ComponentCloudS3DataSource",
    "ComponentCloudAzStorageBlobDataSource",
    "ComponentCloudOneDriveDataSource",
    "ComponentCloudSharepointDataSource",
    "ComponentCloudSlackDataSource",
    "ComponentCloudNotionPageDataSource",
    "ComponentCloudConfluenceDataSource",
    "ComponentCloudConfluenceDataSourceFailureHandling",
    "ComponentCloudJiraDataSource",
    "ComponentCloudJiraDataSourceV2",
    "ComponentCloudBoxDataSource",
]


class ComponentCloudS3DataSource(BaseModel):
    bucket: str
    """The name of the S3 bucket to read from."""

    aws_access_id: Optional[str] = None
    """The AWS access ID to use for authentication."""

    class_name: Optional[str] = None

    prefix: Optional[str] = None
    """The prefix of the S3 objects to read from."""

    regex_pattern: Optional[str] = None
    """The regex pattern to filter S3 objects. Must be a valid regex pattern."""

    s3_endpoint_url: Optional[str] = None
    """The S3 endpoint URL to use for authentication."""

    supports_access_control: Optional[bool] = None


class ComponentCloudAzStorageBlobDataSource(BaseModel):
    account_url: str
    """The Azure Storage Blob account URL to use for authentication."""

    container_name: str
    """The name of the Azure Storage Blob container to read from."""

    account_name: Optional[str] = None
    """The Azure Storage Blob account name to use for authentication."""

    blob: Optional[str] = None
    """The blob name to read from."""

    class_name: Optional[str] = None

    client_id: Optional[str] = None
    """The Azure AD client ID to use for authentication."""

    prefix: Optional[str] = None
    """The prefix of the Azure Storage Blob objects to read from."""

    supports_access_control: Optional[bool] = None

    tenant_id: Optional[str] = None
    """The Azure AD tenant ID to use for authentication."""


class ComponentCloudOneDriveDataSource(BaseModel):
    client_id: str
    """The client ID to use for authentication."""

    tenant_id: str
    """The tenant ID to use for authentication."""

    user_principal_name: str
    """The user principal name to use for authentication."""

    class_name: Optional[str] = None

    folder_id: Optional[str] = None
    """The ID of the OneDrive folder to read from."""

    folder_path: Optional[str] = None
    """The path of the OneDrive folder to read from."""

    required_exts: Optional[List[str]] = None
    """The list of required file extensions."""

    supports_access_control: Optional[Literal[True]] = None


class ComponentCloudSharepointDataSource(BaseModel):
    client_id: str
    """The client ID to use for authentication."""

    tenant_id: str
    """The tenant ID to use for authentication."""

    class_name: Optional[str] = None

    drive_name: Optional[str] = None
    """The name of the Sharepoint drive to read from."""

    exclude_path_patterns: Optional[List[str]] = None
    """List of regex patterns for file paths to exclude.

    Files whose paths (including filename) match any pattern will be excluded.
    Example: ['/temp/', '/backup/', '\\..git/', '\\..tmp$', '^~']
    """

    folder_id: Optional[str] = None
    """The ID of the Sharepoint folder to read from."""

    folder_path: Optional[str] = None
    """The path of the Sharepoint folder to read from."""

    get_permissions: Optional[bool] = None
    """Whether to get permissions for the sharepoint site."""

    include_path_patterns: Optional[List[str]] = None
    """List of regex patterns for file paths to include.

    Full paths (including filename) must match at least one pattern to be included.
    Example: ['/reports/', '/docs/.*\\..pdf$', '^Report.*\\..pdf$']
    """

    required_exts: Optional[List[str]] = None
    """The list of required file extensions."""

    site_id: Optional[str] = None
    """The ID of the SharePoint site to download from."""

    site_name: Optional[str] = None
    """The name of the SharePoint site to download from."""

    supports_access_control: Optional[Literal[True]] = None


class ComponentCloudSlackDataSource(BaseModel):
    channel_ids: Optional[str] = None
    """Slack Channel."""

    channel_patterns: Optional[str] = None
    """Slack Channel name pattern."""

    class_name: Optional[str] = None

    earliest_date: Optional[str] = None
    """Earliest date."""

    earliest_date_timestamp: Optional[float] = None
    """Earliest date timestamp."""

    latest_date: Optional[str] = None
    """Latest date."""

    latest_date_timestamp: Optional[float] = None
    """Latest date timestamp."""

    supports_access_control: Optional[bool] = None


class ComponentCloudNotionPageDataSource(BaseModel):
    class_name: Optional[str] = None

    database_ids: Optional[str] = None
    """The Notion Database Id to read content from."""

    page_ids: Optional[str] = None
    """The Page ID's of the Notion to read from."""

    supports_access_control: Optional[bool] = None


class ComponentCloudConfluenceDataSourceFailureHandling(BaseModel):
    """Configuration for handling failures during processing.

    Key-value object controlling failure handling behaviors.

    Example:
    {
      "skip_list_failures": true
    }

    Currently supports:
    - skip_list_failures: Skip failed batches/lists and continue processing
    """

    skip_list_failures: Optional[bool] = None
    """Whether to skip failed batches/lists and continue processing"""


class ComponentCloudConfluenceDataSource(BaseModel):
    authentication_mechanism: str
    """Type of Authentication for connecting to Confluence APIs."""

    server_url: str
    """The server URL of the Confluence instance."""

    class_name: Optional[str] = None

    cql: Optional[str] = None
    """The CQL query to use for fetching pages."""

    failure_handling: Optional[ComponentCloudConfluenceDataSourceFailureHandling] = None
    """Configuration for handling failures during processing.

    Key-value object controlling failure handling behaviors.

    Example: { "skip_list_failures": true }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing
    """

    index_restricted_pages: Optional[bool] = None
    """Whether to index restricted pages."""

    keep_markdown_format: Optional[bool] = None
    """Whether to keep the markdown format."""

    label: Optional[str] = None
    """The label to use for fetching pages."""

    page_ids: Optional[str] = None
    """The page IDs of the Confluence to read from."""

    space_key: Optional[str] = None
    """The space key to read from."""

    supports_access_control: Optional[bool] = None

    user_name: Optional[str] = None
    """The username to use for authentication."""


class ComponentCloudJiraDataSource(BaseModel):
    """Cloud Jira Data Source integrating JiraReader."""

    authentication_mechanism: str
    """Type of Authentication for connecting to Jira APIs."""

    query: str
    """JQL (Jira Query Language) query to search."""

    class_name: Optional[str] = None

    cloud_id: Optional[str] = None
    """The cloud ID, used in case of OAuth2."""

    email: Optional[str] = None
    """The email address to use for authentication."""

    server_url: Optional[str] = None
    """The server url for Jira Cloud."""

    supports_access_control: Optional[bool] = None


class ComponentCloudJiraDataSourceV2(BaseModel):
    """Cloud Jira Data Source integrating JiraReaderV2."""

    authentication_mechanism: str
    """Type of Authentication for connecting to Jira APIs."""

    query: str
    """JQL (Jira Query Language) query to search."""

    server_url: str
    """The server url for Jira Cloud."""

    api_version: Optional[Literal["2", "3"]] = None
    """Jira REST API version to use (2 or 3).

    3 supports Atlassian Document Format (ADF).
    """

    class_name: Optional[str] = None

    cloud_id: Optional[str] = None
    """The cloud ID, used in case of OAuth2."""

    email: Optional[str] = None
    """The email address to use for authentication."""

    expand: Optional[str] = None
    """Fields to expand in the response."""

    fields: Optional[List[str]] = None
    """List of fields to retrieve from Jira. If None, retrieves all fields."""

    get_permissions: Optional[bool] = None
    """Whether to fetch project role permissions and issue-level security"""

    requests_per_minute: Optional[int] = None
    """Rate limit for Jira API requests per minute."""

    supports_access_control: Optional[bool] = None


class ComponentCloudBoxDataSource(BaseModel):
    authentication_mechanism: Literal["developer_token", "ccg"]
    """The type of authentication to use (Developer Token or CCG)"""

    class_name: Optional[str] = None

    client_id: Optional[str] = None
    """
    Box API key used for identifying the application the user is authenticating with
    """

    enterprise_id: Optional[str] = None
    """Box Enterprise ID, if provided authenticates as service."""

    folder_id: Optional[str] = None
    """The ID of the Box folder to read from."""

    supports_access_control: Optional[bool] = None

    user_id: Optional[str] = None
    """Box User ID, if provided authenticates as user."""


Component: TypeAlias = Union[
    Dict[str, object],
    ComponentCloudS3DataSource,
    ComponentCloudAzStorageBlobDataSource,
    ComponentCloudOneDriveDataSource,
    ComponentCloudSharepointDataSource,
    ComponentCloudSlackDataSource,
    ComponentCloudNotionPageDataSource,
    ComponentCloudConfluenceDataSource,
    ComponentCloudJiraDataSource,
    ComponentCloudJiraDataSourceV2,
    ComponentCloudBoxDataSource,
]


class PipelineDataSource(BaseModel):
    """Schema for a data source in a pipeline."""

    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data source"""

    data_source_id: str
    """The ID of the data source."""

    last_synced_at: datetime
    """The last time the data source was automatically synced."""

    name: str
    """The name of the data source."""

    pipeline_id: str
    """The ID of the pipeline."""

    project_id: str

    source_type: Literal[
        "S3",
        "AZURE_STORAGE_BLOB",
        "GOOGLE_DRIVE",
        "MICROSOFT_ONEDRIVE",
        "MICROSOFT_SHAREPOINT",
        "SLACK",
        "NOTION_PAGE",
        "CONFLUENCE",
        "JIRA",
        "JIRA_V2",
        "BOX",
    ]

    created_at: Optional[datetime] = None
    """Creation datetime"""

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Custom metadata that will be present on all data loaded from the data source"""

    status: Optional[Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESS", "ERROR", "CANCELLED"]] = None
    """The status of the data source in the pipeline."""

    status_updated_at: Optional[datetime] = None
    """The last time the status was updated."""

    sync_interval: Optional[float] = None
    """The interval at which the data source should be synced."""

    sync_schedule_set_by: Optional[str] = None
    """The id of the user who set the sync schedule."""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    version_metadata: Optional[DataSourceReaderVersionMetadata] = None
    """Version metadata for the data source"""
