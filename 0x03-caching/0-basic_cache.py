#!/usr/bin/python3
''' self descriptive code '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' self descriptive '''

    def put(self, key, item):
        ''' self descriptive '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' self descriptive '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
