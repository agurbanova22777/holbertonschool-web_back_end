#!/usr/bin/env python3
"""This module defines a coroutine that schedules tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn tasks and return delays in ascending completion order."""
    delays: List[float] = []
    tasks = [
        task_wait_random(max_delay)
        for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
