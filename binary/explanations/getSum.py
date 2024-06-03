# Sum of Two Integers

def getSum(a: int, b: int) -> int:

# This line defines a function named `getSum`. The function takes two
# parameters: `a` and `b`, both of which are integers. The function is expected
# to return an integer.

    mask = 0xFFFFFFFF

# This line initializes a variable `mask` to `0xffffffff`, which is a 32-bit
# number with all bits set to 1. This mask is used to get the last 32 bits of a
# number.

    while b & mask:

# This line starts a while loop that continues as long as the bitwise AND of `b`
# and `mask` is not 0. This is equivalent to checking if `b` is not 0, but only
# considering the last 32 bits of `b`.

        a, b = a ^ b, (a & b) << 1

# This line performs the core logic of the function. It calculates the sum of
# `a` and `b` without carrying, which is `a ^ b`, and the carry, which is `(a &
# b) << 1`, and assigns these values to `a` and `b`, respectively. The carry is
# shifted left by 1 bit because it should be added to the next higher bit.

    return a & mask if b > mask else a | b

# This line returns the result. If `b` is greater than `mask`, it means there is
# a carry out of the last 32 bits, so the function returns `a & mask` to get the
# last 32 bits of `a`. Otherwise, it returns `a | b` to combine the sum without
# carrying and the carry.

# This function essentially implements binary addition without using the `+`
# operator. It uses bitwise operations to calculate the sum and carry, and
# repeats this process until there is no carry.