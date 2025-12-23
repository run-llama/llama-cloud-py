# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ...._models import BaseModel

__all__ = ["SchemaValidateSchemaResponse"]


class SchemaValidateSchemaResponse(BaseModel):
    """Response schema for schema validation."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
