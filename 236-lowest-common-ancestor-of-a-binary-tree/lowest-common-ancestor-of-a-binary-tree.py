# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans1 = []
        ans2 = []
        def dfs(root, num, ans):
            if not root:
                return 
            ans.append(root)
            if root == num:
                return True
            if dfs(root.left, num, ans):
                return True
            if dfs(root.right, num, ans):
                return True
            ans.pop()
            return 

        dfs(root, p, ans1)
        dfs(root, q, ans2)
        seen = set(ans1)
        res = None
        for i in range(len(ans2)):
            if ans2[i] in seen:
                res = ans2[i]
       
        return res
        