#!/usr/bin/python3
"""Fifo Cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Init method"""
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """Add item to the Fifo cache"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           key not in self.cache_data):
            old = self.__queue.pop()
            del self.cache_data[old]
            print(f'DISCARD: {old}')
        self.__queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
