#based on the dfs algo implemented twice, to find strongly connected components
#1. perform a dfs on the whole graph
#2.reverse the original graph
#3. dfs in reversed graph
#used for: vehicle routing applications, maps, model checking in formal verification
#algorithm runs in linear time 

from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

        #add edg into the graph
        def add_edge(self, s, d):
            self.graph[s].append(d)

        #dfs
        def dfs(self, d, visited_vertex):
            visited_vertex[d] = True
            print(d, end=' ')
            for i in self.graph[d]:
                if not visited_vertex[i]:
                    self.dfs(i, visited_vertex)
        
        def fill_order(self, d, visited_vertex, stack):
            visited_vertex[d] = True
            for i in self.graph[d]:
                if not visited_vertex[i]:
                    self.fill_order(i, visited_vertex, stack)
            stack = stack.append(d)
        #transpose the matrix
        def transpose(self):
            g = Graph(self.v)

            for i in self.graph:
                for j in self.graph[i]:
                    g.add_edge(j, i)
            return g

        #print strongly connected components
        def print_scc(self):
            stack = []
            visited_vertex = [False] * (self.v)

            for i in range(self.V):
                if not visited_vertex[i]:
                    self.fill_order(i, visited_vertex, stack)
            gr = self.transpose()

            visited_vertex = [False] * (self.V)

            while stack:
                i = stack.pop()
                if not visited_vertex[i]:
                    gr.dfs(i, visited_vertex)
                    print(" ")