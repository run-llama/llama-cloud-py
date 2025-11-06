# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConfigurableDataSourceNames"]

ConfigurableDataSourceNames: TypeAlias = Literal[
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
