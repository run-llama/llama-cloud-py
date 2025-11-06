# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import EvalListSupportedModelsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_supported_models(self, client: LlamaCloud) -> None:
        eval = client.evals.list_supported_models()
        assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_supported_models(self, client: LlamaCloud) -> None:
        response = client.evals.with_raw_response.list_supported_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_supported_models(self, client: LlamaCloud) -> None:
        with client.evals.with_streaming_response.list_supported_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_supported_models(self, async_client: AsyncLlamaCloud) -> None:
        eval = await async_client.evals.list_supported_models()
        assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_supported_models(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.evals.with_raw_response.list_supported_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_supported_models(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.evals.with_streaming_response.list_supported_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalListSupportedModelsResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True
