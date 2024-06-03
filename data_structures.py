# Arrays

# Aa array is a collection of elements stored at contiguous memory locations.
# Arrays allow random access to elements using an index.

# Python array creation
arr = [1, 2, 3, 4, 5]

# Linked Lists

# A linked list is a inear data structure where elements are not stored in
# contiguous memory locations. Each element(node) points to the next element in
# the list.

# Python linked list node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Example of creating a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Stacks

# A stack is a "last in, first out" (LIFO) data structure. Elements are aded and
# removed from the same end, called the top.

# Python stack implementation using a list
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns 2

# Queues

# A queue is a "first in, first out" (FIFO) data structure. Elements are added
# at the rear and removed from the front.

# Python queue implementation using collections.deque
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Removes and returns 1

# Hash Tables

# A hash table is a data structure that implements an associative array abstract
# data type and can map keys to values. It uses a hash function to compute an
# index into an array of buckets or slots, from which the desired value can be
# found.

# Python dictionary is a built-in implementation of a hash table
hash_table = {}
hash_table["key"] = "value"