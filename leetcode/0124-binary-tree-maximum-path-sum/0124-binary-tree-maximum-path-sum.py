# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float("-inf")
        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            leftmax = max(dfs(root.left), 0)
            rightmax = max(dfs(root.right), 0)
            summ = root.val + leftmax + rightmax
            ans = max(ans, summ)

            return root.val + max(leftmax, rightmax)
        dfs(root)
        return ans

        