from collections import deque
import time

start = time.time()


# Define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# example graph as adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# graph = {
#     'A': ['B', 'C', 'D', 'E'],
#     'B': ['A', 'C', 'D', 'F'],
#     'C': ['A', 'B', 'D', 'E', 'F', 'G'],
#     'D': ['A', 'B', 'C', 'E', 'H'],
#     'E': ['A', 'C', 'D', 'F', 'H', 'I'],
#     'F': ['B', 'C', 'E', 'G', 'I', 'J'],
#     'G': ['C', 'F', 'H', 'J', 'K', 'L'],
#     'H': ['D', 'E', 'G', 'I', 'L'],
#     'I': ['E', 'F', 'H', 'J', 'L', 'M'],
#     'J': ['F', 'G', 'I', 'K', 'M', 'N'],
#     'K': ['G', 'J', 'L', 'N', 'O', 'P'],
#     'L': ['G', 'H', 'I', 'K', 'P'],
#     'M': ['I', 'J', 'N', 'Q'],
#     'N': ['J', 'K', 'M', 'O', 'Q', 'R'],
#     'O': ['K', 'N', 'P', 'R'],
#     'P': ['K', 'L', 'O', 'S'],
#     'Q': ['M', 'N', 'R', 'T'],
#     'R': ['N', 'O', 'Q', 'S', 'T', 'U'],
#     'S': ['P', 'R', 'U'],
#     'T': ['Q', 'R', 'U', 'V'],
#     'U': ['R', 'S', 'T', 'V'],
#     'V': ['T', 'U', 'W', 'X'],
#     'W': ['V', 'X', 'Y'],
#     'X': [],
#     'Y': [],
#     'Z': []
# }
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['M', 'N'],
    'G': ['O', 'P'],
    'H': ['Q', 'R'],
    'I': ['S', 'T'],
    'J': ['U', 'V'],
    'K': [],
    'L': ['W', 'X'],
    'M': [],
    'N': ['Y', 'Z'],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}

# start BFS from vertex 'A'
dfs(graph, 'A')

end = time.time()
print(end - start)
