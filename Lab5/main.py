import numpy as np
import time
import networkx as nx
import matplotlib.pyplot as plt

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[start] = 0
    for _ in range(n):
        u = min(filter(lambda x: not visited[x], range(n)), key=dist.__getitem__)
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
    return dist

# Floyd-Warshall algorithm implementation
def floyd_warshall(graph):
    n = len(graph)
    dist = graph.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Function to draw graph using NetworkX
def draw_graph(graph):
    G = nx.DiGraph()
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Measure execution time of Dijkstra's algorithm for increasing number of nodes in sparse graph
times_sparse_dijkstra = []
for n in range(10, 101, 10):
    graph_sparse = np.random.choice([0, 1], size=(n, n), p=[0.9, 0.1])
    start_time = time.time()
    dijkstra(graph_sparse, 0)
    end_time = time.time()
    times_sparse_dijkstra.append(end_time - start_time)

# Measure execution time of Floyd-Warshall algorithm for increasing number of nodes in sparse graph
times_sparse_floyd = []
for n in range(10, 101, 10):
    graph_sparse = np.random.choice([0, 1], size=(n, n), p=[0.9, 0.1])
    start_time = time.time()
    floyd_warshall(graph_sparse)
    end_time = time.time()
    times_sparse_floyd.append(end_time - start_time)

# Measure execution time of Dijkstra's algorithm for increasing number of nodes in dense graph
times_dense_dijkstra = []
for n in range(10, 101, 10):
    graph_dense = np.random.randint(0, 10, size=(n, n))
    start_time = time.time()
    dijkstra(graph_dense, 0)
    end_time = time.time()
    times_dense_dijkstra.append(end_time - start_time)

# Measure execution time of Floyd-Warshall algorithm for increasing number of nodes in dense graph
times_dense_floyd = []
for n in range(10, 101, 10):
    graph_dense = np.random.randint(0, 10, size=(n, n))
    start_time = time.time()
    floyd_warshall(graph_dense)
    end_time = time.time()
    times_dense_floyd.append(end_time - start_time)

#
# Draw sample sparse graph
graph_sparse = np.random.choice([0, 1], size=(10, 10), p=[0.9, 0.1])
draw_graph(graph_sparse)

# Draw sample dense graph
graph_dense = np.random.randint(0, 10, size=(10, 10))
draw_graph(graph_dense)
# Plot execution time data for sparse graph
plt.plot(range(10, 101, 10), times_sparse_dijkstra, label="Dijkstra's Algorithm (Sparse)")
plt.plot(range(10, 101, 10), times_sparse_floyd, label="Floyd-Warshall Algorithm (Sparse)")
plt.legend()
plt.xlabel("Number of Nodes")
plt.ylabel("Execution Time (Seconds)")
plt.title("Execution Time of Shortest Path Algorithms on Sparse Graph")
plt.show()

# Plot execution time data for dense graph
plt.plot(range(10, 101, 10), times_dense_dijkstra, label="Dijkstra's Algorithm (Dense)")
plt.plot(range(10, 101, 10), times_dense_floyd, label="Floyd-Warshall Algorithm (Dense)")
plt.legend()
plt.xlabel("Number of Nodes")
plt.ylabel("Execution Time (Seconds)")
plt.title("Execution Time of Shortest Path Algorithms on Dense Graph")
plt.show()
