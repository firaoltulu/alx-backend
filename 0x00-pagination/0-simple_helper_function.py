#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This Function Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
