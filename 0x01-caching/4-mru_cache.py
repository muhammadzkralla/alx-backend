#!/usr/bin/python3
""" 4-mru_cache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing item
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (last item in the dictionary)
            discarded_key = next(reversed(self.cache_data))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Return the value and mark the item as most
        #  recently used by re-inserting it
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
