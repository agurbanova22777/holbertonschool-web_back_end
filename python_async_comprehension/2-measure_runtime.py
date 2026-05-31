#!/usr/bin/env python3
"""This module measures the runtime of async comprehensions run in parallel."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and return runtime."""
    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start
