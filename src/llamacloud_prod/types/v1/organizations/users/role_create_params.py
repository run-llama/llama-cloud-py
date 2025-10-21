# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RoleCreateParams"]


class RoleCreateParams(TypedDict, total=False):
    body_organization_id: Required[Annotated[str, PropertyInfo(alias="organization_id")]]
    """The organization's ID."""

    role_id: Required[str]
    """The role's ID."""

    user_id: Required[str]
    """The user's ID."""
