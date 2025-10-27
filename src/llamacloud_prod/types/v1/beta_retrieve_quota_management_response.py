# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaRetrieveQuotaManagementResponse", "Item", "ItemConfigurationValue"]


class ItemConfigurationValue(BaseModel):
    numerator: int
    """The rate numerator"""

    denominator: Optional[int] = None
    """The rate limit denominator"""

    denominator_units: Optional[Literal["second", "minute", "hour", "day"]] = None
    """The default rate limit denominator units"""


class Item(BaseModel):
    configuration_metadata: Optional[Dict[str, object]] = None
    """The configuration metadata"""

    configuration_type: Literal[
        "rate_limit_parse_concurrent_premium",
        "rate_limit_parse_concurrent_default",
        "rate_limit_concurrent_jobs_in_execution_default",
        "rate_limit_concurrent_jobs_in_execution_doc_ingest",
        "limit_embedding_character",
        "limit_files_per_index",
    ]
    """The quota configuration type"""

    configuration_value: ItemConfigurationValue
    """The quota configuration value"""

    source_id: str
    """The source ID, e.g. the organization ID"""

    source_type: Literal["organization"]
    """The source type, e.g. 'organization'"""

    status: Literal["ACTIVE", "INACTIVE"]
    """The status of the quota, i.e. 'ACTIVE' or 'INACTIVE'"""

    id: Optional[str] = None
    """The system-generated UUID for the quota"""

    created_at: Optional[datetime] = None
    """The creation date of the quota configuration in the database"""

    ended_at: Optional[datetime] = None
    """The end date of the quota"""

    idempotency_key: Optional[str] = None
    """The idempotency key"""

    started_at: Optional[datetime] = None
    """The start date of the quota"""

    updated_at: Optional[datetime] = None
    """The last updated date of the quota configuration in the database"""


class BetaRetrieveQuotaManagementResponse(BaseModel):
    items: List[Item]

    page: int

    pages: int

    size: int

    total: int
