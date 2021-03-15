#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function make_multiplier """

    def fn(num: float):
        return num * multiplier
    return fn
