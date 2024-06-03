# Longest Palindromic Substring

def longestPalindrome(s: str) -> str:

# This line defines a function named `longestPalindrome` that takes a string `s`
# as input and returns a string.

    def expandAroundCenter(left, right):

# This line defines a nested function `expandAroundCenter` that takes two
# indices, `left` and `right`.

        while left >= 0 and right < len(s) and s[left] == s[right]:

# This line starts a while loop that continues as long as the `left` index is
# not negative, the `right` index is less than the length of the string `s`, and
# the characters at the `left` and `right` indices of `s` are the same.

            left -= 1
            right += 1

# These lines decrement the `left` index and increment the `right` index. This
# expands the potential palindrome around the center.

        return s[left + 1:right]

# This line returns the substring of `s` that starts from `left + 1` and ends at
# `right`. This is the longest palindrome that can be formed by expanding around
# the center.

    if len(s) < 2 or s == s[::-1]:
        return s

# This block checks if the length of `s` is less than 2 or if `s` is the same as
# its reverse. If either condition is true, it returns `s` because `s` is a
# palindrome itself.

    max_palindrome = ''

# This line initializes `max_palindrome` as an empty string. This variable will
# hold the longest palindrome found.

    for i in range(len(s) - 1):

# This line starts a for loop that iterates over the indices of `s`.

        palindrome1 = expandAroundCenter(i, i)
        palindrome2 = expandAroundCenter(i, i + 1)

# These lines call `expandAroundCenter` with two different sets of indices.
# `palindrome1` is the longest palindrome with `i` as the center, and
# `palindrome2` is the longest palindrome with the character between `i` and `i
# + 1` as the center.

        max_palindrome = max(palindrome1, palindrome2, max_palindrome, key=len)

# This line updates `max_palindrome` to be the longest of `palindrome1`,
# `palindrome2`, and the current `max_palindrome`.

    return max_palindrome

# This line returns the longest palindrome found in `s`.