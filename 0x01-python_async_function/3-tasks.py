#!/usr/bin/env python3
"""
Returns asyncio.Task object
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Description: Takes an integer max_delay and returns a asyncio.Task.
    Arguments: max_delay: int.
    """
    return asyncio.create_task(wait_random(max_delay))
