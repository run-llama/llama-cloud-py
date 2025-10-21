# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["UserUpdateRemoveParams", "Body"]


class UserUpdateRemoveParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    email: Optional[str]
    """The user's email address."""

    project_id_list: Optional[SequenceNotStr[str]]
    """The project ids"""

    user_id: Optional[str]
    """The user's ID."""
