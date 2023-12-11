#!/usr/bin/env python3
"""
Return execution time for wait_n given `n` and `max_delay`.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Description: Create a measure_time function with integers n and
                 max_delay as arguments that measures the total execution
                 time for wait_n(n, max_delay), and returns total_time / n.
                 Your function should return a float.
    Arguments: n: int, max_delay: int
    """
    start_time = time.time()
    delays = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_time = elapsed_time / n
    return average_time
