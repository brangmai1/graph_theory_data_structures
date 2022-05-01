from pprint import pprint

class AdjacencyList:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def add_edges(self, new_list):
        for first, direction, second in new_list:
            if direction == '->':
                self.right_direction(first, second)
            elif direction == '<-':
                self.left_direction(first, second)
            else:
                self.right_direction(first, second)
                self.left_direction(first, second)

    def right_direction(self, first_vertex, second_vertex):
        if first_vertex in self.adj_list:
            self.adj_list[first_vertex].append(second_vertex)
        else:
            self.adj_list[first_vertex] = [second_vertex]

    def left_direction(self, first_vertex, second_vertex):
        if first_vertex in self.adj_list:
            self.adj_list[first_vertex].append(second_vertex)
        else:
            self.adj_list[first_vertex] = [second_vertex]

    def display_list(self):
        pprint(self.adj_list)
