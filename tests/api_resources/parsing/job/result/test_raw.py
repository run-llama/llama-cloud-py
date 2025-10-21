# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRaw:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_json(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_json(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_json(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_json(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_json(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_json(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_json(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_json(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_markdown(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_markdown(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_markdown(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_markdown(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_markdown(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_markdown(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_markdown(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_markdown(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_pdf(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_pdf(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_pdf(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_pdf(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_pdf(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_pdf(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_pdf(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_pdf(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_structured(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_structured(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_structured(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_structured(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_structured(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_structured(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_structured(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_structured(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_text(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_text(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_text(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_text(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_text(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_text(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_text(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_text(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xlsx(self, client: LlamacloudProd) -> None:
        raw = client.parsing.job.result.raw.get_xlsx(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xlsx(self, client: LlamacloudProd) -> None:
        response = client.parsing.job.result.raw.with_raw_response.get_xlsx(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xlsx(self, client: LlamacloudProd) -> None:
        with client.parsing.job.result.raw.with_streaming_response.get_xlsx(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xlsx(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.raw.with_raw_response.get_xlsx(
                "",
            )


class TestAsyncRaw:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_json(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_json(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_json(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_json(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_json(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_json(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_json(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_json(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_markdown(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_markdown(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_markdown(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_markdown(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_markdown(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_markdown(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_markdown(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_markdown(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_pdf(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_pdf(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_pdf(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_pdf(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_pdf(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_pdf(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_pdf(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_pdf(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_structured(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_structured(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_structured(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_structured(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_structured(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_structured(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_structured(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_structured(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_text(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_text(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_text(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_text(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_text(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_text(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_text(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_text(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xlsx(self, async_client: AsyncLlamacloudProd) -> None:
        raw = await async_client.parsing.job.result.raw.get_xlsx(
            "job_id",
        )
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xlsx(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.parsing.job.result.raw.with_raw_response.get_xlsx(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(object, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xlsx(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.parsing.job.result.raw.with_streaming_response.get_xlsx(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(object, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xlsx(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.raw.with_raw_response.get_xlsx(
                "",
            )
