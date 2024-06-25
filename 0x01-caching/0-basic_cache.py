#!/usr/bin/python3
""" Basic Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCaching class"""

    def put(self, key, item):
        """Add and item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get and item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
