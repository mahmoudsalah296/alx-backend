#!/usr/bin/env python3
"""First-In First-Out caching module.
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    First-In First-Out caching
    """

    def __init__(self):
        """Initializes the cache."""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            pass
        else:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: ", first_key)

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
