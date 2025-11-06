# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import PresignedURL

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        table = client.beta.spreadsheet.jobs.tables.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        )
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        table = client.beta.spreadsheet.jobs.tables.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
            expires_at_seconds=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        response = client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with client.beta.spreadsheet.jobs.tables.with_streaming_response.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(PresignedURL, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
                table_type="table",
                spreadsheet_job_id="",
                table_id="table_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id` but received ''"):
            client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
                table_type="table",
                spreadsheet_job_id="spreadsheet_job_id",
                table_id="",
            )


class TestAsyncTables:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        table = await async_client.beta.spreadsheet.jobs.tables.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        )
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        table = await async_client.beta.spreadsheet.jobs.tables.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
            expires_at_seconds=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(PresignedURL, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.spreadsheet.jobs.tables.with_streaming_response.retrieve(
            table_type="table",
            spreadsheet_job_id="spreadsheet_job_id",
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(PresignedURL, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            await async_client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
                table_type="table",
                spreadsheet_job_id="",
                table_id="table_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id` but received ''"):
            await async_client.beta.spreadsheet.jobs.tables.with_raw_response.retrieve(
                table_type="table",
                spreadsheet_job_id="spreadsheet_job_id",
                table_id="",
            )
