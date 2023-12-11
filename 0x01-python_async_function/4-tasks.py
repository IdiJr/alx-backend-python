#!/usr/bin/env python3
"""
Execute task_wait_random and returns sorted list of delay
"""

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[asyncio.Task]:
    """ Description: Take the code from wait_n and alter it into a new function
                 task_wait_n. The code is nearly identical to wait_n except
                 task_wait_random is being called.
    Arguments: n: int, max_delay: int = 10
    """
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    )
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
