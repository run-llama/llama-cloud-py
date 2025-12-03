# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SchemaValidateSchemaParams"]


class SchemaValidateSchemaParams(TypedDict, total=False):
    data_schema: Required[Union[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]], str]]
