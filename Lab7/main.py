import random
import time
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = set(range(num_vertices))
        self.edges = []
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.edges.append((u, v))
        self.edges.append((v, u))
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def get_neighbors(self, vertex):
        neighbors = set()
        for u, v in self.edges:
            if u == vertex:
                neighbors.add(v)
            elif v == vertex:
                neighbors.add(u)
        return neighbors


def kruskal(graph):
    mst = set()
    forest = {vertex: {vertex} for vertex in graph.vertices}
    edges = list(graph.weights.keys())
    edges.sort(key=lambda uv: graph.weights[uv])
    for uv in edges:
        u, v = uv
        if forest[u] != forest[v]:
            mst.add(uv)
            old_tree = forest[u]
            new_tree = forest[v]
            for w in old_tree:
                forest[w] = new_tree
    return mst

def prim(graph):
    mst = set()
    visited = {0}
    while len(visited) < graph.num_vertices:
        candidates = []
        for vertex in visited:
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    candidates.append((vertex, neighbor))
        edge = min(candidates, key=lambda uv: graph.weights[uv])
        mst.add(edge)
        visited.add(edge[1])
    return mst

# Generate random graphs
num_vertices_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
graph_list = [Graph(num_vertices) for num_vertices in num_vertices_list]
for graph in graph_list:
    for u in graph.vertices:
        for v in graph.vertices:
            if u < v:
                graph.add_edge(u, v, random.randint(1, 100))

# Time Kruskal's algorithm
kruskal_times = []
for graph in graph_list:
    start_time = time.time()
    kruskal(graph)
    end_time = time.time()
    kruskal_times.append(end_time - start_time)

# Time Prim's algorithm
prim_times = []
for graph in graph_list:
    start_time = time.time()
    prim(graph)
    end_time = time.time()
    prim_times.append(end_time - start_time)

# Plot the results
plt.plot(num_vertices_list, kruskal_times, label='Kruskal')
plt.plot(num_vertices_list, prim_times, label='Prim')
plt.xlabel('Number of vertices')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
