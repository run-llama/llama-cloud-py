# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EvalListSupportedModelsResponse",
    "EvalListSupportedModelsResponseItem",
    "EvalListSupportedModelsResponseItemDetails",
]


class EvalListSupportedModelsResponseItemDetails(BaseModel):
    description: str
    """The description of the LLM model."""

    multi_modal: bool
    """Whether the model supports multi-modal image input"""

    name: str
    """The name of the LLM model."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)


class EvalListSupportedModelsResponseItem(BaseModel):
    details: EvalListSupportedModelsResponseItemDetails
    """The details of the supported LLM model."""

    name: str
    """The name of the supported LLM model."""

    enabled: Optional[bool] = None
    """Whether the LLM model is enabled for use in LlamaCloud."""


EvalListSupportedModelsResponse: TypeAlias = List[EvalListSupportedModelsResponseItem]
