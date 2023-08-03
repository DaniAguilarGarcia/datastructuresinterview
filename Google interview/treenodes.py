#count complete tree nodes
#binary search to construct the sequence of moves to the leaf
#right->left->left
class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        d=0
        while node.left:
            node = node.left
            d += 1
        return d
    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d-1
        for _ in range(d):
            pivot = left +(right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
    def countNodes(self, root: TreeNode) -> int:
        #if tree is empty
        if not root:
            return 0
        
    d = self.compute_depth(root)
    #if tree contains 1 node
    if d == 0:
        return 1
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
    left, right = 1, 2**d - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if self.exists(pivot, d, root):
            left = pivot +1
        else:
            right = pivot - 1
    return (2**d - 1) + left
