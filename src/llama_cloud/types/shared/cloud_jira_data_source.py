# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudJiraDataSource"]


class CloudJiraDataSource(BaseModel):
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
