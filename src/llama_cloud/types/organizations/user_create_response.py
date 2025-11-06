# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user_organization import UserOrganization

__all__ = ["UserCreateResponse"]

UserCreateResponse: TypeAlias = List[UserOrganization]
