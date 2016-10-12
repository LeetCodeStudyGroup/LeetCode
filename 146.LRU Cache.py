class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyset = []
        self.cache = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.keyset.remove(key)
            self.keyset.insert(0, key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.cache[key] = value
        if key in self.keyset:
            self.keyset.remove(key)
        self.keyset.insert(0, key)
        if len(self.cache) > self.capacity:
            del self.cache[self.keyset.pop(-1)]
        
