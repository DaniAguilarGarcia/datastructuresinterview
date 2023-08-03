class Solutions(object):
    def __init__(self):
        #dict which holds old nodes as keys and new nodes as its values
        self.validation = {}

    def copyRandomList(self, head):
        if head == None:
            return None
            #if we have already processed the current node, then we simply return the cloned verion of it
            if head in self.visitedHash:
                return.visitedHash[head]
            #create new node
            #with the value same as old node
            node = Node(head.val, None, None)
            #save value in hash map
            self.visitedHash[head] = node
            #recursive copy
            node.next = self.copyRandomList(head.next)
            node.copyRandomList = self.copyRandomList(head.random)

            return node
