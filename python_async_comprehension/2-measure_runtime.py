#!/usr/bin/env python3
"""Module that measures runtime of async comprehensions in parallel."""
import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel and return runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start
