# Missing Number

def missingNumber(nums: List[int]) -> int:

# This line defines a function named `missingNumber`. The function takes one
# parameter, `nums`, which is a list of integers. The function is expected to
# return an integer.

    expected_sum = len(nums) * (len(nums) + 1) // 2

# This line calculates the expected sum of the numbers from 0 to `len(nums)`.
# The formula `n * (n + 1) // 2` is used to calculate the sum of the first `n`
# natural numbers.

    actual_sum = sum(nums)

# This line calculates the actual sum of the numbers in `nums`.

    return expected_sum - actual_sum

# This line returns the difference between the expected sum and the actual sum.
# This difference is the number that is missing from `nums`.

# This function essentially finds the missing number in an array containing `n`
# distinct numbers taken from 0, 1, 2, ..., n. It does this by comparing the
# expected sum of the numbers from 0 to `n` with the actual sum of the numbers
# in the array. The missing number is the difference between these two sums.