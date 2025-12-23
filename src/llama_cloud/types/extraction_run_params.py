# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .extraction.extract_config_param import ExtractConfigParam
from .extraction.webhook_configuration_param import WebhookConfigurationParam

__all__ = ["ExtractionRunParams", "File"]


class ExtractionRunParams(TypedDict, total=False):
    config: Required[ExtractConfigParam]
    """The configuration parameters for the extraction"""

    data_schema: Required[Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str]]
    """The schema of the data to extract"""

    organization_id: Optional[str]

    project_id: Optional[str]

    file: Optional[File]
    """Schema for file data with base64 content and MIME type."""

    file_id: Optional[str]
    """The ID of the file to extract from"""

    text: Optional[str]
    """The text content to extract from"""

    webhook_configurations: Optional[Iterable[WebhookConfigurationParam]]
    """The outbound webhook configurations"""


class File(TypedDict, total=False):
    """Schema for file data with base64 content and MIME type."""

    data: Required[str]
    """The file content as base64-encoded string"""

    mime_type: Required[str]
    """The MIME type of the file (e.g., 'application/pdf', 'text/plain')"""
