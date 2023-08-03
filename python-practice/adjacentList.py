#represents graphs as an array list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.graph = None
class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
    #add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s]= node

        node = AdjNode(s)
        node.next = self.graph[s]
        self.graph[s] = node
    #print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end=" ")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()