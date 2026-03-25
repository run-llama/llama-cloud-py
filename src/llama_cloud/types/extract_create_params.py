# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .extract_configuration_param import ExtractConfigurationParam
from .extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["ExtractCreateParams"]


class ExtractCreateParams(TypedDict, total=False):
    document_input_value: Required[str]
    """File ID or Parse Job ID to extract from"""

    organization_id: Optional[str]

    project_id: Optional[str]

    configuration: Optional[ExtractConfigurationParam]
    """Extract configuration combining parse and extract settings."""

    configuration_id: Optional[str]
    """Saved extract configuration ID (mutually exclusive with configuration)"""

    webhook_configurations: Optional[Iterable[WebhookConfigurationParam]]
    """Outbound webhook endpoints to notify on job status changes"""
