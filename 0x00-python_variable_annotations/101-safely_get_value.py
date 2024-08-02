#!/usr/bin/env python3
'''function safely_get_value'''


from typing import Any, Mapping, Union, TypeVar


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Any = None) -> Union[Any, None]:
    """
    A type-annotated function safely_get_value that takes
    a dictionary dct, an index key and a default value default
    and returns the value stored in the dictionary
    at the index key or the default value if the key doesn’t exist
    """
    if key in dct:
        return dct[key]
    else:
        return default
