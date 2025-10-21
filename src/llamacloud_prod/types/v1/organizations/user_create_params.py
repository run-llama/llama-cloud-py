# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["UserCreateParams", "Body"]


class UserCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    project_ids: Required[Optional[SequenceNotStr[str]]]
    """The project IDs to add the user to."""

    email: Optional[str]
    """The user's email address."""

    role_id: Optional[str]
    """The role ID to assign to the user."""

    user_id: Optional[str]
    """The user's ID."""
