# Combination Sum IV

def combinationSum4(nums: List[int], target: int) -> int:

# This line defines a function named `combinationSum4`. The function takes two
# parameters: `nums`, which is a list of integers, and `target`, which is an
# integer. The function is expected to return an integer.

    dp = [0] * (target + 1)

# This line initializes a list `dp` of length `target + 1`, filled with zeros.
# Each element in this list will eventually hold the number of combinations of
# `nums` that sum up to its index.

    dp[0] = 1

# This line sets the first element of `dp` to 1. This is because there is
# exactly one combination that sums up to 0, which is the empty combination.

    for i in range(1, target + 1):

# This line starts a for loop that iterates from 1 to `target`. For each
# iteration, the current number is stored in the `i` variable.

        for num in nums:

# This line starts a nested for loop that iterates over each number in `nums`.

            if i >= num:

# This line checks if `i` is greater than or equal to `num`. If it is, `num` can
# be used in a combination that sums up to `i`.

                dp[i] += dp[i - num]

#This line increments `dp[i]` by `dp[i - num]`. This is because each combination
#that sums up to `i - num` can be extended by `num` to form a combination that
#sums up to `i`.

    return dp[target]

# After the loops have finished, this line returns the last element in `dp`,
# which is the number of combinations of `nums` that sum up to `target`.

# This function essentially calculates the number of combinations of `nums` that
# can sum up to `target`, with repetitions allowed. It does this by using a
# dynamic programming approach, where the result for each number is calculated
# based on the results for smaller numbers.