# Coin Change

def coinChange(coins: List[int], amount: int) -> int:

# This line defines a function named `coinChange`. The function takes two
# parameters: `coins`, which is a list of integers, and `amount`, which is an
# integer. The function is expected to return an integer.

    dp = [float('inf')] * (amount + 1)

# This line initializes a list `dp` of length `amount + 1`, filled with
# infinity. Each element in this list will eventually hold the minimum number of
# coins that sum up to its index.

    dp[0] = 0

# This line sets the first element of `dp` to 0. This is because there are zero
# coins that sum up to 0.

    for coin in coins:

# This line starts a for loop that iterates over each coin in `coins`.

        for i in range(coin, amount + 1):

# This line starts a nested for loop that iterates from `coin` to `amount`. For
# each iteration, the current amount is stored in the `i` variable.

            dp[i] = min(dp[i], dp[i - coin] + 1)

# This line updates `dp[i]` to the minimum of `dp[i]` and `dp[i - coin] + 1`.
# This is because the minimum number of coins that sum up to `i` is either the
# minimum number of coins that sum up to `i - coin` plus one coin, or a previous
# minimum.

    return dp[amount] if dp[amount] != float('inf') else -1

# After the loops have finished, this line returns `dp[amount]` if it is not
# infinity, otherwise it returns -1. This is because if `dp[amount]` is still
# infinity, there are no combinations of coins that sum up to `amount`.

# This function essentially calculates the minimum number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1. It does this by using a dynamic
# programming approach, where the result for each amount is calculated based on
# the results for smaller amounts.