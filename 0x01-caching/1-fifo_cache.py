#!/usr/bin/env python3
"""cache FIFO module"""


from base_caching import BaseCaching
from collections import deque, Counter


class FIFOCache(BaseCaching):
    """class for FIFO caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.counter = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if key not in self.cache_data:
                self.cache_data[key] = item
                self.counter += 1
                # print(self.counter)
            else:
                self.cache_data[key] = item

        if self.counter > self.MAX_ITEMS:
            my_dq = deque(self.cache_data.items())
            removed_item = my_dq.popleft()
            print(f"DISCARD: {removed_item[0]}")
            self.cache_data = dict(my_dq)
            self.counter -= 1

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
