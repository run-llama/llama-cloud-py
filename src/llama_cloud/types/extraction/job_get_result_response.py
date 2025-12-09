# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["JobGetResultResponse"]


class JobGetResultResponse(BaseModel):
    """Schema for an extraction resultset."""

    data: Union[
        Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]],
        List[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]],
        None,
    ] = None
    """The data extracted from the file"""

    extraction_agent_id: str
    """The id of the extraction agent"""

    extraction_metadata: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """The metadata extracted from the file"""

    run_id: str
    """The id of the extraction run"""
