# Reverse Bits

def reverseBits(n: int) -> int:

# This line defines a function named `reverseBits`. The function takes one
# parameter, `n`, which is an integer. The function is expected to return an
# integer.

    res = 0

# This line initializes a variable `res` to 0. This variable will hold the
# result, which is the binary representation of `n` reversed.

    for i in range(32):

# This line starts a for loop that iterates 32 times. This is because the
# function is reversing a 32-bit integer.

        res <<= 1

# This line shifts `res` one bit to the left. This effectively multiplies `res`
# by 2 and makes room for the next bit.

        res |= n & 1

# This line performs a bitwise OR operation between `res` and the least
# significant bit of `n`, and assigns the result to `res`. This effectively adds
# the least significant bit of `n` to `res`.

        n >>= 1

# This line shifts `n` one bit to the right. This effectively divides `n` by 2
# and removes the least significant bit.

    return res

# After the loop has finished, this line returns `res`, which is the binary
# representation of `n` reversed.

# This function essentially reverses the binary representation of `n`. It does
# this by repeatedly taking the least significant bit of `n` and adding it to
# `res`, and then removing the least significant bit of `n`.