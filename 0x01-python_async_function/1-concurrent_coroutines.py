#!/usr/bin/env python3
"""
concurrent coroutines
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine wait_n
    args: n (int): the number of times
          max_delay (int): the maximum delay
    Spawn wait_random n times with the specified max_delay.
    Return: the list of all the delays (float values).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]