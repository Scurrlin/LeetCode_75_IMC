# Two Sum

def twoSum(self, nums: List[int], target: int) -> List[int]:

# This line defines a function named `twoSum`. The function takes three
# parameters: `self`, `nums`, and `target`. `self` is typically used in the
# context of class methods, but here it seems unnecessary as the function isn't
# part of a class. `nums` is expected to be a list of integers, and `target` is
# expected to be an integer. The function is expected to return a list of
# integers.

    nums_dict = {}

# This line initializes an empty dictionary `nums_dict`. This dictionary will be
# used to store the numbers from the `nums` list as keys and their indices as
# values.

    for i, num in enumerate(nums):

# This line starts a for loop that iterates over the `nums` list.
# `enumerate(nums)` returns a tuple containing the index and the value for each
# element in `nums`, which are unpacked into `i` and `num`, respectively.

        if target - num in nums_dict:

# This line checks if `target - num` is a key in `nums_dict`. If it is, this
# means that `num` and `target - num` are two numbers in `nums` that add up to
# `target`.

            return [nums_dict[target - num], i]

# If the above condition is true, the function returns a list containing the
# index of `target - num` (which is retrieved from `nums_dict`) and the current
# index `i`.

        nums_dict[num] = i

# If `target - num` is not in `nums_dict`, this line adds `num` to `nums_dict`
# with its value being the current index `i`. This is done so that it can be
# checked against in future iterations.

# If the function goes through the entire list without finding two numbers that
# add up to `target`, it will end without returning anything. This isn't
# explicitly handled in the code, but Python functions without a return
# statement implicitly return `None`.