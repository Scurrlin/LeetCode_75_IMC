# Dijkstra's Algorithm

import heapq

def dijkstra(graph, start):
    # Initialize a dictionary to store the shortest distances from the start
    # vertex to all other vertices
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # The distance from start vertex to itself is 0
    
    # Initialize a priority queue (min heap) to store vertices and their
    # distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Ignore vertices that have already been visited
        if current_distance > distances[current_vertex]:
            continue
        
        # Visit each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the updated distance and vertex to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Define the graph represented as an adjacency list with weighted edges
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}
# Define the starting vertex
start_vertex = 'A'
# Call the dijkstra() function with the graph and starting vertex as arguments
distances = dijkstra(graph, start_vertex)
# Print the shortest distances from the starting vertex to all other vertices
print("Shortest distances from vertex", start_vertex)
print(distances)

# Bellman-Ford's Algorithm

def bellman_ford(graph, start):
    # Step 1: Initialize distances from start to all other vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Distance from start to itself is 0
    
    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    
    # Step 3: Check for negative-weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")
    
    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}
start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)
print("Shortest distances from vertex", start_vertex)
print(distances)

# Depth-First Search

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to keep track of visited vertices
    
    visited.add(start)  # Mark the current vertex as visited
    print(start)  # Print or process the current vertex
    
    # Recursively visit all adjacent vertices that have not been visited yet
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Define the graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_vertex = 'A'
# Call the dfs() function with the graph and the starting vertex as arguments
dfs(graph, start_vertex)

# Breadth-First Search

from collections import deque

def bfs(graph, start):
    visited = set()  # Initialize an empty set to keep track of visited vertices
    queue = deque([start])  # Initialize a queue with the starting vertex
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        visited.add(vertex)  # Mark the current vertex as visited
        print(vertex)  # Print or process the current vertex
        
        # Enqueue all adjacent vertices of the current vertex that have not been
        # visited yet
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_vertex = 'A'
bfs(graph, start_vertex)
