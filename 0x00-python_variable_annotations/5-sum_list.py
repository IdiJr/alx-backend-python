#!/usr/bin/env python3
""" Outputs sum of all elements in input_list. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Description: accepts a list input_list of floats as argument and
    returns their sum as a float.
    Arguments: input_list: List[float]
    """
    return sum(input_list)
