# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthReadSelfResponse", "Claims", "Restrict"]


class Claims(BaseModel):
    allow_org_deletion: Optional[bool] = None
    """Whether the user is allowed to delete organizations."""

    allowed_app: Optional[bool] = None
    """Whether the user is allowed to access the app."""

    allowed_classify: Optional[bool] = None
    """Whether the user is allowed to access the classifier feature."""

    allowed_org_creation: Optional[bool] = None
    """Whether the user is allowed to create organizations."""

    allowed_report: Optional[bool] = None
    """Whether the user is allowed to access llama-report generation."""

    allowed_spreadsheet: Optional[bool] = None
    """Whether the user is allowed to access the spreadsheet feature."""

    api_datasource_access: Optional[bool] = None
    """Whether the user is allowed to access API data sources."""

    extraction_test_user: Optional[bool] = None
    """Whether the user is a test user for extraction.

    This will include additional debug metadata and access to test endpoints.
    """

    max_document_ingestion_jobs_in_execution: Optional[int] = None
    """The maximum number of document ingestion jobs the user can have in execution."""

    max_jobs_in_execution_per_job_type: Optional[int] = None
    """The maximum number of jobs the user can have in execution per job type."""

    max_metadata_update_jobs_in_execution: Optional[int] = None
    """The maximum number of metadata update jobs the user can have in execution."""


class Restrict(BaseModel):
    project_id: Optional[str] = None
    """The project ID to restrict the user to."""


class AuthReadSelfResponse(BaseModel):
    id: str

    email: str

    claims: Optional[Claims] = None
    """The user's custom claims."""

    created_at: Optional[datetime] = None
    """The user's creation date."""

    first_name: Optional[str] = None
    """The user's first name."""

    last_login_provider: Optional[Literal["oidc", "basic", "no_auth"]] = None
    """The last login provider."""

    last_name: Optional[str] = None
    """The user's last name."""

    name: Optional[str] = None
    """The user's name."""

    restrict: Optional[Restrict] = None
    """The restrictions on the user."""
