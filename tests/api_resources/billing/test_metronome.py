# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.billing import MetronomeGetDashboardResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetronome:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_dashboard(self, client: LlamaCloud) -> None:
        metronome = client.billing.metronome.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_dashboard_with_all_params(self, client: LlamaCloud) -> None:
        metronome = client.billing.metronome.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_type="invoices",
        )
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_dashboard(self, client: LlamaCloud) -> None:
        response = client.billing.metronome.with_raw_response.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metronome = response.parse()
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_dashboard(self, client: LlamaCloud) -> None:
        with client.billing.metronome.with_streaming_response.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metronome = response.parse()
            assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetronome:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_dashboard(self, async_client: AsyncLlamaCloud) -> None:
        metronome = await async_client.billing.metronome.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_dashboard_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        metronome = await async_client.billing.metronome.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dashboard_type="invoices",
        )
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_dashboard(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.billing.metronome.with_raw_response.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metronome = await response.parse()
        assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_dashboard(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.billing.metronome.with_streaming_response.get_dashboard(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metronome = await response.parse()
            assert_matches_type(MetronomeGetDashboardResponse, metronome, path=["response"])

        assert cast(Any, response.is_closed) is True
