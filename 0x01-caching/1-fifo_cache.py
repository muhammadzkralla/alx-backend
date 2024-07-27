#!/usr/bin/python3
""" 1-fifo_cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class to implement a FIFO caching system """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first item in the order list (FIFO)
            oldest_key = self.order.pop(0)
            # Remove the oldest item from the cache
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
