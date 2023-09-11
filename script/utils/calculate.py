from typing import List, Tuple, Union
from math import sqrt, inf


def calculate_length(pos1, pos2):
    """calculate position1 to position2 length"""
    return sqrt(pow(pos2[0] - pos1[0], 2) + pow(pos2[1] - pos1[1], 2))


def calculate_shortest_position(position: Tuple[Union[int, float], Union[int, float]],
                                positions: List[Tuple]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    :param position:
    :param positions:
    :return: shortest position
    """
    shortest = inf
    pos = (-1, -1)
    for p in positions:
        temp = calculate_length(position, p)
        if temp < shortest:
            shortest = temp
            pos = p
    return pos


def calculate_angle(pos1, pos2):
    pass
