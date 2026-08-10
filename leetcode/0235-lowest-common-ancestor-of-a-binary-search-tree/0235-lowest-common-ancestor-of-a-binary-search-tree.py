# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def dfs(root, num):
            nonlocal ans
            ans.append(root)
            if root.val< num.val:
                dfs(root.right, num)
            elif root.val > num.val:
                dfs(root.left, num)
            else: return 
        dfs(root, p)
        temp = ans[:] 
        ans = []
        dfs(root, q)
        
        seen = set(temp)
        res = None
        for i in range(len(ans)):
            if ans[i] in seen:
                res = ans[i]
        return res
        
            
        