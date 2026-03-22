# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:return False
        if not subroot: return True
        if self.same(root, subroot): return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

    def same(self, root, subroot):
        if not root and not subroot: return True
        if not root  or not subroot: return False
        if root.val!= subroot.val: return False
        return self.same(root.left, subroot.left) and self.same(root.right, subroot.right)
        


        
        