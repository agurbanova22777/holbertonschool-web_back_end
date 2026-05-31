#!/usr/bin/env python3
"""This module measures average runtime for running wait_n concurrently."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure runtime for wait_n and return the average time per coroutine."""
    start: float = time.time()
    asyncio.run(
        wait_n(n, max_delay)
    )
    total_time: float = time.time() - start
    return total_time / n
