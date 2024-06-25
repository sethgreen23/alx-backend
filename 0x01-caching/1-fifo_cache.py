#!/usr/bin/python3
"""Fifo Cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """Init method"""
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """Add item to the Fifo cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old = self.__queue.pop(0)
                del self.cache_data[old]
                print(f'DISCARD: {old}')
            self.__queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache"""
        return self.cache_data.get(key)
