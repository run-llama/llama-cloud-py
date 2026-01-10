# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudS3DataSource"]


class CloudS3DataSource(TypedDict, total=False):
    bucket: Required[str]
    """The name of the S3 bucket to read from."""

    aws_access_id: Optional[str]
    """The AWS access ID to use for authentication."""

    aws_access_secret: Optional[str]
    """The AWS access secret to use for authentication."""

    class_name: str

    prefix: Optional[str]
    """The prefix of the S3 objects to read from."""

    regex_pattern: Optional[str]
    """The regex pattern to filter S3 objects. Must be a valid regex pattern."""

    s3_endpoint_url: Optional[str]
    """The S3 endpoint URL to use for authentication."""

    supports_access_control: bool
