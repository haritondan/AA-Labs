import math
import random
import numpy as np
from matplotlib import pyplot as plt
from graph import generate_sparse_graph, generate_complete_graph, draw_graph, floyd, dijkstra
import time


dense_graph = generate_complete_graph(10)
draw_graph(dense_graph, 'Dense Graph')

sparse_graph = generate_sparse_graph(10, 0.3)
draw_graph(sparse_graph, 'Sparse Graph')

random.seed(100)

times_floyd = list()
times_dj = list()
nodes = [5, 25, 50, 100]
nodes_searched = list()
node_search = list()
digit_num = 6
image_num = 0

for i in nodes:

    current_times_dj = list()
    current_times_floyd = list()
    random_nodes = list()
    nodes_searched.append('Graph ' + str(i))
    node_search.append('Graph: ' + str(i))

    # Sparse graph
    nodes_searched.append('Sparse: ')
    node_search.append('Sparse: ')
    graph_sparse = generate_sparse_graph(i, 2 / i)

    if i / 5 >= 5:
        search = 5
    else:
        search = math.floor(i / 5)

    for j in range(search):
        start_node = str(random.randint((j + 1), (j + 1) * 2))
        end_node = str(random.randint((j + 1) * 3, (j + 1) * 5))

        # Dijkstra
        start_time = time.perf_counter()
        shortest_path_dj = dijkstra(graph_sparse, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_dj.append(round(time_taken, digit_num))

        # Floyd

        start_time = time.perf_counter()
        shortest_path_floyd = floyd(graph_sparse, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_floyd.append(round(time_taken, digit_num))

        random_nodes.append([start_node, end_node])
        nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
        node_search.append(start_node + '-' + end_node + ' | ')

    # Dense graph
    nodes_searched.append('Dense: ')
    node_search.append('Dense: ')
    graph_dense = generate_complete_graph(i)

    for j in random_nodes:
        start_node = j[0]
        end_node = j[1]

        # Dijkstra

        start_time = time.perf_counter()
        shortest_path_dj = dijkstra(graph_dense, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_dj.append(round(time_taken, digit_num))

        # Floyd

        start_time = time.perf_counter()
        shortest_path_floyd = floyd(graph_dense, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_floyd.append(round(time_taken, digit_num))

        nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
        node_search.append(start_node + '-' + end_node + ' | ')

    times_floyd.append(current_times_floyd)
    times_dj.append(current_times_dj)


arr = [i for i in range(5)]
x = np.arange(1, len(arr)+1)

# Dijkstra
plt.figure(image_num)
plt.bar(x-0.2, times_dj[2][0:5], 0.2, label='Sparse 50', color='blue')
plt.bar(x-0.1, times_dj[3][0:5], 0.2, label='Sparse 100', color='grey')
plt.bar(x+0.2, times_dj[2][5:10], 0.2, label='Dense 50', color='purple')
plt.bar(x+0.3, times_dj[3][5:10], 0.2, label='Dense 100', color='pink')
plt.xlabel('Check')
plt.ylabel('Time(s)')
plt.title('Dijkstra:')
plt.legend()

# Update x-ticks labels
custom_labels = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5']
plt.xticks(x, custom_labels)

image_num += 1

plt.figure(image_num)
plt.bar(x-0.2, times_floyd[2][0:5], 0.2, label='Sparse 50', color='blue')
plt.bar(x-0.1, times_floyd[3][0:5], 0.2, label='Sparse 100', color='red')
plt.bar(x+0.2, times_floyd[2][5:10], 0.2, label='Dense 50', color='black')
plt.bar(x+0.3, times_floyd[3][5:10], 0.2, label='Dense 100', color='orange')
plt.xlabel('Check')
plt.ylabel('Time(s)')
plt.title('Floyd:')
plt.legend()

custom_labels = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5']
plt.xticks(x, custom_labels)

image_num += 1

plt.figure(image_num)
plt.bar(x-0.3, times_dj[3][0:5], 0.2, label='Dijkstra sparse 100', color='green')
plt.bar(x+0.1, times_floyd[3][0:5], 0.2, label='Floyd sparse 100', color='magenta')
plt.bar(x+0.2, times_dj[3][5:10], 0.2, label='Dijkstra dense 100', color='orange')
plt.bar(x+0.4, times_floyd[3][5:10], 0.2, label='Floyd dense 100', color='purple')
plt.xlabel('Check')
plt.ylabel('Time(s)')
plt.title('Dijkstra vs Floyd')
plt.legend()

custom_labels = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5']
plt.xticks(x, custom_labels)
image_num += 1

plt.show()
