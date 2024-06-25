#!/usr/bin/python3
"""Fifo Cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Init method"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """Add item to the Fifo cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old = self.cache_list.pop(0)
            del self.cache_data[old]
            print(f'DISCARD: {old}')
        self.cache_data[key] = item
        self.cache_list.append(key)

    def get(self, key):
        """Get item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_list.remove(key)
        self.cache_list.append(key)
        return self.cache_data.get(key)
