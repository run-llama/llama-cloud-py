# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .metronome import (
    MetronomeResource,
    AsyncMetronomeResource,
    MetronomeResourceWithRawResponse,
    AsyncMetronomeResourceWithRawResponse,
    MetronomeResourceWithStreamingResponse,
    AsyncMetronomeResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.v1 import (
    billing_downgrade_plan_params,
    billing_create_customer_portal_session_params,
    billing_create_intent_and_customer_session_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.billing_downgrade_plan_response import BillingDowngradePlanResponse
from ....types.v1.billing_create_intent_and_customer_session_response import (
    BillingCreateIntentAndCustomerSessionResponse,
)

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def metronome(self) -> MetronomeResource:
        return MetronomeResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def create_customer_portal_session(
        self,
        *,
        organization_id: str,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Create a new customer portal session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/billing/customer-portal-session",
            body=maybe_transform(
                {"return_url": return_url},
                billing_create_customer_portal_session_params.BillingCreateCustomerPortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id},
                    billing_create_customer_portal_session_params.BillingCreateCustomerPortalSessionParams,
                ),
            ),
            cast_to=str,
        )

    def create_intent_and_customer_session(
        self,
        *,
        organization_id: str,
        plan_name: Literal[
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
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreateIntentAndCustomerSessionResponse:
        """
        Create a new setup intent and and a customer session.

        See https://docs.stripe.com/payments/existing-customers?platform=web&ui=elements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/billing/create-intent-and-customer-session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "plan_name": plan_name,
                    },
                    billing_create_intent_and_customer_session_params.BillingCreateIntentAndCustomerSessionParams,
                ),
            ),
            cast_to=BillingCreateIntentAndCustomerSessionResponse,
        )

    def downgrade_plan(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingDowngradePlanResponse:
        """
        Downgrade Plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/billing/downgrade-plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, billing_downgrade_plan_params.BillingDowngradePlanParams
                ),
            ),
            cast_to=BillingDowngradePlanResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def metronome(self) -> AsyncMetronomeResource:
        return AsyncMetronomeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llamacloud-prod-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def create_customer_portal_session(
        self,
        *,
        organization_id: str,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Create a new customer portal session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/billing/customer-portal-session",
            body=await async_maybe_transform(
                {"return_url": return_url},
                billing_create_customer_portal_session_params.BillingCreateCustomerPortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id},
                    billing_create_customer_portal_session_params.BillingCreateCustomerPortalSessionParams,
                ),
            ),
            cast_to=str,
        )

    async def create_intent_and_customer_session(
        self,
        *,
        organization_id: str,
        plan_name: Literal[
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
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreateIntentAndCustomerSessionResponse:
        """
        Create a new setup intent and and a customer session.

        See https://docs.stripe.com/payments/existing-customers?platform=web&ui=elements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/billing/create-intent-and-customer-session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "plan_name": plan_name,
                    },
                    billing_create_intent_and_customer_session_params.BillingCreateIntentAndCustomerSessionParams,
                ),
            ),
            cast_to=BillingCreateIntentAndCustomerSessionResponse,
        )

    async def downgrade_plan(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingDowngradePlanResponse:
        """
        Downgrade Plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/billing/downgrade-plan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, billing_downgrade_plan_params.BillingDowngradePlanParams
                ),
            ),
            cast_to=BillingDowngradePlanResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.create_customer_portal_session = to_raw_response_wrapper(
            billing.create_customer_portal_session,
        )
        self.create_intent_and_customer_session = to_raw_response_wrapper(
            billing.create_intent_and_customer_session,
        )
        self.downgrade_plan = to_raw_response_wrapper(
            billing.downgrade_plan,
        )

    @cached_property
    def metronome(self) -> MetronomeResourceWithRawResponse:
        return MetronomeResourceWithRawResponse(self._billing.metronome)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.create_customer_portal_session = async_to_raw_response_wrapper(
            billing.create_customer_portal_session,
        )
        self.create_intent_and_customer_session = async_to_raw_response_wrapper(
            billing.create_intent_and_customer_session,
        )
        self.downgrade_plan = async_to_raw_response_wrapper(
            billing.downgrade_plan,
        )

    @cached_property
    def metronome(self) -> AsyncMetronomeResourceWithRawResponse:
        return AsyncMetronomeResourceWithRawResponse(self._billing.metronome)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.create_customer_portal_session = to_streamed_response_wrapper(
            billing.create_customer_portal_session,
        )
        self.create_intent_and_customer_session = to_streamed_response_wrapper(
            billing.create_intent_and_customer_session,
        )
        self.downgrade_plan = to_streamed_response_wrapper(
            billing.downgrade_plan,
        )

    @cached_property
    def metronome(self) -> MetronomeResourceWithStreamingResponse:
        return MetronomeResourceWithStreamingResponse(self._billing.metronome)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.create_customer_portal_session = async_to_streamed_response_wrapper(
            billing.create_customer_portal_session,
        )
        self.create_intent_and_customer_session = async_to_streamed_response_wrapper(
            billing.create_intent_and_customer_session,
        )
        self.downgrade_plan = async_to_streamed_response_wrapper(
            billing.downgrade_plan,
        )

    @cached_property
    def metronome(self) -> AsyncMetronomeResourceWithStreamingResponse:
        return AsyncMetronomeResourceWithStreamingResponse(self._billing.metronome)
