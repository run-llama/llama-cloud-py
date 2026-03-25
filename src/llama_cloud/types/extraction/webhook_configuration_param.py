# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookConfigurationParam"]


class WebhookConfigurationParam(TypedDict, total=False):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "extract.pending",
                "extract.success",
                "extract.error",
                "extract.partial_success",
                "extract.cancelled",
                "parse.pending",
                "parse.running",
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
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str]
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_url: Optional[str]
    """URL to receive webhook POST notifications"""
