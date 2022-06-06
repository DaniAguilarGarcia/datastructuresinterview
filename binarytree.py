#each oarent node can have at most 2 children
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def traversePreorder(self):
        print(self.val, end= '')
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder