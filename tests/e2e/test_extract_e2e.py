"""
End-to-end tests for the Extract V2 resource.

These tests hit the real LlamaCloud API and require:
  - LLAMA_CLOUD_API_KEY env var to be set

Run with:
  LLAMA_CLOUD_API_KEY=... pytest tests/e2e/test_extract_e2e.py -v -s -o "addopts="
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from llama_cloud.types import ExtractV2Job, ExtractConfigurationParam

pytestmark = [
    pytest.mark.skipif(
        not os.environ.get("LLAMA_CLOUD_API_KEY"),
        reason="LLAMA_CLOUD_API_KEY not set",
    ),
    pytest.mark.filterwarnings("ignore::ResourceWarning"),
]

TEST_PDF = Path(__file__).parent.parent / "test_files" / "TOS.pdf"

SIMPLE_CONFIG: ExtractConfigurationParam = {
    "extract_options": {
        "data_schema": {
            "type": "object",
            "properties": {"title": {"type": "string", "description": "The title or heading of the document"}},
        },
    },
}


@pytest.fixture(scope="module")
def client() -> LlamaCloud:
    return LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


@pytest.fixture(scope="module")
def async_client() -> AsyncLlamaCloud:
    return AsyncLlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


@pytest.fixture(scope="module")
def file_id(client: LlamaCloud) -> str:
    """Upload a test file once and return its file ID for all tests."""
    with open(TEST_PDF, "rb") as f:
        uploaded = client.files.create(file=f, purpose="extract")
    return uploaded.id


class TestExtractE2ESync:
    def test_create_and_get(self, client: LlamaCloud, file_id: str) -> None:
        """Test creating an extract job and fetching it by ID."""
        job = client.extract.create(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
        )
        assert isinstance(job, ExtractV2Job)
        assert job.id
        assert job.status in ("PENDING", "THROTTLED", "RUNNING", "COMPLETED")

        fetched = client.extract.get(job_id=job.id)
        assert fetched.id == job.id

    def test_wait_for_completion(self, client: LlamaCloud, file_id: str) -> None:
        """Test creating a job then waiting for it to complete."""
        job = client.extract.create(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
        )

        completed = client.extract.wait_for_completion(
            job.id,
            polling_interval=2.0,
            verbose=True,
        )
        assert completed.status == "COMPLETED"
        assert completed.extract_result is not None

    def test_run(self, client: LlamaCloud, file_id: str) -> None:
        """Test the end-to-end run() convenience method."""
        result = client.extract.run(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
            polling_interval=2.0,
            verbose=True,
        )
        assert isinstance(result, ExtractV2Job)
        assert result.status == "COMPLETED"
        assert result.extract_result is not None

    def test_list_jobs(self, client: LlamaCloud) -> None:
        """Test listing extract jobs (at least one should exist from prior tests)."""
        page = client.extract.list()
        jobs = list(page)
        assert len(jobs) > 0
        assert all(isinstance(j, ExtractV2Job) for j in jobs)


class TestExtractE2EAsync:
    async def test_create_and_get(self, async_client: AsyncLlamaCloud, file_id: str) -> None:
        """Test creating an extract job and fetching it by ID (async)."""
        job = await async_client.extract.create(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
        )
        assert isinstance(job, ExtractV2Job)
        assert job.id

        fetched = await async_client.extract.get(job_id=job.id)
        assert fetched.id == job.id

    async def test_wait_for_completion(self, async_client: AsyncLlamaCloud, file_id: str) -> None:
        """Test creating a job then waiting for it to complete (async)."""
        job = await async_client.extract.create(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
        )

        completed = await async_client.extract.wait_for_completion(
            job.id,
            polling_interval=2.0,
            verbose=True,
        )
        assert completed.status == "COMPLETED"
        assert completed.extract_result is not None

    async def test_run(self, async_client: AsyncLlamaCloud, file_id: str) -> None:
        """Test the end-to-end run() convenience method (async)."""
        result = await async_client.extract.run(
            type="file_id",
            value=file_id,
            config=SIMPLE_CONFIG,
            polling_interval=2.0,
            verbose=True,
        )
        assert isinstance(result, ExtractV2Job)
        assert result.status == "COMPLETED"
        assert result.extract_result is not None
