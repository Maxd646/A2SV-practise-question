# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.helper(root, arr)
        for i in range(1, len(arr)):
            if arr[i-1]>= arr[i]:
                return False
        return True
    def helper(self, root, arr):
        if not root:
            return 
        self.helper(root.left, arr)
        arr.append(root.val)
        self.helper(root.right, arr)
    





        


        
        