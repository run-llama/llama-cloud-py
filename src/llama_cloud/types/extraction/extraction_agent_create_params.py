# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .extract_config_param import ExtractConfigParam

__all__ = ["ExtractionAgentCreateParams"]


class ExtractionAgentCreateParams(TypedDict, total=False):
    config: Required[ExtractConfigParam]
    """The configuration parameters for the extraction agent."""

    data_schema: Required[Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str]]
    """The schema of the data."""

    name: Required[str]
    """The name of the extraction schema"""

    organization_id: Optional[str]

    project_id: Optional[str]
