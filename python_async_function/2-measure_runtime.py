#!/usr/bin/env python3
"""This module measures the average runtime of running wait_n concurrently."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure runtime for wait_n(n, max_delay) and return the average per task."""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start
    return total_time / n
