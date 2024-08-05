#!/usr/bin/env python3
"""
Measure the execution time of wait_n
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    Args:
        n (int): the number of times to call wait_random
        max_delay (int): the maximum delay for wait_random
    Returns:
        float: average time per execution
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
