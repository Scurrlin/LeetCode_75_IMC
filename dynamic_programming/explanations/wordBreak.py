# Word Break Problem

def wordBreak(s: str, wordDict: List[str]) -> bool:

# This line defines a function named `wordBreak`. The function takes two
# parameters: `s`, which is a string, and `wordDict`, which is a list of
# strings. The function is expected to return a boolean.

    n = len(s)

# This line initializes a variable `n` to the length of `s`. This variable will
# be used to iterate over `s`.

    dp = [False] * (n + 1)

# This line initializes a list `dp` of length `n + 1`, filled with `False`. Each
# element in this list will eventually hold a boolean indicating whether the
# substring of `s` up to that index can be segmented into words in `wordDict`.

    dp[0] = True

# This line sets the first element of `dp` to `True`. This is because an empty
# string can be segmented into an empty list of words.

    for i in range(1, n + 1):

# This line starts a for loop that iterates from 1 to `n`. For each iteration,
# the current index is stored in the `i` variable.

        for word in wordDict:

# This line starts a nested for loop that iterates over each word in `wordDict`.

            if i >= len(word) and s[i - len(word):i] == word:

# This line checks if `i` is greater than or equal to the length of `word` and
# if the substring of `s` from `i - len(word)` to `i` is equal to `word`. If
# both conditions are true, `word` can be used to segment the substring of `s`
# up to `i`.

                dp[i] = dp[i] or dp[i - len(word)]

# This line sets `dp[i]` to `True` if `dp[i]` is `True` or if `dp[i -
# len(word)]` is `True`. This is because if the substring of `s` up to `i -
# len(word)` can be segmented into words in `wordDict`, then so can the
# substring of `s` up to `i` by adding `word`.

    return dp[n]

# After the loops have finished, this line returns the last element in `dp`,
# which is a boolean indicating whether `s` can be segmented into words in
# `wordDict`.

# This function essentially determines whether `s` can be segmented into a
# space-separated sequence of one or more dictionary words. It does this by
# using a dynamic programming approach, where the result for each substring is
# calculated based on the results for smaller substrings.