# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.pipelines import (
    ImageListPageFiguresResponse,
    ImageListPageScreenshotsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_figure(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_figure_with_all_params(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_page_figure(self, client: LlamaCloud) -> None:
        response = client.pipelines.images.with_raw_response.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_page_figure(self, client: LlamaCloud) -> None:
        with client.pipelines.images.with_streaming_response.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_page_figure(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pipelines.images.with_raw_response.get_page_figure(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            client.pipelines.images.with_raw_response.get_page_figure(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_screenshot(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_page_screenshot_with_all_params(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_page_screenshot(self, client: LlamaCloud) -> None:
        response = client.pipelines.images.with_raw_response.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_page_screenshot(self, client: LlamaCloud) -> None:
        with client.pipelines.images.with_streaming_response.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_page_screenshot(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pipelines.images.with_raw_response.get_page_screenshot(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_page_figures(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_page_figures_with_all_params(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_page_figures(self, client: LlamaCloud) -> None:
        response = client.pipelines.images.with_raw_response.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_page_figures(self, client: LlamaCloud) -> None:
        with client.pipelines.images.with_streaming_response.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_page_figures(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pipelines.images.with_raw_response.list_page_figures(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_page_screenshots(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_page_screenshots_with_all_params(self, client: LlamaCloud) -> None:
        image = client.pipelines.images.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_page_screenshots(self, client: LlamaCloud) -> None:
        response = client.pipelines.images.with_raw_response.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_page_screenshots(self, client: LlamaCloud) -> None:
        with client.pipelines.images.with_streaming_response.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_page_screenshots(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pipelines.images.with_raw_response.list_page_screenshots(
                id="",
            )


class TestAsyncImages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_figure(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_figure_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_page_figure(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.pipelines.images.with_raw_response.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_page_figure(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.pipelines.images.with_streaming_response.get_page_figure(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_page_figure(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pipelines.images.with_raw_response.get_page_figure(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            await async_client.pipelines.images.with_raw_response.get_page_figure(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_screenshot(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_page_screenshot_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_page_screenshot(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.pipelines.images.with_raw_response.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_page_screenshot(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.pipelines.images.with_streaming_response.get_page_screenshot(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_page_screenshot(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pipelines.images.with_raw_response.get_page_screenshot(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_page_figures(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_page_figures_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_page_figures(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.pipelines.images.with_raw_response.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_page_figures(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.pipelines.images.with_streaming_response.list_page_figures(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageListPageFiguresResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_page_figures(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pipelines.images.with_raw_response.list_page_figures(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_page_screenshots(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_page_screenshots_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        image = await async_client.pipelines.images.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_page_screenshots(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.pipelines.images.with_raw_response.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_page_screenshots(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.pipelines.images.with_streaming_response.list_page_screenshots(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageListPageScreenshotsResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_page_screenshots(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pipelines.images.with_raw_response.list_page_screenshots(
                id="",
            )
