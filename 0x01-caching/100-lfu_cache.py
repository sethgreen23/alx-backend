#!/usr/bin/python3
"""LFUCache Cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache caching system"""
    def __init__(self):
        """Init method"""
        super().__init__()
        self.__key_frequency_dict = {}
        self.__cache_frequency_list = {}

    def put(self, key, item):
        """Add item to the LFUCache cache"""
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
           and key not in self.cache_data):
            # add entery to the element
            # get the least frequent element and remove it
            for i in sorted(self.__cache_frequency_list.keys()):
                if self.__cache_frequency_list.get(i) is None or \
                   len(self.__cache_frequency_list[i]) == 0:
                    continue
                old = self.__cache_frequency_list[i].pop(0)
                del self.__key_frequency_dict[old]
                del self.cache_data[old]
                print(f'DISCARD: {old}')
                break
        if key not in self.cache_data:
            self.__key_frequency_dict[key] = 0
            if self.__cache_frequency_list.get(0) is None:
                self.__cache_frequency_list[0] = [key]
            else:
                self.__cache_frequency_list[0].append(key)
        if key in self.cache_data:
            self.__cache_frequency_list[
                self.__key_frequency_dict[key]].remove(key)
            self.__key_frequency_dict[key] += 1
            frequency = self.__key_frequency_dict[key]
            if self.__cache_frequency_list.get(frequency) is None:
                self.__cache_frequency_list[frequency] = [key]
            else:
                self.__cache_frequency_list[frequency].append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item from the LFUCache cache"""
        if key is None or key not in self.cache_data:
            return None
        self.__cache_frequency_list[
            self.__key_frequency_dict[key]].remove(key)
        self.__key_frequency_dict[key] += 1
        frequency = self.__key_frequency_dict[key]
        if self.__cache_frequency_list.get(frequency) is None:
            self.__cache_frequency_list[frequency] = [key]
        else:
            self.__cache_frequency_list[frequency].append(key)
        return self.cache_data.get(key)
