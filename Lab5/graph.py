import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt


def generate_random_graph(num_nodes, num_edges):
    graph = {str(i): {} for i in range(num_nodes)}

    while num_edges > 0:
        u, v = random.sample(graph.keys(), 2)
        if v not in graph[u]:
            weight = random.randint(1, 10)
            graph[u][v] = weight
            graph[v][u] = weight
            num_edges -= 1

    return graph


def generate_sparse_graph(num_nodes, edge_density):
    max_edges = int(num_nodes * (num_nodes - 1) / 2)
    num_edges = int(max_edges * edge_density)
    graph = {str(i): {} for i in range(num_nodes)}

    while num_edges > 0:
        u, v = random.sample(graph.keys(), 2)
        if v not in graph[u]:
            weight = random.randint(1, 10)
            graph[u][v] = weight
            graph[v][u] = weight
            num_edges -= 1

    return graph


def generate_complete_graph(num_nodes):
    graph = {str(i): {str(j): random.randint(1, 10) for j in range(i + 1, num_nodes)} for i in range(num_nodes)}
    for i in graph:
        for j in graph[i]:
            graph[j][i] = graph[i][j]
    return graph


def draw_graph(graph, title):
    G = nx.Graph()
    edge_labels = {(node, neighbor): weight for node in graph for neighbor, weight in graph[node].items()}
    G.add_nodes_from(graph.keys())
    G.add_edges_from(edge_labels.keys())

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.axis('off')
    plt.show()


def dijkstra(graph, start, target):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        if current_vertex == target:
            return distances[target]
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return -1


def floyd(graph, start, target):
    if start not in graph or target not in graph:
        return -1

    nodes = list(graph.keys())
    dist = {i: {j: 0 if i == j else graph[i].get(j, float('inf')) for j in nodes} for i in nodes}

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist[start][target] if dist[start][target] != float('inf') else -1
