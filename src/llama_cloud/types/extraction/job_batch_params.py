# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .extract_config_param import ExtractConfigParam
from .webhook_configuration_param import WebhookConfigurationParam

__all__ = ["JobBatchParams"]


class JobBatchParams(TypedDict, total=False):
    extraction_agent_id: Required[str]
    """The id of the extraction agent"""

    file_ids: Required[SequenceNotStr[str]]
    """The ids of the files"""

    from_ui: bool

    config_override: Optional[ExtractConfigParam]
    """Configuration parameters for the extraction agent."""

    data_schema_override: Union[
        Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str, None
    ]
    """The data schema to override the extraction agent's data schema with"""

    webhook_configurations: Optional[Iterable[WebhookConfigurationParam]]
    """The outbound webhook configurations"""
