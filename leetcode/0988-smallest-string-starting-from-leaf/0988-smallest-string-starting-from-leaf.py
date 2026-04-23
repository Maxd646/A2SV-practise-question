# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        path = []
        def dfs(root):
            if not root:
                return ""
            ch = chr(root.val + ord('a'))
            path.append(ch)
            if not root.left and not root.right:
                ans.append(path[:][::-1])
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        return "".join(min(ans))



        