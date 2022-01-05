from collections import OrderedDict # So that we can use an ordered dictionary

# Time: O(1), Space: O(capacity)
# May also be done using Doubly Linked List
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            
cache = LRUCache(2)
cache.put(1, 1)