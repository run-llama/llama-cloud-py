# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "UsageAndPlan",
    "Plan",
    "PlanLimits",
    "PlanCurrentBillingPeriod",
    "PlanRecurringCredit",
    "PlanRecurringCreditCreditType",
    "Usage",
    "UsageActiveFreeCreditsUsage",
]


class PlanLimits(BaseModel):
    allow_pay_as_you_go: bool
    """Whether usage is allowed after credit grants are exhausted"""

    max_concurrent_index_jobs: Optional[int] = None

    max_concurrent_parse_jobs_other: Optional[int] = None

    max_concurrent_parse_jobs_premium: Optional[int] = None

    max_data_sinks: Optional[int] = None

    max_data_sources: Optional[int] = None

    max_embedding_models: Optional[int] = None

    max_extraction_agents: Optional[int] = None

    max_extraction_jobs: Optional[int] = None

    max_extraction_runs: Optional[int] = None

    max_files_per_index: Optional[int] = None

    max_indexes: Optional[int] = None

    max_monthly_invoice_total_usd: Optional[int] = None

    max_organizations: Optional[int] = None

    max_pages_per_index: Optional[int] = None

    max_projects: Optional[int] = None

    max_published_agents: Optional[int] = None

    max_report_agent_sessions: Optional[int] = None

    max_users: Optional[int] = None

    mfa_enabled: bool

    sso_enabled: bool

    subscription_cost_usd: int

    spending_soft_alerts_usd_cents: Optional[List[int]] = None
    """The amount of USD cents at which a soft alert should be triggered"""


class PlanCurrentBillingPeriod(BaseModel):
    end_date: datetime

    start_date: datetime


class PlanRecurringCreditCreditType(BaseModel):
    id: str

    name: str


class PlanRecurringCredit(BaseModel):
    credit_amount: int

    credit_type: PlanRecurringCreditCreditType

    name: str

    priority: float

    product_id: str
    """The ID of the product in Metronome used to represent the credit grant"""

    rollover_fraction: float
    """
    The fraction of the credit that will roll over to the next period, between 0 and
    1
    """

    periods_duration: Optional[float] = None
    """How many billing periods the credit grant will last for"""


class Plan(BaseModel):
    limits: PlanLimits

    metronome_plan_type: Literal["plan", "contract"]

    metronome_rate_card_alias: Optional[str] = None

    name: Literal[
        "free",
        "llama_parse",
        "enterprise",
        "unknown",
        "free_contract",
        "pro",
        "enterprise_contract",
        "enterprise_poc",
        "free_v1",
        "starter_v1",
        "pro_v1",
    ]

    plan_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL"]

    id: Optional[str] = None
    """The ID of the plan in Metronome"""

    current_billing_period: Optional[PlanCurrentBillingPeriod] = None
    """The current billing period"""

    ending_before: Optional[datetime] = None
    """The date the plan ends on"""

    failure_count: Optional[int] = None
    """The number of payment failures for this organization"""

    is_payment_failed: Optional[bool] = None
    """Whether the organization has a failed payment that requires support contact"""

    metronome_customer_id: Optional[str] = None
    """The ID of the customer in Metronome"""

    recurring_credits: Optional[List[PlanRecurringCredit]] = None

    starting_on: Optional[datetime] = None
    """The date the plan starts on"""


class UsageActiveFreeCreditsUsage(BaseModel):
    expires_at: datetime

    grant_name: str

    remaining_balance: int

    starting_balance: int


class Usage(BaseModel):
    active_alerts: Optional[
        List[
            Literal[
                "plan_spend_limit_exceeded",
                "plan_spend_limit_soft_alert",
                "configured_spend_limit_exceeded",
                "free_credits_exhausted",
                "internal_spending_alert",
                "has_spending_alert",
            ]
        ]
    ] = None

    active_free_credits_usage: Optional[List[UsageActiveFreeCreditsUsage]] = None

    current_invoice_total_usd_cents: Optional[int] = None

    total_extraction_agents: Optional[int] = None

    total_indexed_pages: Optional[int] = None

    total_indexes: Optional[int] = None

    total_users: Optional[int] = None


class UsageAndPlan(BaseModel):
    plan: Plan

    usage: Usage
    """Response model"""
