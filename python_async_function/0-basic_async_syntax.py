#!/usr/bin/env python3
"""This module defines a coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay up to max_delay seconds, then return it."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
