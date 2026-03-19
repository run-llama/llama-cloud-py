# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ExtractValidateSchemaParams"]


class ExtractValidateSchemaParams(TypedDict, total=False):
    data_schema: Required[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """JSON schema to validate"""
