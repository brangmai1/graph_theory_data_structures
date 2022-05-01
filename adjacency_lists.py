

class AdjacencyLists:

    def __init__(self, args):
        self.adj_list = dict()
        for first, second in args:
            if first not in adj_list:
                


            if edge_pair[1] == '->':
                self.right_direction(adj_list, edge_pair)
            elif edge_pair[1] == '<-':
                self.left_direction(adj_list, edge_pair)
            else:
                self.right_direction(adj_list, edge_pair)
                self.left_direction(adj_list, edge_pair)


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


if __name__ == "__main__":

    adj_list = AdjacencyLists((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (4, 3),(4, 5), (2, 5))


    my_matrix = adjacency_matrix((1, '->', 2), (1, '->', 3), (2, '->', 1), (2, '<-', 4), (3, '->', 1), (4, '<>', 3),
                                 (4, '<>', 5), (2, '<>', 5))
    print("\nAdjacency Matrix")
    pprint(my_matrix)
