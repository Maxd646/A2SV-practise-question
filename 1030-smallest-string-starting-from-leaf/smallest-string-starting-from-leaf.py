# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        Minn = ""
        string = ""
        def dfs(root):

            nonlocal Minn

            nonlocal string

            if not root:
                return 
            string += chr(ord('a') + root.val)

            if root.left is None and root.right is None:

                curr = string[::-1]
                if Minn == "" or Minn > curr:
                    Minn = curr
                    
            dfs(root.left)
            dfs(root.right)
            string = string[:-1]
        dfs(root)
        return Minn
            
        