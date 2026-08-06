# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pre(rootleft, rootright, level):
            if rootleft is None or rootright is None:
                return root
            if level %2 == 0:
                rootleft.val, rootright.val = rootright.val, rootleft.val
            pre(rootleft.left, rootright.right, level+1)
            pre(rootleft.right, rootright.left, level+1)
        pre(root.left, root.right, 0)
        return root
            
            
        