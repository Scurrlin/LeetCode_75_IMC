# Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle element
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the target is not found in the array
    return -1

# Define the sorted array
arr = [2, 3, 4, 5, 8]
# Define the target value to search for
target = 5
# Call the binary_search() function with the array and target value as arguments
result_index = binary_search(arr, target)
# Check if the target value was found
if result_index != -1:
    print(f"Target value {target} found at index {result_index}.")
else:
    print("Target value not found.")

# Depth-First Search
    
def dfs_search(graph, start, target, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to keep track of visited vertices
    
    visited.add(start)  # Mark the current vertex as visited
    print(start)  # Print or process the current vertex
    
    # If the current vertex is the target, return True (target found)
    if start == target:
        return True
    
    # Recursively search all adjacent vertices that have not been visited yet
    for neighbor in graph[start]:
        if neighbor not in visited:
            # If the target is found in any of the recursive calls, return True
            if dfs_search(graph, neighbor, target, visited):
                return True
    
    # If the target is not found in any adjacent vertices, return False
    return False


# Define the graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# Define the starting vertex
start_vertex = 'A'
# Define the target value to search for
target_value = 'F'
# Call the dfs_search() function with the graph, starting vertex, and target
# value as arguments
result = dfs_search(graph, start_vertex, target_value)
# Print whether the target value was found or not
if result:
    print(f"Target value {target_value} found in the graph.")
else:
    print(f"Target value {target_value} not found in the graph.")

# Breadth-First Search

from collections import deque

def bfs_search(graph, start, target):
    visited = set()  # Initialize an empty set to keep track of visited vertices
    queue = deque([start])  # Initialize a queue with the starting vertex
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        print(vertex)  # Print or process the current vertex
        
        # If the current vertex is the target value, return True (target found)
        if vertex == target:
            return True
        
        visited.add(vertex)  # Mark the current vertex as visited
        
        # Enqueue all adjacent vertices of the current vertex that have not been
        # visited yet
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # If the target value is not found, return False
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_vertex = 'A'
target_value = 'F'
result = bfs_search(graph, start_vertex, target_value)
if result:
    print(f"Target value {target_value} found in the graph.")
else:
    print(f"Target value {target_value} not found in the graph.")
