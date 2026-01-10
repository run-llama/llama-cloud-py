# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudJiraDataSourceV2"]


class CloudJiraDataSourceV2(BaseModel):
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
