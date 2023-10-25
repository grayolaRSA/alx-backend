#!/usr/bin/env python3
"""cache MRU module"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """class for LRU caching system"""

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
                mru_key = next(reversed(self.access_hist))
                del self.cache_data[mru_key]
                del self.access_hist[mru_key]
                print(f"DISCARD: {mru_key}")

        if key in self.cache_data:
            self.access_hist.pop(key)
        self.cache_data[key] = item
        self.access_hist[key] = None

    def get(self, key):
        """ Get an item by key
        """
        # value = super().get(key)
        if key is None or key not in self.cache_data:
            return None

        if key in self.cache_data:
            self.access_hist.pop(key)
            self.access_hist[key] = None
        return self.cache_data[key]
