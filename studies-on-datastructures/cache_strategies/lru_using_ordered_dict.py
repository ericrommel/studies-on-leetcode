from collections import OrderedDict
from typing import TypeVar, Generic, Hashable, Optional

T = TypeVar('T')


class LRUCache(Generic[T]):
    def __init__(self, capacity: int):
        self.cache: OrderedDict[Hashable, T] = OrderedDict()
        self.capacity = capacity

    def get(self, key: Hashable) -> Optional[T]:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: Hashable, value: T) -> None:
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)

    def __len__(self) -> int:
        return len(self.cache)

    def clear(self) -> None:
        self.cache.clear()


# Running
# Build a new cache with capacity 2 (i.e. we can store at most two values at a time)
cache = LRUCache[str](capacity=2)

# Put two values in to the cache. Cache keys will now be [1, 2]
cache.put(1, "hello")
cache.put(2, "hello again")

# Length is 2 since that is the number of values in the cache
print(len(cache))  # Output: 2

# Can retrieve 1 since both 1 and 2 are in the cache. Cache keys are now [2, 1] since 2 was called more recently than 1
print(cache.get(2))  # Output: hello again

# This will evict key 1 with value "hello". Cache keys are now [3, 2]
cache.put(3, "goodbye")

# We now return None since 1 is no longer in the cache
print(cache.get(1))  # Output: None

# But we can get the cached value for 3. Cache keys are still [3, 2] since 3 was called more recently than 2
print(cache.get(3))  # Output: goodbye

# Cache keys are now [2, 3]
print(cache.get(2))  # Output: hello again

# This will drop key 3. Cache keys are now [1, 2]
cache.put(1, "I'm back!")

# Get None since 3 was dropped
print(cache.get(3))  # Output: None

# Finally we can clear the cache
cache.clear()
print(len(cache))  # Output: 0
