# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0
        x=self.maxDepth(root.left)
        y=self.maxDepth(root.right)
        print(1, max(x, y))
        return 1+ max(x, y)
        
            
