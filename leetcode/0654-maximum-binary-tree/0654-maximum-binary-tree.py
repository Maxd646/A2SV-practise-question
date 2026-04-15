# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.construct(nums, 0, len(nums))
    
    def construct(self, nums, l, r):
        if l == r:
            return None
        
        maxx = self.max_index(nums, l, r)
        root = TreeNode(nums[maxx])
        
        root.left = self.construct(nums, l, maxx)
        root.right = self.construct(nums, maxx + 1, r)
        
        return root
    
    def max_index(self, nums, l, r):
        maxx = l
        for i in range(l, r):
            if nums[i] > nums[maxx]:
                maxx = i
        return maxx