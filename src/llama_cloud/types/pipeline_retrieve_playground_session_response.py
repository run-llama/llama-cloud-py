# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .message_role import MessageRole
from .llm_parameters import LlmParameters

__all__ = ["PipelineRetrievePlaygroundSessionResponse", "ChatMessage", "ChatMessageAnnotation"]


class ChatMessageAnnotation(BaseModel):
    data: str

    type: str

    class_name: Optional[str] = None


class ChatMessage(BaseModel):
    id: str

    index: int
    """The index of the message in the chat."""

    role: MessageRole
    """The role of the message."""

    additional_kwargs: Optional[Dict[str, str]] = None
    """Additional arguments passed to the model"""

    annotations: Optional[List[ChatMessageAnnotation]] = None
    """Retrieval annotations for the message."""

    class_name: Optional[str] = None

    content: Optional[str] = None
    """Text content of the generation"""


class PipelineRetrievePlaygroundSessionResponse(BaseModel):
    id: str
    """Unique identifier"""

    llm_params_id: str

    pipeline_id: str

    retrieval_params_id: str

    user_id: str

    chat_messages: Optional[List[ChatMessage]] = None
    """Chat message history for this session."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    llm_params: Optional[LlmParameters] = None
    """LLM parameters last used in this session."""

    retrieval_params: Optional["PresetRetrievalParams"] = None
    """Preset retrieval parameters last used in this session."""

    updated_at: Optional[datetime] = None
    """Update datetime"""


from .preset_retrieval_params import PresetRetrievalParams
