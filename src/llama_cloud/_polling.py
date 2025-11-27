# File manually added for polling utilities. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
import asyncio
from typing import Literal, TypeVar, Callable, Awaitable
from logging import getLogger
from typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")
logger = getLogger(__name__)

BackoffStrategy = Literal["constant", "linear", "exponential"]


class PollingTimeoutError(Exception):
    """Raised when polling times out before completion."""

    pass


class PollingError(Exception):
    """Raised when a job fails during polling."""

    pass


def _calculate_next_interval(
    current_interval: float,
    backoff: BackoffStrategy,
    max_interval: float,
) -> float:
    """Calculate the next polling interval based on backoff strategy."""
    if backoff == "constant":
        return current_interval
    elif backoff == "linear":
        return min(current_interval + 1.0, max_interval)
    elif backoff == "exponential":
        return min(current_interval * 2.0, max_interval)
    else:
        raise ValueError(f"Invalid backoff strategy: {backoff}")


def poll_until_complete(
    get_status_fn: Callable[[], T],
    is_complete_fn: Callable[[T], bool],
    is_error_fn: Callable[[T], bool],
    get_error_message_fn: Callable[[T], str],
    *,
    polling_interval: float = 1.0,
    max_interval: float = 5.0,
    timeout: float = 2000.0,
    backoff: BackoffStrategy = "linear",
    verbose: bool = False,
) -> T:
    """
    Synchronous polling utility that polls until a job completes.

    Args:
        get_status_fn: Function to get the current status
        is_complete_fn: Function to check if the status indicates completion
        is_error_fn: Function to check if the status indicates an error
        get_error_message_fn: Function to extract error message from status
        polling_interval: Initial polling interval in seconds
        max_interval: Maximum polling interval for backoff
        timeout: Maximum time to wait in seconds
        backoff: Backoff strategy - "constant", "linear", or "exponential"
        verbose: Print progress indicators every 10 polls

    Returns:
        The final status object when complete

    Raises:
        PollingTimeoutError: If polling times out
        PollingError: If the job fails
    """
    start_time = time.time()
    tries = 0
    current_interval = polling_interval

    while True:
        time.sleep(current_interval)
        tries += 1

        # Get current status
        status = get_status_fn()

        # Check if complete
        if is_complete_fn(status):
            if verbose and tries > 1:
                logger.info(f"\nCompleted after {tries} checks")
            return status

        # Check if error
        if is_error_fn(status):
            error_msg = get_error_message_fn(status)
            raise PollingError(error_msg)

        # Check timeout
        elapsed = time.time() - start_time
        if elapsed > timeout:
            raise PollingTimeoutError(f"Polling timed out after {elapsed:.1f}s (timeout: {timeout}s)")

        # Print progress
        if verbose and tries % 10 == 0:
            logger.info(".")

        # Calculate next interval
        current_interval = _calculate_next_interval(current_interval, backoff, max_interval)


async def poll_until_complete_async(
    get_status_fn: Callable[[], Awaitable[T]],
    is_complete_fn: Callable[[T], bool],
    is_error_fn: Callable[[T], bool],
    get_error_message_fn: Callable[[T], str],
    *,
    polling_interval: float = 1.0,
    max_interval: float = 5.0,
    timeout: float = 2000.0,
    backoff: BackoffStrategy = "linear",
    verbose: bool = False,
) -> T:
    """
    Asynchronous polling utility that polls until a job completes.

    Args:
        get_status_fn: Async function to get the current status
        is_complete_fn: Function to check if the status indicates completion
        is_error_fn: Function to check if the status indicates an error
        get_error_message_fn: Function to extract error message from status
        polling_interval: Initial polling interval in seconds
        max_interval: Maximum polling interval for backoff
        timeout: Maximum time to wait in seconds
        backoff: Backoff strategy - "constant", "linear", or "exponential"
        verbose: Print progress indicators every 10 polls

    Returns:
        The final status object when complete

    Raises:
        PollingTimeoutError: If polling times out
        PollingError: If the job fails
    """
    start_time = time.time()
    tries = 0
    current_interval = polling_interval

    while True:
        await asyncio.sleep(current_interval)
        tries += 1

        # Get current status
        status = await get_status_fn()

        # Check if complete
        if is_complete_fn(status):
            if verbose and tries > 1:
                logger.info(f"\nCompleted after {tries} checks")
            return status

        # Check if error
        if is_error_fn(status):
            error_msg = get_error_message_fn(status)
            logger.error(f"A job failed with error: {error_msg}")
            return status

        # Check timeout
        elapsed = time.time() - start_time
        if elapsed > timeout:
            error_msg = f"Polling timed out after {elapsed:.1f}s (timeout: {timeout}s)"
            logger.error(error_msg)
            return status

        # Print progress
        if verbose and tries % 10 == 0:
            logger.info(".")

        # Calculate next interval
        current_interval = _calculate_next_interval(current_interval, backoff, max_interval)
