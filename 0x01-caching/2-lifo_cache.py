#!/usr/bin/env python3

""" contains a L    LIFOCACHE class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    uses the LIFO concept to implement the
    caching system
    """
    array = []

    def __init__(self):
        super().__init__()
        self.pointer = self.MAX_ITEMS - 1
        for i in range(self.MAX_ITEMS):
            self.array.append(None)

    def put(self, key, item):
        """
        add an item to the cache
        """
        if key is None or item is None:
            return
        if self.pointer == -1:
            if key in self.array:
                index = self.array.index(key)
                self.shift(0, index)
                self.array[0] = key
            else:
                last_in = self.array[0]
                print("DISCARD: {}".format(last_in))
                del self.cache_data[last_in]
                self.array[0] = key

        else:
            if key in self.array:
                index = array.index(key)
                self.shift(self.pointer, index)
                self.array[self.pointer + 1] = key
            else:
                self.array[self.pointer] = key
            self.pointer -= 1
        self.cache_data[key] = item

    def get(self, key):
        """
        get an item from the cache
        """
        if key is None:
            return
        return self.cache_data(key, None)

    def shift(self, start, end):
        for ind in range(end, start, -1):
            self.array[ind] = self.array[ind - 1]
