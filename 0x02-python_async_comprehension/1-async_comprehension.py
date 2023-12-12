#!/usr/bin/env python3
"""
Return list of values yielded by async_generator.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Description: A coroutine called async_comprehension that takes no
                     arguments, collects 10 random numbers using an async
                     comprehensing over async_generator, then return the
                     10 random numbers.
    """
    return [value async for value in async_generator()]
