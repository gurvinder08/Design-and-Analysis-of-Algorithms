import sys
print("Dijkstra's Algorithm Implementation:")

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def showAns(self, dist):
        print("Vertex \tDistance from a")
        for node in range(self.V):
            print(node, "\t","\t", dist[node])

    def minDistance(self, dist, Set):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and Set[v] == False:
                min = dist[v]
                min_index = v

        return min_index
    def dijkstra_algorithm(self, a):

        dist = [sys.maxsize] * self.V
        dist[a] = 0
        Set = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, Set)
            Set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and Set[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.showAns(dist)

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
t.dijkstra_algorithm(0)
