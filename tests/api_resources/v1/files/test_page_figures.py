# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llamacloud_prod import LlamacloudProd, AsyncLlamacloudProd
from llamacloud_prod.types.v1 import PresignedURL
from llamacloud_prod.types.v1.files import (
    PageFigureListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPageFigures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamacloudProd) -> None:
        response = client.v1.files.page_figures.with_raw_response.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = response.parse()
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamacloudProd) -> None:
        with client.v1.files.page_figures.with_streaming_response.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = response.parse()
            assert_matches_type(object, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.files.page_figures.with_raw_response.retrieve(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            client.v1.files.page_figures.with_raw_response.retrieve(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamacloudProd) -> None:
        response = client.v1.files.page_figures.with_raw_response.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = response.parse()
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamacloudProd) -> None:
        with client.v1.files.page_figures.with_streaming_response.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = response.parse()
            assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.files.page_figures.with_raw_response.list(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_presigned_url(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_presigned_url_with_all_params(self, client: LlamacloudProd) -> None:
        page_figure = client.v1.files.page_figures.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_presigned_url(self, client: LlamacloudProd) -> None:
        response = client.v1.files.page_figures.with_raw_response.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = response.parse()
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_presigned_url(self, client: LlamacloudProd) -> None:
        with client.v1.files.page_figures.with_streaming_response.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = response.parse()
            assert_matches_type(PresignedURL, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_presigned_url(self, client: LlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.files.page_figures.with_raw_response.generate_presigned_url(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            client.v1.files.page_figures.with_raw_response.generate_presigned_url(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )


class TestAsyncPageFigures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.files.page_figures.with_raw_response.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = await response.parse()
        assert_matches_type(object, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.files.page_figures.with_streaming_response.retrieve(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = await response.parse()
            assert_matches_type(object, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.files.page_figures.with_raw_response.retrieve(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            await async_client.v1.files.page_figures.with_raw_response.retrieve(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.files.page_figures.with_raw_response.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = await response.parse()
        assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.files.page_figures.with_streaming_response.list(
            page_index=0,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = await response.parse()
            assert_matches_type(PageFigureListResponse, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.files.page_figures.with_raw_response.list(
                page_index=0,
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_presigned_url(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_presigned_url_with_all_params(self, async_client: AsyncLlamacloudProd) -> None:
        page_figure = await async_client.v1.files.page_figures.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_presigned_url(self, async_client: AsyncLlamacloudProd) -> None:
        response = await async_client.v1.files.page_figures.with_raw_response.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_figure = await response.parse()
        assert_matches_type(PresignedURL, page_figure, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_presigned_url(self, async_client: AsyncLlamacloudProd) -> None:
        async with async_client.v1.files.page_figures.with_streaming_response.generate_presigned_url(
            figure_name="figure_name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_index=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_figure = await response.parse()
            assert_matches_type(PresignedURL, page_figure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_presigned_url(self, async_client: AsyncLlamacloudProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.files.page_figures.with_raw_response.generate_presigned_url(
                figure_name="figure_name",
                id="",
                page_index=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `figure_name` but received ''"):
            await async_client.v1.files.page_figures.with_raw_response.generate_presigned_url(
                figure_name="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_index=0,
            )
