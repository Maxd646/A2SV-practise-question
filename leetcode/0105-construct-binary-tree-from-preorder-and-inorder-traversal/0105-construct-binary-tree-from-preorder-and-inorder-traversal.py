# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        n = len(inorder)
        seen = {inorder[i]:i for i in range(n)}
        def help(index, left, right):
            if left > right:
                return 
            
            root = TreeNode(preorder[index])

            mid = seen[preorder[index]]

            if mid > left:
                root.left = help(index +1, left, mid-1)
            if mid < right:
                root.right = help(index+mid-left+1, mid+1, right)
            return root
        return help(0, 0, n-1)


        