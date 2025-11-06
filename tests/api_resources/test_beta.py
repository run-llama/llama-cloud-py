# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import BetaRetrieveQuotaManagementResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_quota_management(self, client: LlamaCloud) -> None:
        beta = client.beta.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        )
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_quota_management_with_all_params(self, client: LlamaCloud) -> None:
        beta = client.beta.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
            page=0,
            page_size=0,
        )
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_quota_management(self, client: LlamaCloud) -> None:
        response = client.beta.with_raw_response.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_quota_management(self, client: LlamaCloud) -> None:
        with client.beta.with_streaming_response.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_quota_management(self, async_client: AsyncLlamaCloud) -> None:
        beta = await async_client.beta.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        )
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_quota_management_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        beta = await async_client.beta.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
            page=0,
            page_size=0,
        )
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_quota_management(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.with_raw_response.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_quota_management(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.with_streaming_response.retrieve_quota_management(
            source_id="source_id",
            source_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaRetrieveQuotaManagementResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True
