from __future__ import annotations

from typing import List
from datetime import datetime

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from llama_cloud._polling import PollingError, PollingTimeoutError
from llama_cloud.types.classify_get_response import ClassifyGetResponse
from llama_cloud.types.classify_configuration import Rule, ClassifyConfiguration


def _make_job(status: str, error_message: str | None = None) -> ClassifyGetResponse:
    return ClassifyGetResponse(
        id="clj-test",
        configuration=ClassifyConfiguration(rules=[Rule(type="invoice", description="d")]),
        document_input_type="file_id",
        file_input="dfl-test",
        project_id="prj-test",
        status=status,  # type: ignore[arg-type]
        user_id="usr-test",
        created_at=datetime(2026, 4, 16),
        error_message=error_message,
    )


class _StubSequence:
    def __init__(self, jobs: List[ClassifyGetResponse]) -> None:
        self._jobs = list(jobs)
        self.calls = 0

    def __call__(self, *_args: object, **_kwargs: object) -> ClassifyGetResponse:
        self.calls += 1
        if self._jobs:
            return self._jobs.pop(0) if len(self._jobs) > 1 else self._jobs[0]
        raise AssertionError("Unexpected extra get() call")


class _AsyncStubSequence:
    def __init__(self, jobs: List[ClassifyGetResponse]) -> None:
        self._jobs = list(jobs)
        self.calls = 0

    async def __call__(self, *_args: object, **_kwargs: object) -> ClassifyGetResponse:
        self.calls += 1
        if self._jobs:
            return self._jobs.pop(0) if len(self._jobs) > 1 else self._jobs[0]
        raise AssertionError("Unexpected extra get() call")


def test_wait_for_completion_sync_completed() -> None:
    client = LlamaCloud(api_key="test", base_url="http://unused")
    stub = _StubSequence(
        [
            _make_job("RUNNING"),
            _make_job("RUNNING"),
            _make_job("COMPLETED"),
        ]
    )
    client.classify.get = stub  # type: ignore[method-assign]

    result = client.classify.wait_for_completion("clj-test", polling_interval=0.0, max_interval=0.0)

    assert result.status == "COMPLETED"
    assert stub.calls == 3


def test_wait_for_completion_sync_failed_raises() -> None:
    client = LlamaCloud(api_key="test", base_url="http://unused")
    client.classify.get = _StubSequence([_make_job("FAILED", error_message="boom")])  # type: ignore[method-assign]

    with pytest.raises(PollingError, match="boom"):
        client.classify.wait_for_completion("clj-test", polling_interval=0.0, max_interval=0.0)


def test_wait_for_completion_sync_timeout_raises() -> None:
    client = LlamaCloud(api_key="test", base_url="http://unused")
    client.classify.get = _StubSequence([_make_job("RUNNING")])  # type: ignore[method-assign]

    with pytest.raises(PollingTimeoutError):
        client.classify.wait_for_completion(
            "clj-test",
            polling_interval=0.01,
            max_interval=0.01,
            timeout=0.01,
        )


def test_wait_for_completion_sync_rejects_empty_job_id() -> None:
    client = LlamaCloud(api_key="test", base_url="http://unused")
    with pytest.raises(ValueError):
        client.classify.wait_for_completion("")


@pytest.mark.asyncio
async def test_wait_for_completion_async_completed() -> None:
    client = AsyncLlamaCloud(api_key="test", base_url="http://unused")
    stub = _AsyncStubSequence(
        [
            _make_job("PENDING"),
            _make_job("RUNNING"),
            _make_job("COMPLETED"),
        ]
    )
    client.classify.get = stub  # type: ignore[method-assign]

    result = await client.classify.wait_for_completion("clj-test", polling_interval=0.0, max_interval=0.0)

    assert result.status == "COMPLETED"
    assert stub.calls == 3


@pytest.mark.asyncio
async def test_wait_for_completion_async_failed_returns_final_status() -> None:
    client = AsyncLlamaCloud(api_key="test", base_url="http://unused")
    client.classify.get = _AsyncStubSequence([_make_job("FAILED", error_message="boom")])  # type: ignore[method-assign]

    # The async polling helper logs and returns rather than raising; mirror that behavior here.
    result = await client.classify.wait_for_completion("clj-test", polling_interval=0.0, max_interval=0.0)
    assert result.status == "FAILED"


@pytest.mark.asyncio
async def test_wait_for_completion_async_rejects_empty_job_id() -> None:
    client = AsyncLlamaCloud(api_key="test", base_url="http://unused")
    with pytest.raises(ValueError):
        await client.classify.wait_for_completion("")
