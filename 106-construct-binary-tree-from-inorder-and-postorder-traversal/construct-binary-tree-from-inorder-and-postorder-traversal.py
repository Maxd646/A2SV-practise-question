# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        n = len(inorder)
        seen = {inorder[i]: i for i in range(n)}

        def help (index, left, right):
            if left> right :
                return

            root = TreeNode(postorder[index])
            mid = seen[postorder[index]]

            if left < mid :
                root.left = help(index-(right-mid+1), left, mid-1)

            if right > mid:
                root.right = help (index-1, mid+1, right)
            return root

        return help(n-1, 0, n-1)
        