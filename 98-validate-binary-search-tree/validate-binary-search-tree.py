# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        seen = set()
        def dfs(root):
            if root:
                dfs(root.left)
                if root.val in seen:
                    return True
                    exit()
                inorder.append(root.val)
                dfs(root.right)
        dfs(root)
        if inorder == sorted(list(set(inorder))):
            return True
        return False

        

        