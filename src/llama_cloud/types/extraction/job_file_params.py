# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["JobFileParams"]


class JobFileParams(TypedDict, total=False):
    extraction_agent_id: Required[str]
    """The id of the extraction agent"""

    file: Required[FileTypes]
    """The file to run the job on"""

    from_ui: bool

    config_override: Optional[str]
    """The config to override the extraction agent's config with as a JSON string"""

    data_schema_override: Optional[str]
    """
    The data schema to override the extraction agent's data schema with as a JSON
    string
    """
