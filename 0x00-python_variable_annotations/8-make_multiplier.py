#!/usr/bin/env python3
'''function make_multiplier'''


from typing import Callable


def make_multiplier(mult: float) -> Callable[[float], float]:
    """
    A type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    """
    def multiplier(n: float) -> float:
        """
        A type-annotated function multiplier
        """
        return n * mult
    return multiplier
