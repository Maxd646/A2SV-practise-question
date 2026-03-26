# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def backtrack(root, comb):
            if not root:
                return 
            comb.append(str(root.val))
            if not root.left and not root.right:
                new="->".join(comb)
                ans.append(new)
            backtrack(root.left, comb)
            backtrack(root.right, comb)
            comb.pop()
        backtrack(root, [])
        return ans

        