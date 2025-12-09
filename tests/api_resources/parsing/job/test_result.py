# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from llama_cloud.types.parsing.job import (
    ParsingJobJsonResult,
    ParsingJobTextResult,
    ParsingJobMarkdownResult,
    ParsingJobStructuredResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResult:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_image(self, client: LlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        result = client.parsing.job.result.get_image(
            name="name",
            job_id="job_id",
        )
        assert result.is_closed
        assert result.json() == {"foo": "bar"}
        assert cast(Any, result.is_closed) is True
        assert isinstance(result, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_image_with_all_params(self, client: LlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        result = client.parsing.job.result.get_image(
            name="name",
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert result.is_closed
        assert result.json() == {"foo": "bar"}
        assert cast(Any, result.is_closed) is True
        assert isinstance(result, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_image(self, client: LlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        result = client.parsing.job.result.with_raw_response.get_image(
            name="name",
            job_id="job_id",
        )

        assert result.is_closed is True
        assert result.http_request.headers.get("X-Stainless-Lang") == "python"
        assert result.json() == {"foo": "bar"}
        assert isinstance(result, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_image(self, client: LlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.parsing.job.result.with_streaming_response.get_image(
            name="name",
            job_id="job_id",
        ) as result:
            assert not result.is_closed
            assert result.http_request.headers.get("X-Stainless-Lang") == "python"

            assert result.json() == {"foo": "bar"}
            assert cast(Any, result.is_closed) is True
            assert isinstance(result, StreamedBinaryAPIResponse)

        assert cast(Any, result.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_image(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_image(
                name="name",
                job_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.parsing.job.result.with_raw_response.get_image(
                name="",
                job_id="job_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_json(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_json(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_json_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_json(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_json(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_json(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_json(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_json(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ParsingJobJsonResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_json(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_json(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_markdown(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_markdown(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_markdown_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_markdown(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_markdown(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_markdown(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_markdown(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_markdown(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_markdown(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_markdown(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_pdf(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_pdf(
            job_id="job_id",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_pdf_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_pdf(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_pdf(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_pdf(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_pdf(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_pdf(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(object, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_pdf(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_pdf(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_structured(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_structured(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_structured_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_structured(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_structured(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_structured(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_structured(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_structured(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_structured(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_structured(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_text(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_text(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_text_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_text(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_text(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_text(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_text(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_text(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ParsingJobTextResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_text(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_text(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xlsx(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_xlsx(
            job_id="job_id",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_xlsx_with_all_params(self, client: LlamaCloud) -> None:
        result = client.parsing.job.result.get_xlsx(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_xlsx(self, client: LlamaCloud) -> None:
        response = client.parsing.job.result.with_raw_response.get_xlsx(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_xlsx(self, client: LlamaCloud) -> None:
        with client.parsing.job.result.with_streaming_response.get_xlsx(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(object, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_xlsx(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.job.result.with_raw_response.get_xlsx(
                job_id="",
            )


class TestAsyncResult:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_image(self, async_client: AsyncLlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        result = await async_client.parsing.job.result.get_image(
            name="name",
            job_id="job_id",
        )
        assert result.is_closed
        assert await result.json() == {"foo": "bar"}
        assert cast(Any, result.is_closed) is True
        assert isinstance(result, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_image_with_all_params(
        self, async_client: AsyncLlamaCloud, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        result = await async_client.parsing.job.result.get_image(
            name="name",
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert result.is_closed
        assert await result.json() == {"foo": "bar"}
        assert cast(Any, result.is_closed) is True
        assert isinstance(result, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_image(self, async_client: AsyncLlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        result = await async_client.parsing.job.result.with_raw_response.get_image(
            name="name",
            job_id="job_id",
        )

        assert result.is_closed is True
        assert result.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await result.json() == {"foo": "bar"}
        assert isinstance(result, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_image(self, async_client: AsyncLlamaCloud, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/parsing/job/job_id/result/image/name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.parsing.job.result.with_streaming_response.get_image(
            name="name",
            job_id="job_id",
        ) as result:
            assert not result.is_closed
            assert result.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await result.json() == {"foo": "bar"}
            assert cast(Any, result.is_closed) is True
            assert isinstance(result, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, result.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_image(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_image(
                name="name",
                job_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_image(
                name="",
                job_id="job_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_json(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_json(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_json_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_json(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_json(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_json(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ParsingJobJsonResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_json(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_json(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ParsingJobJsonResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_json(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_json(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_markdown(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_markdown(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_markdown_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_markdown(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_markdown(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_markdown(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_markdown(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_markdown(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ParsingJobMarkdownResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_markdown(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_markdown(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_pdf(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_pdf(
            job_id="job_id",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_pdf_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_pdf(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_pdf(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_pdf(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_pdf(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_pdf(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(object, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_pdf(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_pdf(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_structured(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_structured(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_structured_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_structured(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_structured(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_structured(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_structured(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_structured(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ParsingJobStructuredResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_structured(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_structured(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_text(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_text(
            job_id="job_id",
        )
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_text_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_text(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_text(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_text(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ParsingJobTextResult, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_text(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_text(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ParsingJobTextResult, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_text(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_text(
                job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_xlsx(
            job_id="job_id",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_xlsx_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        result = await async_client.parsing.job.result.get_xlsx(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.job.result.with_raw_response.get_xlsx(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(object, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.job.result.with_streaming_response.get_xlsx(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(object, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_xlsx(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.job.result.with_raw_response.get_xlsx(
                job_id="",
            )
