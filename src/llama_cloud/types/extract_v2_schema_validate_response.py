# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ExtractV2SchemaValidateResponse"]


class ExtractV2SchemaValidateResponse(BaseModel):
    """Response schema for schema validation."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """Validated JSON schema"""
