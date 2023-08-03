#adjacency matrix
#representing a graph as a matrix of booleans(0s and 1s)
#the boolean value indicates if there is a direct path between two vertices.

def Graph(object):
    #initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    #add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("same vertex d% and d%" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    #remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
             print("No edge between %d and %d" % (v1, v2))
             return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def __len__(self):
        return self.size
    #print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print
    def main():
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)

        g.print_matrix()


if __name__ == '__main__':
    main()



