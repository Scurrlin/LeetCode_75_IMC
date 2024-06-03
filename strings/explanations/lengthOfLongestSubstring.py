# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s: str) -> int:

# This line defines a function named `lengthOfLongestSubstring` that takes a
# string `s` as input and returns an integer.

    char_map = {}

# This line initializes an empty dictionary `char_map`. This dictionary will be
# used to store the last occurrence of each character in the string.

    start = max_length = 0

# This line initializes two variables, `start` and `max_length`, to 0. `start`
# is used to keep track of the starting index of the current substring, and
# `max_length` is used to keep track of the length of the longest substring
# without repeating characters that we've seen so far.

    for end in range(len(s)):

# This line starts a loop that iterates over the string `s` using the index
# `end`.

        if s[end] in char_map:

# This line checks if the current character `s[end]` has been seen before by
# checking if it's in `char_map`.

            start = max(start, char_map[s[end]] + 1)

# If the current character has been seen before, this line updates `start` to be
# the maximum of the current `start` and one more than the index of the last
# occurrence of the current character. This is done to ensure that `start`
# always points to the start of the current substring without repeating
# characters.

        char_map[s[end]] = end

# This line updates `char_map` to store the current index `end` as the last
# occurrence of the current character.

        max_length = max(max_length, end - start + 1)

# This line updates `max_length` to be the maximum of the current `max_length`
# and the length of the current substring without repeating characters.

    return max_length

# Finally, this line returns `max_length`, which is the length of the longest
# substring without repeating characters.