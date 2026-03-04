# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .classify_configuration_param import ClassifyConfigurationParam

__all__ = ["ClassifyCreateParams"]


class ClassifyCreateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    configuration: Optional[ClassifyConfigurationParam]
    """Configuration for classification."""

    configuration_id: Optional[str]
    """Product configuration ID for reusable presets"""

    file_id: Optional[str]
    """File ID to classify"""

    parse_job_id: Optional[str]
    """Parse job ID to classify"""

    transaction_id: Optional[str]
    """Idempotency key scoped to the project"""
