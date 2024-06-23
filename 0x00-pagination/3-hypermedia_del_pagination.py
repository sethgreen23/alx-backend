#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return the appropriate page of the dataset"""
        self.indexed_dataset()
        if self.__indexed_dataset is not None:
            indexed_data = [row for row in self.__indexed_dataset.values()]
            self.__indexed_dataset = {i: indexed_data[i]
                                      for i in range(len(indexed_data))}
        assert index in self.__indexed_dataset

        # find the start index
        start_index = next((idx for idx,
                            _ in self.__indexed_dataset.items()
                            if idx >= index))
        if start_index + page_size not in self.__indexed_dataset:
            next_index = None
        else:
            next_index = start_index + page_size
        end_idx = next_index or len(self.__indexed_dataset)
        data = [self.__indexed_dataset[i] for i in range(start_index, end_idx)]
        page_size = len(data)
        return {
            'index': start_index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }
