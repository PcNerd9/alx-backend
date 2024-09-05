#!/usr/bin/env python3

""" contains a FIFOCACHE class
"""

from base import BaseCaching


class FIFOCache(BaseCaching):
    """
    uses the FIFO concept to implement the
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
                self.shift(0, index, key)
                self.array[0] = key
            else:
                last_data = self.array[self.MAX_ITEMS - 1]
                print("DISCARD: {}".format(last_data))
                del self.cache_data[last_data]
                self.shift(0, self.MAX_ITEMS - 1, key)
                self.array[0] = key

        else:
            if key in self.array:
                index = array.index(key)
                self.shift(self.pointer, index, key)
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
        return self.cache_data.get(key, None)

    def shift(self, start, end, key):
        for ind in range(end, start, -1):
            self.array[ind] = self.array[ind - 1]
