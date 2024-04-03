#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic cahe class"""

    def __init__(self):
        # use parent attribute
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
