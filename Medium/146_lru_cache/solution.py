###################
### 146. LRU (Least Recently Used) Cache
### Design a data structure that follows the contraints of a 
### LRU Cache. Implement the LRUCache class:

### LRUCache(int capacity) - Initialize the LRU cache with 
### positive size capacity.

### int get(int key) - Return the value of the key if the key
### exists, otherwise return -1.

### void put(int key, int value) - Update the value of the key if
### the key exists. Otherwise, add the key-value par to the
### cache. If the number of keys exceeds the capacity from this
### operation, evict the least recently used key.

### The functions get and put must each run in 0(1) average time
### complexity. 
###################

######################### PROBLEM COVERS #########################
# LRU CACHE


# importing the library for OrderedDict
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # initializing capacity cache with positive size
        # don't need to assign default value, comes as input
        self.capacity = capacity
        # LRU cache: stores key-value pairs in order
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        # moving key to end to mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # remove first item (least recently used)
            self.cache.popitem(last=False)
        
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))

# # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)