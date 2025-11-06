# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .message_role import MessageRole
from .llm_parameters_param import LlmParametersParam

__all__ = ["PipelineChatParams", "Data", "Message"]


class PipelineChatParams(TypedDict, total=False):
    class_name: str

    data: Data

    messages: Iterable[Message]


class Data(TypedDict, total=False):
    class_name: str

    llm_parameters: Optional[LlmParametersParam]

    retrieval_parameters: "PresetRetrievalParamsParam"
    """
    Schema for the search params for an retrieval execution that can be preset for a
    pipeline.
    """


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[MessageRole]
    """Message role."""

    id: str
    """ID of the message, if any. a UUID."""

    class_name: str

    data: Optional[Dict[str, object]]
    """Additional data to be stored with the message."""


from .preset_retrieval_params_param import PresetRetrievalParamsParam
