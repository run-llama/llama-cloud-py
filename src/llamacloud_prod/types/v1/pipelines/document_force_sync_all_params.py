# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocumentForceSyncAllParams"]


class DocumentForceSyncAllParams(TypedDict, total=False):
    batch_size: int

    only_failed: bool
    """
    Only sync retriable documents (failed/cancelled/not-started/stalled-in-progress)
    """
