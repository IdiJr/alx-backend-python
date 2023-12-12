#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension executed 4 times in
parallel.
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Desription: A measure_runtime coroutine that executes
                    async_comprehension four times in
                    parallel using asyncio.gather.
    """
    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - first_time
