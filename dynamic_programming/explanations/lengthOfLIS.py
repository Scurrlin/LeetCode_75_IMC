# Longest Increasing Subsequence

def lengthOfLIS(nums: List[int]) -> int:

# This line defines a function named `lengthOfLIS`. The function takes one
# parameter, `nums`, which is a list of integers. The function is expected to
# return an integer.

    if not nums:
        return 0

# This line checks if `nums` is empty. If it is, the function returns 0 because
# there are no elements to form a sequence.

    dp = [1] * len(nums)

# This line initializes a list `dp` of the same length as `nums`, filled with
# 1s. Each element in this list will eventually hold the length of the longest
# increasing subsequence ending at its index.

    for i in range(1, len(nums)):

# This line starts a for loop that iterates from 1 to `len(nums) - 1`. For each
# iteration, the current index is stored in the `i` variable.

        for j in range(i):

# This line starts a nested for loop that iterates from 0 to `i - 1`. For each
# iteration, the current index is stored in the `j` variable.

            if nums[i] > nums[j]:

# This line checks if `nums[i]` is greater than `nums[j]`. If it is, `nums[i]`
# can extend the increasing subsequence ending at `nums[j]`.

                dp[i] = max(dp[i], dp[j] + 1)

# This line updates `dp[i]` to the maximum of `dp[i]` and `dp[j] + 1`. This is
# because the longest increasing subsequence ending at `nums[i]` is either the
# longest increasing subsequence ending at `nums[j]` extended by `nums[i]`, or a
# previous subsequence ending at `nums[i]`.


    return max(dp)

# After the loops have finished, this line returns the maximum element in `dp`,
# which is the length of the longest increasing subsequence in `nums`.

# This function essentially calculates the length of the longest increasing
# subsequence in `nums`. It does this by using a dynamic programming approach,
# where the result for each element is calculated based on the results for
# smaller elements.