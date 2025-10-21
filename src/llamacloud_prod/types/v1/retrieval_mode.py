# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RetrievalMode"]

RetrievalMode: TypeAlias = Literal["chunks", "files_via_metadata", "files_via_content", "auto_routed"]
