# CONCEPTS COVERED

- LRU Cache

### Key:
- ❣️ Inner Concept
- 🦋 Example
- 👉 Comment
- ✅ Output

## LRU Cache
- LRU = Least Recently Used: way to remember things but only keep a limited number of them, and when it gets full, it forgets the one you haven't used in the longest time
- Think of it like a desk with limited space:
    - You put important papers (data) on desk
    - When desk is full and you want to add new paper, you remove the paper you haven't looked at in the longest time
    - The goal: keep the most recently used or important papers handy
- LRU function: 
    - Stores key-value pairs (e.g. a note and it's content)
    - Keeps track of which key used most recently
    - When capacity is exceeded, remove least recently used key
    - Provides two operations:
        - get(key): return value if key exists, and mark it 'recently used'. Else return -1
        - put(key, value): Add or update the value for the key. If capacity exceeded, remove least recently used.

    🦋 Minimal working example
    from collections import OrderedDict 

    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()

        def get(self, key):
            if key not in self.cache:
                return -1
            👉 Move key to end to show recently used
            self.cache.move_to_end(key)
            return self.cache[key]

        def put(self, key, value):
            if key in self.cache:
                👉 Update existing key and mark recently used
                self.cache.move_to_end(key)
            self.cache[key] = value
            👉 If over capacity, remove least recently used item (first one)
            if len(self.cache) > self.capacity:
                👉 .popitem(last=False) removed oldest from OrderedDict, which  keeps key insertion order
                self.cache.popitem(last=False)

        👉 Example Usage:
        cache = LRUCache(2) 👉 capacity = 2 (cache holds up to 2 items)

        cache.put(1, 1) 👉 cache: {1=1}
        cache.put(2, 2) 👉 cache: {1=1, 2=2}
        👉 Access key with get(), it becomes most recently used
        print(cache.get(1)) 👉 returns 1, cache order: {2=2, 1=1}
        👉 Adding key with put(), exceed capacity & least recent item is removed
        cache.put(3, 3) 👉 evicts key 2, cache: {1=1, 3=3}
        print(cache.get(2))   👉 returns -1 (not found)
        cache.put(4, 4)       👉 evicts key 1, cache: {3=3, 4=4}
        print(cache.get(1))   👉 returns -1 (not found)
        print(cache.get(3))   👉 returns 3
        print(cache.get(4))   👉 returns 4

