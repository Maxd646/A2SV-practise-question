# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            print("yes")
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        mid= postorder.index(preorder[1])
        print(mid)
        print(preorder, postorder)
        root.left = self. constructFromPrePost(preorder[1:mid+2], postorder[:mid+1])
        root.right = self. constructFromPrePost(preorder[mid+2:], postorder[mid+1:-1])
        return root

        