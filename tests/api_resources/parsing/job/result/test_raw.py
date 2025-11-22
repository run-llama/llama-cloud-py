# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRaw:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_json(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_json(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_json(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_json(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_json(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_json(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_json(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_json(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_markdown(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_markdown(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_markdown(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_markdown(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_markdown(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_markdown(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_markdown(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_markdown(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_pdf(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_pdf(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_pdf(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_pdf(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_pdf(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_pdf(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_pdf(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_pdf(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_structured(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_structured(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_structured(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_structured(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_structured(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_structured(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_structured(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_structured(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_text(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_text(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_text(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_text(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_text(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_text(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_text(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_text(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_xlsx(self, client: LlamaCloud) -> None:
        raw = client.parsing.job.result.raw.get_raw_xlsx(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_xlsx(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_raw_xlsx(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_xlsx(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_raw_xlsx(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_xlsx(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_raw_xlsx(
                "",
            )


class TestAsyncRaw:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_json(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_json(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_json(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_json(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_json(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_json(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_json(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_json(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_markdown(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_markdown(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_markdown(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_markdown(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_markdown(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_markdown(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_markdown(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_markdown(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_pdf(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_pdf(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_pdf(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_pdf(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_pdf(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_pdf(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_pdf(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_pdf(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_structured(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_structured(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_structured(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_structured(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_structured(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_structured(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_structured(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_structured(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_text(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_text(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_text(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_text(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_text(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_text(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_text(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_text(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        raw = await async_client.parsing.job.result.raw.get_raw_xlsx(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_raw_xlsx(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_raw_xlsx(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_raw_xlsx(
                "",
            )
