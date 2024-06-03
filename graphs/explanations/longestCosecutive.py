# Longest Consecutive Sequence

def longestConsecutive(nums: List[int]) -> int:

# This is the function definition for `longestConsecutive`. It takes a list of
# integers `nums` as an input and returns an integer.

    nums_set = set(nums)

# This line converts the list `nums` into a set `nums_set`. This is done to
# allow for constant time complexity for checking the presence of an element.

    max_len = 0

# This line initializes `max_len` to 0. `max_len` is used to keep track of the
# maximum length of consecutive numbers.

    for num in nums_set:

# This line starts a loop that iterates over each number in `nums_set`.

        if num - 1 not in nums_set:

# This line checks if the number one less than the current number is not in
# `nums_set`. This is done to ensure that we only start counting consecutive
# numbers from the first number in the sequence.

            current_len = 1

# If `num - 1` is not in `nums_set`, this line initializes `current_len` to 1.
# `current_len` is used to keep track of the current length of consecutive
# numbers.

            while num + current_len in nums_set:
                current_len += 1

# This while loop increments `current_len` as long as the number `num +
# current_len` is in `nums_set`. This is done to count the length of consecutive
# numbers.

            max_len = max(max_len, current_len)

# This line updates `max_len` to be the maximum of `max_len` and `current_len`.
# This is done to keep track of the maximum length of consecutive numbers.

    return max_len

# This line returns `max_len`, which is the maximum length of consecutive
# numbers in `nums`.