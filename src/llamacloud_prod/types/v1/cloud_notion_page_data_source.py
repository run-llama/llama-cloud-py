# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudNotionPageDataSource"]


class CloudNotionPageDataSource(BaseModel):
    class_name: Optional[str] = None

    database_ids: Optional[str] = None
    """The Notion Database Id to read content from."""

    page_ids: Optional[str] = None
    """The Page ID's of the Notion to read from."""

    supports_access_control: Optional[bool] = None
