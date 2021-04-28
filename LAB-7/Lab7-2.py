# Kruskal's Algorithm
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d  " % (u, v, weight))

print("Kruskal's Algorithm:")
print("Edge \tWeight")
g= Graph(9)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,7,11)
g.addEdge(1,2,8)
g.addEdge(2,8,2)
g.addEdge(2,3,7)
g.addEdge(2,5,4)
g.addEdge(3,4,6)
g.addEdge(3,5,14)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,8,6)
g.addEdge(6,7,1)
g.addEdge(7,8,7)

g.kruskal_algo()


# Visualization of minimum spanning tree
H=nx.Graph()
H.add_edge('a','b', weight=4)
H.add_edge('b','c',weight=8)
H.add_edge('c','d',weight=7)
H.add_edge('d','e',weight=6)
H.add_edge('c','i',weight=2)
H.add_edge('c','f',weight=4)
H.add_edge('f','g',weight=2)
H.add_edge('g','h',weight=1)

labels = nx.get_edge_attributes(H,'weight')
pos = nx.spring_layout(H)

nx.draw_networkx(H,pos, edge_color='g' , node_color='c', node_size=500)
nx.draw_networkx_edge_labels(H,pos,edge_labels=labels)

plt.show()
