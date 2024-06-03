# Product of Array Except Self

def productExceptSelf(self, nums: List[int]) -> List[int]:

# This line defines a function named `productExceptSelf`. The function takes two
# parameters: `self` and `nums`. `self` is typically used in the context of
# class methods, but here it seems unnecessary as the function isn't part of a
# class. `nums` is expected to be a list of integers. The function is expected
# to return a list of integers.

    n = len(nums)

# This line initializes a variable `n` to the length of `nums`. This will be
# used to iterate over `nums`.

    left_products = [1 for _ in nums]

# This line initializes a list `left_products` with the same length as `nums`,
# with all elements set to 1. This list will be used to store the product of all
# numbers to the left of each number in `nums`.

    right_products = [1 for _ in nums]

# This line initializes a list `right_products` with the same length as `nums`,
# with all elements set to 1. This list will be used to store the product of all
# numbers to the right of each number in `nums`.

    for i in range(1, n):

# This line starts a for loop that iterates from 1 to `n - 1`. For each
# iteration, the current index is stored in the `i` variable.

        left_products[i] = left_products[i - 1] * nums[i - 1]

# This line updates the `i`-th element of `left_products` to the product of the
# `(i - 1)`-th element of `left_products` and the `(i - 1)`-th element of
# `nums`. This effectively calculates the product of all numbers to the left of
# the `i`-th number in `nums`.

    for i in range(n - 2, -1, -1):

# This line starts a for loop that iterates from `n - 2` to 0 in reverse order.
# For each iteration, the current index is stored in the `i` variable.

        right_products[i] = right_products[i + 1] * nums[i + 1]

# This line updates the `i`-th element of `right_products` to the product of the
# `(i + 1)`-th element of `right_products` and the `(i + 1)`-th element of
# `nums`. This effectively calculates the product of all numbers to the right of
# the `i`-th number in `nums`.

    return [left_products[i] * right_products[i] for i in range(n)]

# This line returns a list where the `i`-th element is the product of the `i`-th
# elements of `left_products` and `right_products`. This effectively calculates
# the product of all numbers in `nums` except for the `i`-th number.