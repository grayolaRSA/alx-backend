#!/usr/bin/env python3
"""cache LRU module"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """class for LIFO caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.access_hist = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                lru_key = next(iter(self.access_hist))
                del self.cache_data[lru_key]
                del self.access_hist[lru_key]
                print(f"DISCARD: {lru_key}")

        if key in self.cache_data:
            self.access_hist.pop(key)
            del self.cache_data[key]
        self.cache_data[key] = item
        self.access_hist[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
