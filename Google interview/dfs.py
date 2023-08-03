#recursive dfs

class Node:
    def __init__(self, value, left = None, right = None)
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node(" + str(self.value) + ")"



def walk(tree):
    if tree is not None:
        print(tree) #pre order
        walk(tree.left)
        print(tree) #in order
        walk(tree.right)
        print(tree) #post order

#iterative dfs

def walk2(tree, stack):
    stack.append(tree)
    while len(strack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

#transversing a tree going from top to bottom
#preorder: A -> B -> D -> E -> C -> F -> G
#in order: D -> B -> E -> A -> F -> C -> G
#post order: D -> E -> B -> F -> G -> C -> A

#use a stack
#graph traversal: visit every vertex of the graph
