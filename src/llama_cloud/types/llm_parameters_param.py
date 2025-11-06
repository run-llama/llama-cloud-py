# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LlmParametersParam"]


class LlmParametersParam(TypedDict, total=False):
    class_name: str

    model_name: Literal[
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
    """The name of the model to use for LLM completions."""

    system_prompt: Optional[str]
    """The system prompt to use for the completion."""

    temperature: Optional[float]
    """The temperature value for the model."""

    use_chain_of_thought_reasoning: Optional[bool]
    """Whether to use chain of thought reasoning."""

    use_citation: Optional[bool]
    """Whether to show citations in the response."""
