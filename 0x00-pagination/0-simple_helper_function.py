#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This Function Returns a tuple containing a start and end index."""
    return ((page - 1) * page_size, page * page_size)
