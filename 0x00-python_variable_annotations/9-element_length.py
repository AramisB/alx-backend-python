#!/usr/bin/env python3
'''function element_length'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the function’s parameters and return values
    with the appropriate types
    """
    return [(i, len(i)) for i in lst]
