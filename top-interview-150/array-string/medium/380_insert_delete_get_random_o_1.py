"""
Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.



Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
import random
import pytest
from typing import List
from collections import Counter


class RandomizedSet:

    def __init__(self):
        self.list_values: List[int] = []
        self.map_values = {}

    def insert(self, val: int) -> bool:
        if val in self.map_values:
            return False
        else:
            self.list_values.append(val)
            self.map_values[val] = len(self.list_values) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.map_values:
            return False

        idx_to_remove = self.map_values[val]
        last_element = self.list_values[-1]
        self.list_values[idx_to_remove] = last_element
        self.map_values[last_element] = idx_to_remove
        self.list_values.pop()
        del self.map_values[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.list_values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


@pytest.fixture
def randomized_set():
    return RandomizedSet()

def test_insert(randomized_set):
    assert randomized_set.insert(1) == True  # Insert 1, should return True
    assert randomized_set.insert(1) == False  # Insert 1 again, should return False (duplicate)
    assert randomized_set.insert(2) == True  # Insert 2, should return True

def test_remove(randomized_set):
    assert randomized_set.insert(1) == True
    assert randomized_set.insert(2) == True
    assert randomized_set.remove(1) == True  # Remove 1, should return True
    assert randomized_set.remove(1) == False  # Remove 1 again, should return False (already removed)
    assert randomized_set.remove(3) == False  # Remove non-existing value, should return False

def test_get_random(randomized_set):
    randomized_set.insert(1)
    randomized_set.insert(2)
    randomized_set.insert(3)

    random_values = [randomized_set.get_random() for _ in range(100)]
    count = Counter(random_values)

    # Since all values should have roughly equal probability, we check the counts
    assert count[1] > 0
    assert count[2] > 0
    assert count[3] > 0

def test_insert_and_remove(randomized_set):
    assert randomized_set.insert(1) == True
    assert randomized_set.insert(2) == True
    assert randomized_set.insert(3) == True

    assert randomized_set.remove(2) == True
    assert randomized_set.insert(4) == True
    assert randomized_set.remove(1) == True

    remaining_values = [randomized_set.get_random() for _ in range(100)]
    count = Counter(remaining_values)

    assert count[3] > 0  # 3 should still exist
    assert count[4] > 0  # 4 should still exist
    assert 1 not in count  # 1 was removed, should not exist
    assert 2 not in count  # 2 was removed, should not exist
