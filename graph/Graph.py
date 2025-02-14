from typing import Dict

class Graph:
    adj_list: Dict[str, list[str]]

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print(self.adj_list)

    def add_vertex(self, vertex: str):
        if not vertex in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True

        return False

    def add_edge(self, v1: str, v2: str):
        keys = self.adj_list.keys()
        if not (v1 in keys and v2 in keys):
            return False

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

        return True

    def remove_edge(self, v1: str, v2: str):
        keys = self.adj_list.keys()
        if not (v1 in keys and v2 in keys):
            return False

        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)

        return True

    def remove_vertex(self, vertex: str):
        keys = self.adj_list.keys()
        if not (vertex in keys):
            return False

        self.adj_list.pop(vertex)

        for v in keys:
            if vertex in self.adj_list[v]:
                self.adj_list[v].remove(vertex)

        return True
