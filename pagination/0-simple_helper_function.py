#!/usr/bin/env python3
"""module for pagination helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
