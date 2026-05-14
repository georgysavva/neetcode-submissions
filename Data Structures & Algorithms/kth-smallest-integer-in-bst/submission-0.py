# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count(root)
        return self._kthSmallest(root, k-1)

    def _kthSmallest(self, node, k):
        print("val count k", node.val, node.count, k)
        left_count = node.left.count if node.left is not None else 0
        if left_count == k:
            return node.val
        elif left_count< k:
            return self._kthSmallest(node.right,k-left_count-1)
        else:
            return self._kthSmallest(node.left,k)
    def count(self, node):
        if node is None:
            return 0
        current_count= 1 + self.count(node.left) + self.count(node.right)
        node.count=current_count
        return current_count
        