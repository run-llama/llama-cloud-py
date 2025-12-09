# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "DataSourceCreateParams",
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


class DataSourceCreateParams(TypedDict, total=False):
    component: Required[Component]
    """Component that implements the data source"""

    name: Required[str]
    """The name of the data source."""

    source_type: Required[
        Literal[
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
    ]

    organization_id: Optional[str]

    project_id: Optional[str]

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Custom metadata that will be present on all data loaded from the data source"""


class ComponentCloudS3DataSource(TypedDict, total=False):
    bucket: Required[str]
    """The name of the S3 bucket to read from."""

    aws_access_id: Optional[str]
    """The AWS access ID to use for authentication."""

    aws_access_secret: Optional[str]
    """The AWS access secret to use for authentication."""

    class_name: str

    prefix: Optional[str]
    """The prefix of the S3 objects to read from."""

    regex_pattern: Optional[str]
    """The regex pattern to filter S3 objects. Must be a valid regex pattern."""

    s3_endpoint_url: Optional[str]
    """The S3 endpoint URL to use for authentication."""

    supports_access_control: bool


class ComponentCloudAzStorageBlobDataSource(TypedDict, total=False):
    account_url: Required[str]
    """The Azure Storage Blob account URL to use for authentication."""

    container_name: Required[str]
    """The name of the Azure Storage Blob container to read from."""

    account_key: Optional[str]
    """The Azure Storage Blob account key to use for authentication."""

    account_name: Optional[str]
    """The Azure Storage Blob account name to use for authentication."""

    blob: Optional[str]
    """The blob name to read from."""

    class_name: str

    client_id: Optional[str]
    """The Azure AD client ID to use for authentication."""

    client_secret: Optional[str]
    """The Azure AD client secret to use for authentication."""

    prefix: Optional[str]
    """The prefix of the Azure Storage Blob objects to read from."""

    supports_access_control: bool

    tenant_id: Optional[str]
    """The Azure AD tenant ID to use for authentication."""


class ComponentCloudOneDriveDataSource(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to use for authentication."""

    client_secret: Required[str]
    """The client secret to use for authentication."""

    tenant_id: Required[str]
    """The tenant ID to use for authentication."""

    user_principal_name: Required[str]
    """The user principal name to use for authentication."""

    class_name: str

    folder_id: Optional[str]
    """The ID of the OneDrive folder to read from."""

    folder_path: Optional[str]
    """The path of the OneDrive folder to read from."""

    required_exts: Optional[SequenceNotStr[str]]
    """The list of required file extensions."""

    supports_access_control: Literal[True]


class ComponentCloudSharepointDataSource(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to use for authentication."""

    client_secret: Required[str]
    """The client secret to use for authentication."""

    tenant_id: Required[str]
    """The tenant ID to use for authentication."""

    class_name: str

    drive_name: Optional[str]
    """The name of the Sharepoint drive to read from."""

    exclude_path_patterns: Optional[SequenceNotStr[str]]
    """List of regex patterns for file paths to exclude.

    Files whose paths (including filename) match any pattern will be excluded.
    Example: ['/temp/', '/backup/', '\\..git/', '\\..tmp$', '^~']
    """

    folder_id: Optional[str]
    """The ID of the Sharepoint folder to read from."""

    folder_path: Optional[str]
    """The path of the Sharepoint folder to read from."""

    get_permissions: Optional[bool]
    """Whether to get permissions for the sharepoint site."""

    include_path_patterns: Optional[SequenceNotStr[str]]
    """List of regex patterns for file paths to include.

    Full paths (including filename) must match at least one pattern to be included.
    Example: ['/reports/', '/docs/.*\\..pdf$', '^Report.*\\..pdf$']
    """

    required_exts: Optional[SequenceNotStr[str]]
    """The list of required file extensions."""

    site_id: Optional[str]
    """The ID of the SharePoint site to download from."""

    site_name: Optional[str]
    """The name of the SharePoint site to download from."""

    supports_access_control: Literal[True]


class ComponentCloudSlackDataSource(TypedDict, total=False):
    slack_token: Required[str]
    """Slack Bot Token."""

    channel_ids: Optional[str]
    """Slack Channel."""

    channel_patterns: Optional[str]
    """Slack Channel name pattern."""

    class_name: str

    earliest_date: Optional[str]
    """Earliest date."""

    earliest_date_timestamp: Optional[float]
    """Earliest date timestamp."""

    latest_date: Optional[str]
    """Latest date."""

    latest_date_timestamp: Optional[float]
    """Latest date timestamp."""

    supports_access_control: bool


class ComponentCloudNotionPageDataSource(TypedDict, total=False):
    integration_token: Required[str]
    """The integration token to use for authentication."""

    class_name: str

    database_ids: Optional[str]
    """The Notion Database Id to read content from."""

    page_ids: Optional[str]
    """The Page ID's of the Notion to read from."""

    supports_access_control: bool


class ComponentCloudConfluenceDataSourceFailureHandling(TypedDict, total=False):
    """Configuration for handling failures during processing.

    Key-value object controlling failure handling behaviors.

    Example:
    {
      "skip_list_failures": true
    }

    Currently supports:
    - skip_list_failures: Skip failed batches/lists and continue processing
    """

    skip_list_failures: bool
    """Whether to skip failed batches/lists and continue processing"""


class ComponentCloudConfluenceDataSource(TypedDict, total=False):
    authentication_mechanism: Required[str]
    """Type of Authentication for connecting to Confluence APIs."""

    server_url: Required[str]
    """The server URL of the Confluence instance."""

    api_token: Optional[str]
    """The API token to use for authentication."""

    class_name: str

    cql: Optional[str]
    """The CQL query to use for fetching pages."""

    failure_handling: ComponentCloudConfluenceDataSourceFailureHandling
    """Configuration for handling failures during processing.

    Key-value object controlling failure handling behaviors.

    Example: { "skip_list_failures": true }

    Currently supports:

    - skip_list_failures: Skip failed batches/lists and continue processing
    """

    index_restricted_pages: bool
    """Whether to index restricted pages."""

    keep_markdown_format: bool
    """Whether to keep the markdown format."""

    label: Optional[str]
    """The label to use for fetching pages."""

    page_ids: Optional[str]
    """The page IDs of the Confluence to read from."""

    space_key: Optional[str]
    """The space key to read from."""

    supports_access_control: bool

    user_name: Optional[str]
    """The username to use for authentication."""


class ComponentCloudJiraDataSource(TypedDict, total=False):
    """Cloud Jira Data Source integrating JiraReader."""

    authentication_mechanism: Required[str]
    """Type of Authentication for connecting to Jira APIs."""

    query: Required[str]
    """JQL (Jira Query Language) query to search."""

    api_token: Optional[str]
    """The API/ Access Token used for Basic, PAT and OAuth2 authentication."""

    class_name: str

    cloud_id: Optional[str]
    """The cloud ID, used in case of OAuth2."""

    email: Optional[str]
    """The email address to use for authentication."""

    server_url: Optional[str]
    """The server url for Jira Cloud."""

    supports_access_control: bool


class ComponentCloudJiraDataSourceV2(TypedDict, total=False):
    """Cloud Jira Data Source integrating JiraReaderV2."""

    authentication_mechanism: Required[str]
    """Type of Authentication for connecting to Jira APIs."""

    query: Required[str]
    """JQL (Jira Query Language) query to search."""

    server_url: Required[str]
    """The server url for Jira Cloud."""

    api_token: Optional[str]
    """The API Access Token used for Basic, PAT and OAuth2 authentication."""

    api_version: Literal["2", "3"]
    """Jira REST API version to use (2 or 3).

    3 supports Atlassian Document Format (ADF).
    """

    class_name: str

    cloud_id: Optional[str]
    """The cloud ID, used in case of OAuth2."""

    email: Optional[str]
    """The email address to use for authentication."""

    expand: Optional[str]
    """Fields to expand in the response."""

    fields: Optional[SequenceNotStr[str]]
    """List of fields to retrieve from Jira. If None, retrieves all fields."""

    get_permissions: bool
    """Whether to fetch project role permissions and issue-level security"""

    requests_per_minute: Optional[int]
    """Rate limit for Jira API requests per minute."""

    supports_access_control: bool


class ComponentCloudBoxDataSource(TypedDict, total=False):
    authentication_mechanism: Required[Literal["developer_token", "ccg"]]
    """The type of authentication to use (Developer Token or CCG)"""

    class_name: str

    client_id: Optional[str]
    """
    Box API key used for identifying the application the user is authenticating with
    """

    client_secret: Optional[str]
    """Box API secret used for making auth requests."""

    developer_token: Optional[str]
    """
    Developer token for authentication if authentication_mechanism is
    'developer_token'.
    """

    enterprise_id: Optional[str]
    """Box Enterprise ID, if provided authenticates as service."""

    folder_id: Optional[str]
    """The ID of the Box folder to read from."""

    supports_access_control: bool

    user_id: Optional[str]
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
