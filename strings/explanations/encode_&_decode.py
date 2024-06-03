# Encode and Decode Strings (Leetcode Premium)

class Codec:

# This line defines a new class named `Codec`.

    def encode(self, strs: List[str]) -> str:

# This line defines a method named `encode` that takes a list of strings
# (`strs`) as input and returns a string.

        return ''.join(f'{len(s)}#{s}' for s in strs)

# This line encodes the list of strings into a single string. For each string
# `s` in the list `strs`, it creates a new string that starts with the length of
# `s`, followed by a `#`, and then `s` itself. It then joins all these strings
# together into one string.

    def decode(self, s: str) -> List[str]:

# This line defines a method named `decode` that takes a string (`s`) as input
# and returns a list of strings.

        strs, i = [], 0

# This line initializes an empty list `strs` and a counter `i` set to 0.

        while i < len(s):

# This line starts a while loop that continues as long as `i` is less than the
# length of the input string `s`.

            j = s.find('#', i)
# This line finds the position of the next `#` in the string `s`, starting from
# position `i`, and assigns it to `j`.

            i = j + 1 + int(s[i:j])

# This line extracts the number before the `#` (which represents the length of
# the next string), converts it to an integer, adds `j + 1` to it, and assigns
# the result to `i`.

            strs.append(s[j + 1:i])

# This line extracts the string of length `s[i:j]` from `s`, starting from
# position `j + 1`, and appends it to the list `strs`.

        return strs
    
# This line returns the list of decoded strings `strs`.