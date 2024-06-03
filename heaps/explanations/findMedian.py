# Find Median from Data Stream

import heapq

# This line imports the `heapq` module, which provides an implementation of the
# heap queue algorithm, also known as the priority queue algorithm.

from typing import List

# This line imports the `List` class from the `typing` module, which is used for
# type hinting.

class MedianFinder:

# This line defines a class named `MedianFinder`.

    def __init__(self):

# This line defines the constructor of the `MedianFinder` class.

        self.small = []  # Max heap
        self.large = []  # Min heap

# These lines initialize two empty lists: `small` (a max heap for the smaller
# half of the numbers) and `large` (a min heap for the larger half of the
# numbers).

    def addNum(self, num: int) -> None:

# This line defines a method named `addNum` that takes an integer `num` as a
# parameter and returns nothing.

        heapq.heappush(self.small, -num)

# This line pushes the negative of `num` onto the `small` heap. The negative
# sign is used to implement a max heap using Python's `heapq` module, which only
# provides a min heap.

        if (self.small and self.large and
            (-self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

# These lines check if both heaps are non-empty and if the maximum element of
# `small` is greater than the minimum element of `large`. If so, they pop the
# maximum element from `small`, negate it to get the original number, and push
# it onto `large`.

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

# These lines check if `small` has more than one element than `large`. If so,
# they pop the maximum element from `small`, negate it to get the original
# number, and push it onto `large`.

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

# These lines check if `large` has more elements than `small`. If so, they pop
# the minimum element from `large` and push its negative onto `small`.

    def findMedian(self) -> float:

# This line defines a method named `findMedian` that returns a float.

        if len(self.small) > len(self.large):
            return -self.small[0]

# This line checks if `small` has more elements than `large`. If so, it returns
# the negative of the maximum element of `small` (which is the median).

        return (-self.small[0] + self.large[0]) / 2

# This line is executed if `small` and `large` have the same number of elements.
# It returns the average of the maximum element of `small` and the minimum
# element of `large` (which is the median).