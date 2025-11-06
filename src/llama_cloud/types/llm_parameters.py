# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LlmParameters"]


class LlmParameters(BaseModel):
    class_name: Optional[str] = None

    api_model_name: Optional[
        Literal[
            "GPT_4O",
            "GPT_4O_MINI",
            "GPT_4_1",
            "GPT_4_1_NANO",
            "GPT_4_1_MINI",
            "AZURE_OPENAI_GPT_4O",
            "AZURE_OPENAI_GPT_4O_MINI",
            "AZURE_OPENAI_GPT_4_1",
            "AZURE_OPENAI_GPT_4_1_MINI",
            "AZURE_OPENAI_GPT_4_1_NANO",
            "CLAUDE_3_5_SONNET",
            "CLAUDE_4_5_SONNET",
            "BEDROCK_CLAUDE_3_5_SONNET_V1",
            "BEDROCK_CLAUDE_3_5_SONNET_V2",
            "VERTEX_AI_CLAUDE_3_5_SONNET_V2",
        ]
    ] = FieldInfo(alias="model_name", default=None)
    """The name of the model to use for LLM completions."""

    system_prompt: Optional[str] = None
    """The system prompt to use for the completion."""

    temperature: Optional[float] = None
    """The temperature value for the model."""

    use_chain_of_thought_reasoning: Optional[bool] = None
    """Whether to use chain of thought reasoning."""

    use_citation: Optional[bool] = None
    """Whether to show citations in the response."""
