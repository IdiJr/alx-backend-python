#!/usr/bin/env python3
""" Takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Description: Spawns wait_random n times with the specified max_delay.
                     Returns the list of all the delays(float values) in
                     ascending order without using sort()
                     because of concurrency.
    Arguments: n: int, max_delay: int = 10
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
