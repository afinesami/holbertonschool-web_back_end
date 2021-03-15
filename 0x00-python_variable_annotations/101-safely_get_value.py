#!/usr/bin/env python3
'''More involved type annotations'''
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    ''' Function safely_get_value '''
    if key in dct:
        return dct[key]
    else:
        return default
