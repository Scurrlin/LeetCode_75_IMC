# Climbing Stairs

def climbStairs(n: int) -> int:

# This line defines a function named `climbStairs`. The function takes one
# parameter, `n`, which is an integer. The function is expected to return an
# integer.

    if n == 1:
        return 1

# This line checks if `n` is equal to 1. If it is, the function returns 1
# because there is only one way to climb one stair.

    first, second = 1, 2

# This line initializes two variables, `first` and `second`, to 1 and 2
# respectively. These variables represent the number of ways to climb to the
# first and second stair.

    for i in range(3, n + 1):

# This line starts a for loop that iterates from 3 to `n`. For each iteration,
# the current stair is stored in the `i` variable.

        third = first + second

# This line calculates the number of ways to climb to the `i`-th stair, which is
# the sum of the number of ways to climb to the `(i - 1)`-th stair and the `(i -
# 2)`-th stair. This is because you can reach the `i`-th stair by climbing one
# stair from the `(i - 1)`-th stair or two stairs from the `(i - 2)`-th stair.

        first, second = second, third

# This line updates `first` and `second` to `second` and `third` respectively.
# This is because for the next iteration, the `(i - 1)`-th stair will be the `(i
# - 2)`-th stair and the `i`-th stair will be the `(i - 1)`-th stair.

    return second

# After the loop has finished, this line returns `second`, which is the number
# of ways to climb to the `n`-th stair.

# This function essentially calculates the number of distinct ways you can climb
# to the top of a staircase of `n` stairs. It does this by using a dynamic
# programming approach, where the result for each stair is calculated based on
# the results for the previous two stairs.