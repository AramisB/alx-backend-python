#!/usr/bin/env python3
"""
basic async syntax
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine named wait_random that waits
    for a random delay between 0 and max_delay (included and float
    value) seconds.
    args: max_delay (int, optional): The maximum delay
    Return: The float value of the random delay
    Use the random module.
    """
    return random.uniform(0, max_delay)
