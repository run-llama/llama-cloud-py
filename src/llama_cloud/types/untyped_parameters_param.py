# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UntypedParametersParam"]


class UntypedParametersParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Catch-all for configurations without a dedicated typed schema.

    Accepts arbitrary JSON fields alongside ``product_type``.
    """

    product_type: Required[Literal["unknown"]]
    """Product type."""
