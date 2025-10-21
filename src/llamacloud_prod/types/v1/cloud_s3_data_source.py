# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudS3DataSource"]


class CloudS3DataSource(BaseModel):
    bucket: str
    """The name of the S3 bucket to read from."""

    aws_access_id: Optional[str] = None
    """The AWS access ID to use for authentication."""

    class_name: Optional[str] = None

    prefix: Optional[str] = None
    """The prefix of the S3 objects to read from."""

    regex_pattern: Optional[str] = None
    """The regex pattern to filter S3 objects. Must be a valid regex pattern."""

    s3_endpoint_url: Optional[str] = None
    """The S3 endpoint URL to use for authentication."""

    supports_access_control: Optional[bool] = None
