# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_stream(self, client: LlamacloudProd) -> None:
        test_stream = client.v1.test.stream()
        test_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_stream(self, client: LlamacloudProd) -> None:
        response = client.v1.test.with_raw_response.stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_stream(self, client: LlamacloudProd) -> None:
        with client.v1.test.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncTest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_stream(self, async_client: AsyncLlamacloudProd) -> None:
        test_stream = await async_client.v1.test.stream()
        await test_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.test.with_raw_response.stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.test.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
