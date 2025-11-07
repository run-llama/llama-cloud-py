# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .role import Role

__all__ = ["OrganizationGetRolesResponse"]

OrganizationGetRolesResponse: TypeAlias = List[Role]
