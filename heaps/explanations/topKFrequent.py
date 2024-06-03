# Top K Frequent Elements

import heapq

# This line imports the `heapq` module, which provides an implementation of the
# heap queue algorithm, also known as the priority queue algorithm.

from typing import List

# This line imports the `List` class from the `typing` module, which is used for
# type hinting.

def topKFrequent(nums: List[int], k: int) -> List[int]:

# This line defines a function named `topKFrequent` that takes two parameters:
# `nums` (a list of integers) and `k` (an integer), and returns a list of
# integers.

    freq_dict = {}

# This line initializes an empty dictionary `freq_dict` which will be used to
# store the frequency of each number in `nums`.

    for num in nums:

# This line starts a for loop that iterates over each number in the `nums` list.

        if num in freq_dict:
            freq_dict[num] += 1

# If the current number `num` is already a key in the `freq_dict` dictionary,
# its value (frequency) is incremented by 1.

        else:
            freq_dict[num] = 1

# If the current number `num` is not in the `freq_dict` dictionary, it is added
# as a new key with a value (frequency) of 1.

    return heapq.nlargest(k, freq_dict.keys(), key=freq_dict.get)

# This line uses the `heapq.nlargest` function to return the `k` keys (numbers)
# from `freq_dict` with the highest values (frequencies). The
# `key=freq_dict.get` argument tells `heapq.nlargest` to use the values in
# `freq_dict` for comparison.