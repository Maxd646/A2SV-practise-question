# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def pre(root, level):
            nonlocal ans

            if not root:
                return 
            ans = max(ans, level)
            pre(root.left, level+1)
            pre(root.right, level+1)
        pre(root, 1)
        return ans
            
        