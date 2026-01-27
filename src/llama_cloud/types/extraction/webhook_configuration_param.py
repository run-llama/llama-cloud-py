# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookConfigurationParam"]


class WebhookConfigurationParam(TypedDict, total=False):
    """Allows the user to configure webhook options for notifications and callbacks."""

    webhook_events: Optional[
        List[
            Literal[
                "extract.pending",
                "extract.success",
                "extract.error",
                "extract.partial_success",
                "extract.cancelled",
                "parse.pending",
                "parse.success",
                "parse.error",
                "parse.partial_success",
                "parse.cancelled",
                "classify.pending",
                "classify.success",
                "classify.error",
                "classify.partial_success",
                "classify.cancelled",
                "unmapped_event",
            ]
        ]
    ]
    """List of event names to subscribe to"""

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers to include with webhook requests."""

    webhook_output_format: Optional[str]
    """The output format to use for the webhook.

    Defaults to string if none supplied. Currently supported values: string, json
    """

    webhook_url: Optional[str]
    """The URL to send webhook notifications to."""
