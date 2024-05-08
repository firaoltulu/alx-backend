#!/usr/bin/env python3

""" BaseCaching module
"""
from base_caching import BaseCaching

"""Task 1."""
class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system."""

    def __init__(self):
        """this method Initialize the class with the parent's init method."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """this method Cache a key-value pair."""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """this method Return the value linked to a given key, or None."""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
