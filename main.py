# Brang Mai
from pprint import pprint
import numpy as np
#from adjacency_lists import AdjacencyLists
#from adjacency_matrix import AdjacencyMatrix


def adjacency_list(*args):
    adj_list = dict()
    for edge_pair in args:
        if edge_pair[1] == '->':
            right_direction(adj_list, edge_pair)
        elif edge_pair[1] == '<-':
            left_direction(adj_list, edge_pair)
        else:
            right_direction(adj_list, edge_pair)
            left_direction(adj_list, edge_pair)
    return adj_list


def right_direction(adj_list, pair):
    node = pair[0]
    if node in adj_list:
        adj_list[node].append(pair[2])
    else:
        adj_list[node] = [pair[2]]


def left_direction(adj_list, pair):
    node = pair[2]
    if node in adj_list:
        adj_list[node].append(pair[0])
    else:
        adj_list[node] = [pair[0]]


def nodes_total(*args):
    set_of_nodes = set()
    for edge_pair in args:
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[2])
    return len(set_of_nodes)


def adjacency_matrix(*args):
    nodes_count = nodes_total(*args)

    adj_matrix = []
    temp_list = []

    for value in range(nodes_count + 1):
        temp_list.append(0)
    for value in range(nodes_count + 1):
        adj_matrix.append(temp_list[:])

    adj_list = adjacency_list(*args)
    for node in adj_list.keys():
        for item in adj_list[node]:
            # print(f'Node is {node}, item is {item}')
            adj_matrix[node][item] = 1
    return adj_matrix


def numpy_array(*args):
    nodes_count = nodes_total(*args)
    print(f'total nodes {nodes_count}')
    num_matrix = np.zeros((5, 5))
    return num_matrix


if __name__ == "__main__":
    mal = adjacency_list((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
                         (4, '<>', 5), (2, '<>', 5))
    print("Adjacency List")
    pprint(mal)

    my_matrix = adjacency_matrix((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
                                 (4, '<>', 5), (2, '<>', 5))
    print("\nAdjacency Matrix")
    pprint(my_matrix)

    # al = AdjacencyLists()
    # al.hello_name()

    # am = AdjacencyMatrix((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
    #                      (4, '<>', 5), (2, '<>', 5))

    # my_matrix = AdjacencyMatrix((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
    #                               (4, '<>', 5), (2, '<>', 5))
    #
    # my_matrix.display_matrix()
    # num_array_matrix = numpy_array()
    #
    # print(num_array_matrix)
