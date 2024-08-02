#!/usr/bin/env python3
'''function element_length'''


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Annotate the function’s parameters and return values
    with the appropriate types
    """
    return [(i, len(i)) for i in lst]
