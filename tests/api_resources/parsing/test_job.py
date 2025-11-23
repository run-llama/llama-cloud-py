# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import ParsingJob, PresignedURL

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_presigned_url(self, client: LlamaCloud) -> None:
        job = client.parsing.job.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        )
        assert_matches_type(PresignedURL, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_presigned_url(self, client: LlamaCloud) -> None:
        response = client.parsing.job.with_raw_response.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(PresignedURL, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_presigned_url(self, client: LlamaCloud) -> None:
        with client.parsing.job.with_streaming_response.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(PresignedURL, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_presigned_url(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.with_raw_response.generate_presigned_url(
                filename="filename",
                job_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.parsing.job.with_raw_response.generate_presigned_url(
                filename="",
                job_id="job_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        job = client.parsing.job.get(
            "job_id",
        )
        assert_matches_type(ParsingJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.parsing.job.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ParsingJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.parsing.job.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ParsingJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_details(self, client: LlamaCloud) -> None:
        job = client.parsing.job.get_details(
            "job_id",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_details(self, client: LlamaCloud) -> None:
        response = client.parsing.job.with_raw_response.get_details(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_details(self, client: LlamaCloud) -> None:
        with client.parsing.job.with_streaming_response.get_details(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(object, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_details(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.with_raw_response.get_details(
                "",
            )


class TestAsyncJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.parsing.job.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        )
        assert_matches_type(PresignedURL, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.with_raw_response.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(PresignedURL, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.with_streaming_response.generate_presigned_url(
            filename="filename",
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(PresignedURL, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.with_raw_response.generate_presigned_url(
                filename="filename",
                job_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.parsing.job.with_raw_response.generate_presigned_url(
                filename="",
                job_id="job_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.parsing.job.get(
            "job_id",
        )
        assert_matches_type(ParsingJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.with_raw_response.get(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ParsingJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.with_streaming_response.get(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ParsingJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_details(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.parsing.job.get_details(
            "job_id",
        )
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.with_raw_response.get_details(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(object, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.with_streaming_response.get_details(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(object, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.with_raw_response.get_details(
                "",
            )
