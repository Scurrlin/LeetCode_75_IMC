# House Robber

def rob(nums: List[int]) -> int:

# This line defines a function named `rob`. The function takes one parameter,
# `nums`, which is a list of integers. The function is expected to return an
# integer.

    if not nums:
        return 0

# This line checks if `nums` is empty. If it is, the function returns 0 because
# there are no houses to rob.

    if len(nums) == 1:
        return nums[0]

# This line checks if `nums` contains only one element. If it does, the function
# returns that element because there is only one house to rob.


    if len(nums) == 2:
        return max(nums[0], nums[1])

# This line checks if `nums` contains two elements. If it does, the function
# returns the maximum of those two elements because the robber can only rob one
# of the two houses.

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

# These lines initialize a dynamic programming array `dp` of the same length as
# `nums`, and set the first two elements to `nums[0]` and the maximum of
# `nums[0]` and `nums[1]`, respectively. `dp[i]` will eventually hold the
# maximum amount that can be robbed from the first `i + 1` houses.

    for i in range(2, len(nums)):

# This line starts a for loop that iterates from 2 to `len(nums) - 1`. For each
# iteration, the current index is stored in the `i` variable.

        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

# This line calculates the maximum amount that can be robbed from the first `i +
# 1` houses. The robber has two options: rob the current house and the maximum
# amount from the first `i - 1` houses, or the maximum amount from the first `i`
# houses. The maximum of these two options is chosen.

    return dp[-1]

# After the loop has finished, this line returns the last element in `dp`, which
# is the maximum amount that can be robbed from all the houses.

# This function essentially solves the House Robber problem, where a robber
# wants to rob houses along a street, but cannot rob two adjacent houses, and
# wants to maximize the total amount robbed. It does this by using a dynamic
# programming approach, where the maximum amount for each number of houses is
# calculated based on the maximum amounts for smaller numbers of houses.