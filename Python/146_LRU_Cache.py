from collections import OrderedDict # So that we can use an ordered dictionary

# Time: O(1), Space: O(capacity)
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        check = self.key_value.get(key, None)
        if check:
            self.key_value.move_to_end(key)
        self.key_value[]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            
cache = LRUCache(2)
cache.put(1, 1)