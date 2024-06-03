# Number of 1 Bits

def hammingWeight(n: int) -> int:

# This line defines a function named `hammingWeight`. The function takes one
# parameter, `n`, which is an integer. The function is expected to return an
# integer.

    count = 0

# This line initializes a variable `count` to 0. This variable will keep track
# of the number of 1 bits in `n`.

    while n:

# This line starts a while loop that continues as long as `n` is not 0. This
# loop will iterate over each bit of `n`.

        count += n & 1

# This line increments `count` by the result of `n & 1`. The expression `n & 1`
# performs a bitwise AND operation between `n` and 1, which results in 1 if the
# least significant bit of `n` is 1 and 0 otherwise. This effectively counts the
# least significant 1 bit of `n`.

        n >>= 1

# This line shifts `n` one bit to the right. This effectively removes the least
# significant bit of `n`.

    return count

# After the loop has finished, this line returns the count of 1 bits in `n`.

# This function essentially counts the number of 1 bits in the binary
# representation of `n`. It does this by repeatedly checking the least
# significant bit of `n` and then removing it.