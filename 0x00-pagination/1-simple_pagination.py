#!/usr/bin/env python3
"""Server Class"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    """
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page=page, page_size=page_size)
        return self.dataset()[start:end]
