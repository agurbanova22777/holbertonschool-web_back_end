#!/usr/bin/env python3
"""Module for async comprehension collecting random numbers."""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers via async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random float values.
    """
    return [number async for number in async_generator()]
