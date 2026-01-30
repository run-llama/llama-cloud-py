# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .classifier_rule_param import ClassifierRuleParam
from .classify_parsing_configuration_param import ClassifyParsingConfigurationParam

__all__ = ["JobCreateParams", "WebhookConfiguration"]


class JobCreateParams(TypedDict, total=False):
    file_ids: Required[SequenceNotStr[str]]
    """The IDs of the files to classify"""

    rules: Required[Iterable[ClassifierRuleParam]]
    """The rules to classify the files"""

    organization_id: Optional[str]

    project_id: Optional[str]

    mode: Literal["FAST", "MULTIMODAL"]
    """The classification mode to use"""

    parsing_configuration: ClassifyParsingConfigurationParam
    """The configuration for the parsing job"""

    webhook_configurations: Iterable[WebhookConfiguration]
    """List of webhook configurations for notifications"""


class WebhookConfiguration(TypedDict, total=False):
    webhook_events: Optional[SequenceNotStr[str]]
    """List of events that trigger webhook notifications"""

    webhook_headers: Optional[Dict[str, object]]
    """Custom headers to include in webhook requests"""

    webhook_url: Optional[str]
    """Webhook URL for receiving parsing notifications"""
