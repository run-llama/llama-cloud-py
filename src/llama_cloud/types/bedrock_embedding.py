# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BedrockEmbedding"]


class BedrockEmbedding(BaseModel):
    additional_kwargs: Optional[Dict[str, object]] = None
    """Additional kwargs for the bedrock client."""

    aws_access_key_id: Optional[str] = None
    """AWS Access Key ID to use"""

    aws_secret_access_key: Optional[str] = None
    """AWS Secret Access Key to use"""

    aws_session_token: Optional[str] = None
    """AWS Session Token to use"""

    class_name: Optional[str] = None

    embed_batch_size: Optional[int] = None
    """The batch size for embedding calls."""

    max_retries: Optional[int] = None
    """The maximum number of API retries."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """The modelId of the Bedrock model to use."""

    num_workers: Optional[int] = None
    """The number of workers to use for async embedding calls."""

    profile_name: Optional[str] = None
    """The name of aws profile to use. If not given, then the default profile is used."""

    region_name: Optional[str] = None
    """AWS region name to use. Uses region configured in AWS CLI if not passed"""

    timeout: Optional[float] = None
    """The timeout for the Bedrock API request in seconds.

    It will be used for both connect and read timeouts.
    """
