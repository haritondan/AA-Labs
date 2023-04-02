from timeit import default_timer as timer
start = timer()
graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '3': ['7', '8'],
    '4': ['9', '10'],
    '5': ['11', '12'],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
    '12': []
}

graph2 = {
    '1': ['2', '3', '4','5'],
    '2': ['6', '7'],
    '3': [],
    '4': [],
    '5': [],
    '6': ['8','9'],
    '7': ['10','11'],
    '8': ['12'],
    '9': [],
    '10': [],
    '11': [],
    '12': ['13'],
    '13':[]
}

def dfs(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    if node == target:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

# Call the DFS function with the starting node '1' and target node '11'
# dfs(graph, '1', '12')
print('\n')
dfs(graph2, '1', '12')
print('\n')
end = timer()
print(end - start)