# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(curr):
            if not curr:
                return 0
            extraL = dfs(curr.left)
            extraR = dfs(curr.right)
            self.ans += abs(curr.val-1 + extraL + extraR)
            return curr.val-1 + extraL + extraR
        dfs(root)
        return self.ans
                
        