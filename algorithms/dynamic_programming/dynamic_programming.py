# Fibonacci Sequence

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

# Calculate the Fibonacci number for position 10
result = fibonacci(10)
print("Fibonacci number at position 10:", result)

# Knapsack Problem

def knapsack(weights, values, capacity):
    n = len(weights)
    memo = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                memo[i][w] = max(memo[i - 1][w], values[i - 1] + memo[i - 1][w - weights[i - 1]])
            else:
                memo[i][w] = memo[i - 1][w]

    return memo[n][capacity]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value = knapsack(weights, values, capacity)
print("Maximum value that can be achieved with capacity 5:", max_value)

# Longest Common Subsequence (LCS)

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    # Initialize a memoization table with zeros
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the memoization table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    # Backtrack to construct the longest common subsequence
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif memo[i - 1][j] > memo[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

s1 = "ABCDGH"
s2 = "AEDFHR"
lcs = longest_common_subsequence(s1, s2)
print("Longest Common Subsequence:", lcs)

# Shortest Path Problem (Dijkstra's Variant)

import heapq

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Distance from start vertex to itself is 0
    # Initialize priority queue with the start vertex and its distance
    pq = [(0, start)]
    
    while pq:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If the current distance to the current vertex is greater than the
        # known distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Iterate through neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If the calculated distance is shorter than the known distance,
            # update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the updated distance and neighbor to the priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Define the graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
# Define the starting vertex
start_vertex = 'A'
# Call the dijkstra() function with the graph and the starting vertex as
# arguments
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex, ":")
for vertex, distance in shortest_distances.items():
    print("To vertex", vertex, ":", distance)
