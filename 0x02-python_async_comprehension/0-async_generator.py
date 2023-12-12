#!/usr/bin/env python3
"""
Generates a random value between 0 and 10 every second, 10 times.
"""

import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Definition: A coroutine that takes no arguments, loop
                    10 times, each time asynchronously
                    wait 1 second, then yield a random number
                    between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random()
