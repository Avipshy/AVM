# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low_bound, high_bound):
            if not node:
                return True
            if not (low_bound < node.val < high_bound):
                return False
            
            return (valid(node.left, low_bound, node.val) and valid(node.right, node.val, high_bound))

        return valid(root, float('-inf'), float('inf'))