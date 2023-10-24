#!/usr/bin/python3
""" BasicCaching module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
