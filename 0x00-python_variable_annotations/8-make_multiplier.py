#!/usr/bin/env python3
""" Outputs function that multiplies float by `multiplier`. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """" Description: Accepts a float multiplier as argument and returns a
    function that multiplies a float by multiplier
    Parameters: multiplier: float
    """
    return lambda x: x * multiplier
