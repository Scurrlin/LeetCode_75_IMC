# Palindromic Substrings

def countSubstrings(s: str) -> int:

# This line defines a function named `countSubstrings` that takes a string `s`
# as input and returns an integer.

    def expandAroundCenter(left, right):

# This line defines a nested function `expandAroundCenter` that takes two
# indices `left` and `right` as input.

        count = 0

# This line initializes a variable `count` to 0. This variable will keep track
# of the number of palindromic substrings.

        while left >= 0 and right < len(s) and s[left] == s[right]:

# This line starts a while loop that continues as long as the `left` index is
# greater than or equal to 0, the `right` index is less than the length of the
# string `s`, and the characters at the `left` and `right` indices of `s` are
# the same.

            left -= 1
            right += 1

# These lines decrement the `left` index and increment the `right` index. This
# expands the potential palindrome substring around the center.

            count += 1

# This line increments the `count` by 1 for each palindromic substring found.

        return count

# This line returns the count of palindromic substrings found by the
# `expandAroundCenter` function.

    total = 0

# This line initializes a variable `total` to 0. This variable will keep track
# of the total number of palindromic substrings in `s`.

    for i in range(len(s)):

# This line starts a for loop that iterates over each character in the string
# `s`.

        total += expandAroundCenter(i, i)

# This line calls the `expandAroundCenter` function with `i` as both the `left`
# and `right` indices. This checks for palindromic substrings of odd length and
# adds the count to `total`.

        total += expandAroundCenter(i, i + 1)

# This line calls the `expandAroundCenter` function with `i` as the `left` index
# and `i + 1` as the `right` index. This checks for palindromic substrings of
# even length and adds the count to `total`.

    return total

# This line returns the total count of palindromic substrings in `s`.