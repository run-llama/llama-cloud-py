# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .extract_config_param import ExtractConfigParam

__all__ = ["ExtractionAgentUpdateParams"]


class ExtractionAgentUpdateParams(TypedDict, total=False):
    config: Required[ExtractConfigParam]
    """The configuration parameters for the extraction agent."""

    data_schema: Required[Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str]]
    """The schema of the data"""
