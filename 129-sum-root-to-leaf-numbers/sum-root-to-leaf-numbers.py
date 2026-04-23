# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans =0
        node =[]
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            node.append(root.val)
            if not root.left and not root.right:
                ans += int("".join(map(str, node)))
            dfs(root.left)
            dfs(root.right)
            node.pop()
        dfs(root)
        return ans
            

        