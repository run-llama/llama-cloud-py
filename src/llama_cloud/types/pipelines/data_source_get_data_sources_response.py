# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .pipeline_data_source import PipelineDataSource

__all__ = ["DataSourceGetDataSourcesResponse"]

DataSourceGetDataSourcesResponse: TypeAlias = List[PipelineDataSource]
