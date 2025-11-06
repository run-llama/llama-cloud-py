# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import PresignedURL
from llama_cloud.types.files import (
    PageScreenshotListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPageScreenshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        response = client.files.page_screenshots.with_raw_response.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = response.parse()
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with client.files.page_screenshots.with_streaming_response.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = response.parse()
            assert_matches_type(object, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.files.page_screenshots.with_raw_response.retrieve(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.files.page_screenshots.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = response.parse()
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.files.page_screenshots.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = response.parse()
            assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.files.page_screenshots.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_presigned_url(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_presigned_url_with_all_params(self, client: LlamaCloud) -> None:
        page_screenshot = client.files.page_screenshots.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_presigned_url(self, client: LlamaCloud) -> None:
        response = client.files.page_screenshots.with_raw_response.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = response.parse()
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_presigned_url(self, client: LlamaCloud) -> None:
        with client.files.page_screenshots.with_streaming_response.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = response.parse()
            assert_matches_type(PresignedURL, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_presigned_url(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.files.page_screenshots.with_raw_response.generate_presigned_url(
                page_index=0,
                id="",
            )


class TestAsyncPageScreenshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.files.page_screenshots.with_raw_response.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = await response.parse()
        assert_matches_type(object, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.files.page_screenshots.with_streaming_response.retrieve(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = await response.parse()
            assert_matches_type(object, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.files.page_screenshots.with_raw_response.retrieve(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.files.page_screenshots.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = await response.parse()
        assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.files.page_screenshots.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = await response.parse()
            assert_matches_type(PageScreenshotListResponse, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.files.page_screenshots.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_presigned_url_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        page_screenshot = await async_client.files.page_screenshots.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.files.page_screenshots.with_raw_response.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_screenshot = await response.parse()
        assert_matches_type(PresignedURL, page_screenshot, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.files.page_screenshots.with_streaming_response.generate_presigned_url(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_screenshot = await response.parse()
            assert_matches_type(PresignedURL, page_screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_presigned_url(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.files.page_screenshots.with_raw_response.generate_presigned_url(
                page_index=0,
                id="",
            )
