# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["BedrockEmbeddingParam"]


class BedrockEmbeddingParam(TypedDict, total=False):
    additional_kwargs: Dict[str, object]
    """Additional kwargs for the bedrock client."""

    aws_access_key_id: Optional[str]
    """AWS Access Key ID to use"""

    aws_secret_access_key: Optional[str]
    """AWS Secret Access Key to use"""

    aws_session_token: Optional[str]
    """AWS Session Token to use"""

    class_name: str

    embed_batch_size: int
    """The batch size for embedding calls."""

    max_retries: int
    """The maximum number of API retries."""

    model_name: str
    """The modelId of the Bedrock model to use."""

    num_workers: Optional[int]
    """The number of workers to use for async embedding calls."""

    profile_name: Optional[str]
    """The name of aws profile to use. If not given, then the default profile is used."""

    region_name: Optional[str]
    """AWS region name to use. Uses region configured in AWS CLI if not passed"""

    timeout: float
    """The timeout for the Bedrock API request in seconds.

    It will be used for both connect and read timeouts.
    """
