# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudConfluenceDataSourceParam", "FailureHandling"]


class FailureHandling(TypedDict, total=False):
    skip_list_failures: bool
    """Whether to skip failed batches/lists and continue processing"""


class CloudConfluenceDataSourceParam(TypedDict, total=False):
    authentication_mechanism: Required[str]
    """Type of Authentication for connecting to Confluence APIs."""

    server_url: Required[str]
    """The server URL of the Confluence instance."""

    api_token: Optional[str]
    """The API token to use for authentication."""

    class_name: str

    cql: Optional[str]
    """The CQL query to use for fetching pages."""

    failure_handling: FailureHandling
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
