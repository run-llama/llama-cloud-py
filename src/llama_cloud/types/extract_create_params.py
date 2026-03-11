# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .extract_configuration_param import ExtractConfigurationParam
from .extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["ExtractCreateParams"]


class ExtractCreateParams(TypedDict, total=False):
    type: Required[Literal["url", "file_id", "parse_job_id"]]
    """Type of document input."""

    value: Required[str]
    """Document identifier (URL, file ID, or parse job ID)."""

    organization_id: Optional[str]

    project_id: Optional[str]

    config: Optional[ExtractConfigurationParam]
    """Extraction configuration combining parse and extract settings."""

    configuration_id: Optional[str]
    """Saved extract configuration ID (mutually exclusive with config)"""

    webhook_configurations: Optional[Iterable[WebhookConfigurationParam]]
    """The outbound webhook configurations"""
