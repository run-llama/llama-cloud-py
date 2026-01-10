# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudJiraDataSource"]


class CloudJiraDataSource(TypedDict, total=False):
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
