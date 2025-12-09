# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Retriever"]


class Retriever(BaseModel):
    """An entity that retrieves context nodes from several sub RetrieverTools."""

    id: str
    """Unique identifier"""

    name: str
    """A name for the retriever tool.

    Will default to the pipeline name if not provided.
    """

    project_id: str
    """The ID of the project this retriever resides in."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    pipelines: Optional[List["RetrieverPipeline"]] = None
    """The pipelines this retriever uses."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


from .retriever_pipeline import RetrieverPipeline
