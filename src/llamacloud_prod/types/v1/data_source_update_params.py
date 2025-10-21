# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .cloud_s3_data_source_param import CloudS3DataSourceParam
from .cloud_box_data_source_param import CloudBoxDataSourceParam
from .cloud_jira_data_source_param import CloudJiraDataSourceParam
from .cloud_slack_data_source_param import CloudSlackDataSourceParam
from .configurable_data_source_names import ConfigurableDataSourceNames
from .cloud_jira_data_source_v2_param import CloudJiraDataSourceV2Param
from .cloud_one_drive_data_source_param import CloudOneDriveDataSourceParam
from .cloud_confluence_data_source_param import CloudConfluenceDataSourceParam
from .cloud_sharepoint_data_source_param import CloudSharepointDataSourceParam
from .cloud_notion_page_data_source_param import CloudNotionPageDataSourceParam
from .cloud_az_storage_blob_data_source_param import CloudAzStorageBlobDataSourceParam

__all__ = ["DataSourceUpdateParams", "Component"]


class DataSourceUpdateParams(TypedDict, total=False):
    source_type: Required[ConfigurableDataSourceNames]

    component: Optional[Component]
    """Component that implements the data source"""

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Custom metadata that will be present on all data loaded from the data source"""

    name: Optional[str]
    """The name of the data source."""


Component: TypeAlias = Union[
    Dict[str, object],
    CloudS3DataSourceParam,
    CloudAzStorageBlobDataSourceParam,
    CloudOneDriveDataSourceParam,
    CloudSharepointDataSourceParam,
    CloudSlackDataSourceParam,
    CloudNotionPageDataSourceParam,
    CloudConfluenceDataSourceParam,
    CloudJiraDataSourceParam,
    CloudJiraDataSourceV2Param,
    CloudBoxDataSourceParam,
]
