# -*- coding: utf-8 -*-
"""
snakehelpers: General-purpose Python 3 helper functions by Kenneth Sinder
(https://github.com/kennethsinder/snakehelpers)
"""

from typing import Any, Callable, Dict, Iterable, Optional, Union


def any_in(A: Iterable[Any], B: Iterable[Any]) -> bool:
    return any(a in B for a in A)


def first(L: Iterable[Any],
          criterion: Optional[Union[bool, Callable[[Any], bool]]],
          default: Optional[Any] = None,
          required: Optional[bool] = False) -> Any:
    if criterion is None:
        def pred(x): return True
    elif isinstance(criterion, bool):
        def pred(x): return criterion
    else:
        pred = criterion

    try:
        return next(x for x in L if pred(x))
    except StopIteration:
        if not required:
            return default
        raise

def filter_dict(mapping: Dict[Any, Any],
                keys: Iterable[Any]) -> Dict[Any, Any]:
    result = {}
    for key in keys:
        if key in mapping:
            result[key] = mapping[key]
    return result
