# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass
        _, path_p = self.search(root, p.val)
        path_p = path_p[::-1]

        _, path_q = self.search(root, q.val)
        path_q = path_q[::-1]


        i = 0 
        while i< len(path_p) and i < len(path_q) and path_p[i].val == path_q[i].val:
            i+=1
        i-=1
        return path_p[i]

    def search(self, node, num):
        print(node.val if node else None, num)
        if node is None:
            return False, []
        if node.val == num:
            return True, [node]
        found, path = self.search(node.left, num)
        if found:
            return True, path + [node]
        
        found, path = self.search(node.right, num)
        if found:
            return True, path + [node]
        return False, []
        
        