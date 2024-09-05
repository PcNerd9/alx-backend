#!/usr/bin/env python3

"""
contains a basiccache class
"""

from base import BaseCaching


class BasicCache(BaseCaching):
    """
    A simple implementation of a caching system
    """
    def __init__(self):
        """
        initialize the super class init method
        """
        super().__init__()

    def put(self, key, item):
        """
        save a new item into the cache using the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in the cache if present
        otherwise return None
        """
        if key is None:
            return

        return self.cache_data.get(key, None)
