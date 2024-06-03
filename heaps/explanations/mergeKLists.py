# Merge K Sorted Lists

import heapq

# This line imports the `heapq` module, which provides an implementation of the
# heap queue algorithm, also known as the priority queue algorithm.

from typing import List

# This line imports the `List` class from the `typing` module, which is used for
# type hinting.

class ListNode:

# This line defines a class named `ListNode`.

    def __init__(self, val=0, next=None):

# This line defines the constructor for the `ListNode` class. It takes two
# parameters: `val` and `next`. `val` is the value of the node, and `next` is a
# reference to the next node in the list.

        self.val = val
        self.next = next

# These lines assign the values of `val` and `next` to the instance variables
# `self.val` and `self.next`, respectively.

def mergeKLists(lists: List[ListNode]) -> ListNode:

# This line defines a function named `mergeKLists` that takes a list of
# `ListNode` objects and returns a `ListNode`.

    min_heap = []

# This line initializes an empty list named `min_heap`.

    for l in lists:

# This line starts a for loop that iterates over each `ListNode` in `lists`.

        while l:

# This line starts a while loop that continues as long as `l` is not `None`.

            heapq.heappush(min_heap, l.val)

# This line pushes the value of `l` onto `min_heap`. The `heapq.heappush()`
# function maintains the heap invariant.

            l = l.next

# This line moves to the next node in the list.

    dummy = ListNode(0)

# This line creates a new `ListNode` with a value of 0 and assigns it to
# `dummy`.

    current = dummy

# This line assigns `dummy` to `current`.

    while min_heap:

# This line starts a while loop that continues as long as `min_heap` is not
# empty.

        current.next = ListNode(heapq.heappop(min_heap))

# This line pops the smallest value from `min_heap`, creates a new `ListNode`
# with that value, and assigns it to `current.next`.

        current = current.next

# This line moves to the next node in the list.

    return dummy.next

# This line returns the merged list, which starts from the next node of `dummy`.
# The `dummy` node was used as a placeholder to easily start the merged list.