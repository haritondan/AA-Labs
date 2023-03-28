from collections import deque

import time
start = time.time()

def bfs(graph, start):
    # initialize the queue and visited set
    queue = deque([start])
    visited = set([start])

    while queue:
        # dequeue a vertex from the queue
        vertex = queue.popleft()
        print(vertex)

        # enqueue all unvisited neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# example graph as adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'F'],
    'C': ['A', 'B', 'D', 'E', 'F', 'G'],
    'D': ['A', 'B', 'C', 'E', 'H'],
    'E': ['A', 'C', 'D', 'F', 'H', 'I'],
    'F': ['B', 'C', 'E', 'G', 'I', 'J'],
    'G': ['C', 'F', 'H', 'J', 'K', 'L'],
    'H': ['D', 'E', 'G', 'I', 'L'],
    'I': ['E', 'F', 'H', 'J', 'L', 'M'],
    'J': ['F', 'G', 'I', 'K', 'M', 'N'],
    'K': ['G', 'J', 'L', 'N', 'O', 'P'],
    'L': ['G', 'H', 'I', 'K', 'P'],
    'M': ['I', 'J', 'N', 'Q'],
    'N': ['J', 'K', 'M', 'O', 'Q', 'R'],
    'O': ['K', 'N', 'P', 'R'],
    'P': ['K', 'L', 'O', 'S'],
    'Q': ['M', 'N', 'R', 'T'],
    'R': ['N', 'O', 'Q', 'S', 'T', 'U'],
    'S': ['P', 'R', 'U'],
    'T': ['Q', 'R', 'U', 'V'],
    'U': ['R', 'S', 'T', 'V'],
    'V': ['T', 'U', 'W', 'X'],
    'W': ['V', 'X', 'Y'],
    'X': [],
    'Y': [],
    'Z': []
}


# start BFS from vertex 'A'
bfs(graph, 'A')

end = time.time()
print(end - start)