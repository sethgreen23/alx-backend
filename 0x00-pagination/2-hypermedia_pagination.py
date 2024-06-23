#!/usr/bin/env python3
"""Simple pagination module"""


import csv
import math
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        self.dataset()
        total_pages = ((len(self.__dataset) - 1 + page_size) // page_size)
        if page <= total_pages:
            start, end = index_range(page, page_size)
            return self.__dataset[start:end]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        total_pages = ((len(self.__dataset) - 1 + page_size) // page_size)

        metadata = {
            'page_size': 0 if page > total_pages else page_size,
            'page': page,
            'data': self.get_page(page, page_size),
        }

        if page >= total_pages:
            metadata['next_page'] = None
        else:
            metadata['next_page'] = page + 1

        if page <= 1:
            metadata['previeous_page'] = None
        else:
            metadata['previeous_page'] = page - 1

        metadata['total_pages'] = total_pages
        return metadata
