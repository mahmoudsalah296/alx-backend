#!/usr/bin/env python3
"""simple helper function"""


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    """
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)
