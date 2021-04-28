import networkx as nx
import matplotlib.pyplot as plt

import sys
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_MinSpanning(self, a):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(a[i], "-",i, "\t", self.graph[i][a[i]])

    def minKey(self, key, min_span_tree_set):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and min_span_tree_set[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def prims_algorithm(self):
        key = [sys.maxsize] * self.V
        a = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        min_span_tree_set = [False] * self.V

        a[0] = -1  # First node is always the root of

        for cout in range(self.V):
            u = self.minKey(key, min_span_tree_set)
            min_span_tree_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and min_span_tree_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    a[v] = u

        self.print_MinSpanning(a)

t = Graph(9)
t.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 6, 14, 0, 0, 0],
           [0, 0, 0, 6, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
t.prims_algorithm()

#Graph Visualization
G=nx.Graph()
G.add_edge('a','b', weight=4)
G.add_edge('a','h',weight=8)
G.add_edge('b','h',weight=11)
G.add_edge('b','c',weight=8)
G.add_edge('c','i',weight=2)
G.add_edge('c','d',weight=7)
G.add_edge('c','f',weight=4)
G.add_edge('d','e',weight=6)
G.add_edge('d','f',weight=14)
G.add_edge('e','f',weight=10)
G.add_edge('f','g',weight=2)
G.add_edge('g','i',weight=6)
G.add_edge('g','h',weight=1)
G.add_edge('h','i',weight=7)

labels = nx.get_edge_attributes(G,'weight')
pos = nx.spring_layout(G)

nx.draw_networkx(G,pos, edge_color='r' , node_color='c', node_size=500)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()

