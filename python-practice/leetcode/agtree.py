#definition of a binary tree node

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def treeLeftRight(self, root):
        ret = []
        level_list = deque()
        if root is None:
            return []
        #start with the level 0 with delimeter
        node_queue = deque((root, None))
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                #we finish one level
                ret.append(level_list)
                #add a delimeter to mark the level 
                if len(node_queue) > 0:
                    node_queue.append(None)
                #prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left
        return ret