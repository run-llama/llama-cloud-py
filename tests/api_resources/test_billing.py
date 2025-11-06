# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    BillingDowngradePlanResponse,
    BillingCreateIntentAndCustomerSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_customer_portal_session(self, client: LlamaCloud) -> None:
        billing = client.billing.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        )
        assert_matches_type(str, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_customer_portal_session(self, client: LlamaCloud) -> None:
        response = client.billing.with_raw_response.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(str, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_customer_portal_session(self, client: LlamaCloud) -> None:
        with client.billing.with_streaming_response.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(str, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_intent_and_customer_session(self, client: LlamaCloud) -> None:
        billing = client.billing.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        )
        assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_intent_and_customer_session(self, client: LlamaCloud) -> None:
        response = client.billing.with_raw_response.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_intent_and_customer_session(self, client: LlamaCloud) -> None:
        with client.billing.with_streaming_response.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_downgrade_plan(self, client: LlamaCloud) -> None:
        billing = client.billing.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_downgrade_plan(self, client: LlamaCloud) -> None:
        response = client.billing.with_raw_response.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_downgrade_plan(self, client: LlamaCloud) -> None:
        with client.billing.with_streaming_response.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_customer_portal_session(self, async_client: AsyncLlamaCloud) -> None:
        billing = await async_client.billing.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        )
        assert_matches_type(str, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_customer_portal_session(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.billing.with_raw_response.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(str, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_customer_portal_session(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.billing.with_streaming_response.create_customer_portal_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(str, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_intent_and_customer_session(self, async_client: AsyncLlamaCloud) -> None:
        billing = await async_client.billing.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        )
        assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_intent_and_customer_session(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.billing.with_raw_response.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_intent_and_customer_session(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.billing.with_streaming_response.create_intent_and_customer_session(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan_name="free",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCreateIntentAndCustomerSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_downgrade_plan(self, async_client: AsyncLlamaCloud) -> None:
        billing = await async_client.billing.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_downgrade_plan(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.billing.with_raw_response.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_downgrade_plan(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.billing.with_streaming_response.downgrade_plan(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingDowngradePlanResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True
