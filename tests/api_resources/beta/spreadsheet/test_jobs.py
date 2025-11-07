# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedClassifyJobs, AsyncPaginatedClassifyJobs
from llama_cloud.types.beta.spreadsheet import (
    SpreadsheetJob,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "extraction_range": "extraction_range",
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "use_experimental_processing": True,
            },
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.beta.spreadsheet.jobs.with_raw_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.beta.spreadsheet.jobs.with_streaming_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SpreadsheetJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        response = client.beta.spreadsheet.jobs.with_raw_response.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with client.beta.spreadsheet.jobs.with_streaming_response.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SpreadsheetJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            client.beta.spreadsheet.jobs.with_raw_response.retrieve(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.list()
        assert_matches_type(SyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        job = client.beta.spreadsheet.jobs.list(
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.spreadsheet.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.spreadsheet.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "extraction_range": "extraction_range",
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "use_experimental_processing": True,
            },
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.spreadsheet.jobs.with_raw_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.spreadsheet.jobs.with_streaming_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(SpreadsheetJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.spreadsheet.jobs.with_raw_response.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(SpreadsheetJob, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.spreadsheet.jobs.with_streaming_response.retrieve(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(SpreadsheetJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            await async_client.beta.spreadsheet.jobs.with_raw_response.retrieve(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.list()
        assert_matches_type(AsyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job = await async_client.beta.spreadsheet.jobs.list(
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.spreadsheet.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.spreadsheet.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncPaginatedClassifyJobs[SpreadsheetJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True
