# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types import V1GetJobsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_jobs(self, client: LlamacloudProd) -> None:
        v1 = client.v1.get_jobs()
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_jobs_with_all_params(self, client: LlamacloudProd) -> None:
        v1 = client.v1.get_jobs(
            job_name="job_name",
            limit=100,
            offset=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="sort",
        )
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_jobs(self, client: LlamacloudProd) -> None:
        response = client.v1.with_raw_response.get_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_jobs(self, client: LlamacloudProd) -> None:
        with client.v1.with_streaming_response.get_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetJobsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_jobs(self, async_client: AsyncLlamacloudProd) -> None:
        v1 = await async_client.v1.get_jobs()
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_jobs_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        v1 = await async_client.v1.get_jobs(
            job_name="job_name",
            limit=100,
            offset=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="sort",
        )
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_jobs(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.with_raw_response.get_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetJobsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_jobs(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.with_streaming_response.get_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetJobsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
