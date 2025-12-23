# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .extract_config import ExtractConfig

__all__ = ["ExtractAgent"]


class ExtractAgent(BaseModel):
    """Schema and configuration for an extraction agent."""

    id: str
    """The id of the extraction agent."""

    config: ExtractConfig
    """The configuration parameters for the extraction agent."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """The schema of the data."""

    name: str
    """The name of the extraction agent."""

    project_id: str
    """The ID of the project that the extraction agent belongs to."""

    created_at: Optional[datetime] = None
    """The creation time of the extraction agent."""

    custom_configuration: Optional[Literal["default"]] = None
    """Custom configuration type for the extraction agent.

    Currently supports 'default'.
    """

    updated_at: Optional[datetime] = None
    """The last update time of the extraction agent."""
