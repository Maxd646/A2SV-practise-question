# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return check(node.left, val) and check(node.right, val)
        
        if not root:
            return True
        return check(root, root.val)
        
       

            

        