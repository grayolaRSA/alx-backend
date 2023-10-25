#!/usr/bin/env python3
"""cache LIFO module"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class for LIFO caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                last_key, _ = self.cache_data.popitem()
                # last_key = next(reversed(self.cache_data))
                # first_key = next(iter(self.cache_data))
                print(f"DISCARD: {last_key}")
                # del self.cache_data[last_key]

        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
