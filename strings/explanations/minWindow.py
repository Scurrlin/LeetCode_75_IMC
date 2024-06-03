# Minimum Window Substring

def minWindow(s: str, t: str) -> str:

# This line defines a function named `minWindow` that takes two strings, `s` and `t`, as input and returns a string.

    if not t or not s:
        return ""

# This block checks if either `s` or `t` is empty. If either is empty, the function returns an empty string.

    dict_t = Counter(t)

# This line creates a Counter object from string `t`. This will count the occurrence of each character in `t`.

    required = len(dict_t)

# This line sets `required` to the number of unique characters in `t`.

    l, r = 0, 0

# This line initializes two pointers, `l` and `r`, both at the start of the string `s`.

    formed = 0

# This line initializes `formed` to 0. `formed` is used to track the number of unique characters in the current window that match the characters in `t`.

    window_counts = {}

# This line initializes an empty dictionary `window_counts` to keep track of all the unique characters in the current window.

    ans = float("inf"), None, None

# This line initializes a tuple `ans` to store the minimum window details. It's initialized with infinity, None, None.

    while r < len(s):

# This line starts a while loop that continues as long as `r` is less than the length of string `s`.

        character = s[r]

# This line sets `character` to the character at the `r` index in `s`.

        window_counts[character] = window_counts.get(character, 0) + 1

# This line increments the count of `character` in the current window.

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

# This block checks if `character` is in `t` and its count matches in the window and in `t`. If so, it increments `formed`.

        while l <= r and formed == required:

# This line starts a nested while loop that continues as long as `l` is less than or equal to `r` and `formed` equals `required`.

            character = s[l]

# This line sets `character` to the character at the `l` index in `s`.

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

# This block checks if the size of the current window is less than the minimum found so far. If so, it updates `ans` with the new minimum window details.

            window_counts[character] -= 1

# This line decrements the count of `character` in the window.

            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

# This block checks if `character` is in `t` and its count in the window is less than in `t`. If so, it decrements `formed`.

            l += 1

# This line increments `l` by 1, moving the left pointer to the right.

        r += 1

# This line increments `r` by 1, moving the right pointer to the right.

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# This line returns an empty string if no window was found (i.e., if the first element of `ans` is still infinity). Otherwise, it returns the minimum window in `s` that contains all the characters in `t`.