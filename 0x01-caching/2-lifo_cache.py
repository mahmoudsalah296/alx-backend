#!/usr/bin/env python3
"""last-In First-Out caching module.
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """FIFOCache"""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return

        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data.keys()
        ):
            last_key, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
