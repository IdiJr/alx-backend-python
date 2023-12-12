#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension executed 4 times in
parallel.
"""

import asyncio
from time import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Desription: A measure_runtime coroutine that executes
                    async_comprehension four times in
                    parallel using asyncio.gather.
    """
    first_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    next_time = asyncio.get_event_loop().time()

    total_runtime = next_time - first_time
    return total_runtime

# # Test the coroutine
# async def main():
#     return await measure_runtime()

# print(asyncio.run(main()))
