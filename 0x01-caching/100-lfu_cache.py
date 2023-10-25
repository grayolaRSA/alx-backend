#!/usr/bin/env python3
"""cache LFU module"""


from base_caching import BaseCaching
from collections import OrderedDict, Counter, deque


class LFUCache(BaseCaching):
    """class for LFU caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.access_hist = OrderedDict()
        self.counter = Counter()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                min_count = min(self.counter.values())
                min_keys = [key for key, count in self.counter.items()
                            if count == min_count]
                print(min_keys)
                print(self.access_hist)
                print(len(min_keys))

                if len(min_keys) >= 2:
                    lru_keys = OrderedDict((key, value) for key,
                                           value in self.access_hist.items()
                                           if key in min_keys)
                    print(lru_keys)
                    rk = list(lru_keys)[0]
                    print(rk)
                    # lru_list = list(lru_keys)
                    # print(lru_list)
                    # rk = lru_list[0][0]
                    del self.cache_data[rk]
                    del self.access_hist[rk]
                    del self.counter[rk]
                    print(f"DISCARD: {rk}")
                else:
                    lfu_key = min_keys[0][0]
                    del self.cache_data[lfu_key]
                    del self.access_hist[lfu_key]
                    del self.counter[lfu_key]
                    print(f"DISCARD: {lfu_key}")

            if key in self.cache_data:
                self.access_hist.pop(key)

        self.cache_data[key] = item
        print("Added new item!")
        self.access_hist[key] = None

    def get(self, key):
        """ Get an item by key
        """

        if key is None or key not in self.cache_data:
            return None

        if key in self.cache_data:
            self.access_hist.pop(key)
            self.access_hist[key] = None
        self.counter[key] += 1
        return self.cache_data[key]
