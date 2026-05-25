# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen = Counter()
        def dfs(root):
            if root:
                seen[root.val] +=1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        x = sorted(seen.items(), key = lambda x:- x[1])[0][1]
        # print(x)
        ans =[]
        for z, y in seen.items():
            if x == y:
                ans.append(z) 
        return ans

        