# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        stack=[]
        def pre(root, tr):
            if not root:
                return False
            stack.append(root.val)
            if not root.left and not root.right:
                if sum(stack)==tr:
                    ans.append(stack[:])
                stack.pop()
                return 
            pre(root.left, tr)
            pre(root.right, tr)
            stack.pop()
            return 
        pre(root, targetSum )
            
        return ans
        

        

        