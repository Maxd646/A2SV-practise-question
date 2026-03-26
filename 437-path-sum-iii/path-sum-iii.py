# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def help(root, targetSum):
            if not root:
                return 0
            res=0
            if root.val == targetSum:
                res+=1
            newsum =  targetSum - root.val
            res += help(root.left, newsum)
            res += help(root.right, newsum)
            return res
        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)
        return help(root, targetSum)+ left + right
        


        