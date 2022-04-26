from pprint import pprint


class AdjacencyMatrix:
    def __init__(self, *args):
        self.adj_matrix = []

        nodes_count = self.nodes_total(*args)
        temp_list = []

        for value in range(nodes_count + 1):
            temp_list.append(0)
        for value in range(nodes_count + 1):
            self.adj_matrix.append(temp_list[:])

        adj_list = self.adjacency_list(*args)
        for node in adj_list.keys():
            for item in adj_list[node]:
                self.adj_matrix[node][item] = 1

    def __getitem__(self, item):
        return item

    def nodes_total(*args):
        set_of_nodes = set()
        for edge_pair in args:
            set_of_nodes.add(edge_pair[0])
            set_of_nodes.add(edge_pair[2])
        return len(set_of_nodes)

    def adjacency_list(self, *args):
        adj_list = dict()
        for edge_pair in args:
            if edge_pair[1] == '->':
                self.right_direction(adj_list, edge_pair)
            elif edge_pair[1] == '<-':
                self.left_direction(adj_list, edge_pair)
            else:
                self.right_direction(adj_list, edge_pair)
                self.left_direction(adj_list, edge_pair)
        return adj_list

    def right_direction(a_list, pair):
        node = pair[0]
        if node in a_list:
            a_list[node].append(pair[2])
        else:
            a_list[node] = [pair[2]]

    def left_direction(a_list, pair):
        node = pair[2]
        if node in a_list:
            a_list[node].append(pair[0])
        else:
            a_list[node] = [pair[0]]

    def add_edge_pairs(self, first_node, second_node):
        self.adj_matrix[first_node].append(second_node)

    def display_matrix(self):
        pprint(self.adj_matrix)


if __name__ == '__main__':

    adj_matrix = AdjacencyMatrix((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
                                  #(4, '<>', 5), (2, '<>', 5))
