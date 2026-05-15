# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        self.count(root )
        return self.global_max
    def count(self, node):
        if node is None:
            return 0
        left_gain = max(self.count(node.left),0)
        right_gain = max(self.count(node.right),0)
        current_path = node.val + left_gain + right_gain
        self.global_max = max(current_path,self.global_max)
        return node.val + max(left_gain, right_gain)
        