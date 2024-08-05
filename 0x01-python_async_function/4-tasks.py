#!/usr/bin/env python3
"""
tasks
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine wait_n
    args: n (int): the number of times
          max_delay (int): the maximum delay
    Spawn wait_random n times with the specified max_delay.
    Return: the list of all the delays (float values).
    """
    list_float = []
    for _ in range(n):
        list_float.append(await task_wait_random(max_delay))
    return sorted(list_float)
