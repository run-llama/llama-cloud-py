# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CloudJiraDataSourceV2"]


class CloudJiraDataSourceV2(TypedDict, total=False):
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
