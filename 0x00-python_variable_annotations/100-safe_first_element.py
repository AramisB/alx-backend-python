#!/usr/bin/env python3
'''function safe_first_element'''


from typing import List, Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
