# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSourceReaderVersionMetadata"]


class DataSourceReaderVersionMetadata(BaseModel):
    reader_version: Optional[Literal["1.0", "2.0", "2.1"]] = None
    """The version of the reader to use for this data source."""
