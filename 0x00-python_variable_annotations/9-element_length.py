#!/usr/bin/env python3
"""
Outputs list of tuples, one for each element, of which
consists of the element itself and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Description: Add annotations to the below function’s parameters and
                 return values with the appropriate types
    Parameters: lst: Iterable[Sequence]
    """
    return [(i, len(i)) for i in lst]
