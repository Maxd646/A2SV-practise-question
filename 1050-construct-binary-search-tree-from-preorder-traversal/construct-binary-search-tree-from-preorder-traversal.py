# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        inorder = sorted(preorder)
        
        seen = {inorder[i]: i for i in range(len(inorder))}

        def dfs(index, left, right):

            if left > right:
                return 

            root = TreeNode(preorder[index])
            mid = seen[preorder[index]]

            if mid > left:
                root.left = dfs(index+1, left, mid-1)
            
            if mid < right:
                root.right = dfs(index + (mid -left+1), mid+1, right)

            return root

        return dfs(0, 0, len(preorder)-1)





        