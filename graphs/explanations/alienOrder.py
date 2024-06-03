# Alien Dictionary (Leetcode Premium)

def alienOrder(words: List[str]) -> str:

# This is the function definition for `alienOrder`. It takes a list of strings
# `words` as an input and returns a string.

    graph = {}
    indegree = {}

# These lines initialize two dictionaries `graph` and `indegree`. `graph` will
# store the adjacency list representation of the graph and `indegree` will store
# the indegree of each node.

    for word in words:
        for char in word:
            graph[char] = set()
            indegree[char] = 0

# These loops initialize `graph` and `indegree` for each character in `words`.

    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    indegree[char2] += 1
                break
        else:
            if len(word1) > len(word2):
                return ""

# These loops build the graph and update the indegree. If a character in `word1`
# is not the same as the corresponding character in `word2`, add an edge from
# the character in `word1` to the character in `word2` and increment the
# indegree of the character in `word2`. If `word1` is longer than `word2` and
# all the characters in `word2` are the same as the corresponding characters in
# `word1`, return an empty string because the input is invalid.

    queue = [char for char in indegree if indegree[char] == 0]
    order = []

# Initialize a queue with the characters that have an indegree of 0 and an empty
# list `order` to store the order of characters.

    while queue:
        char = queue.pop(0)
        order.append(char)
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

# While the queue is not empty, remove a character from the queue, add it to
# `order`, and decrease the indegree of its neighbors. If a neighbor's indegree
# becomes 0, add it to the queue. This is a topological sort.

    if len(order) != len(indegree):
        return ""

# If the length of `order` is not the same as the length of `indegree`, return
# an empty string because the graph has a cycle.

    return "".join(order)

# Return the order of characters as a string. This is the lexicographically
# smallest alien dictionary order that is possible given the words in the input.