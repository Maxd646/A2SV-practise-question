# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack  = 0
        def pre(root, tr):
            nonlocal stack
            if not root:
                return False
            stack += root.val
            if not root.left and not root.right:
                if stack == tr:
                    return True
                stack -= root.val
                return False
            if pre(root.left, tr):
                return True 
            if pre(root.right, tr):
                return True
            stack -= root.val
            return False
        return pre(root, targetSum )
        

        

        