# Counting Bits

def countBits(n: int) -> List[int]:

# This line defines a function named `countBits`. The function takes one
# parameter, `n`, which is an integer. The function is expected to return a list
# of integers.

    res = [0] * (n + 1)

# This line initializes a list `res` of length `n + 1`, filled with zeros. Each
# element in this list will eventually hold the number of 1 bits in the binary
# representation of its index.

    for i in range(1, n + 1):

# This line starts a for loop that iterates from 1 to `n`. For each iteration,
# the current number is stored in the `i` variable.

        res[i] = res[i & (i - 1)] + 1
    
# This line calculates the number of 1 bits in `i`. The expression `i & (i - 1)`
# clears the least significant 1 bit in `i`, so `res[i & (i - 1)]` is the number
# of 1 bits in `i` without the least significant 1 bit. Adding 1 to this gives
# the number of 1 bits in `i`.

    return res

# After the loop has finished, this line returns the list `res`. The element at
# index `i` in `res` is the number of 1 bits in the binary representation of
# `i`.

# This function essentially calculates the number of 1 bits in the binary
# representation of each number from 0 to `n`. It does this by using a dynamic
# programming approach, where the result for each number is calculated based on
# the result for a smaller number.