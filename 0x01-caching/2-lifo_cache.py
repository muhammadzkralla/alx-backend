#!/usr/bin/python3
""" 2-lifo_cache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.stack.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
