# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0
        def DFS(root):

            nonlocal ans 

            if not root:
                return 0, 0
            
            left,leftc = DFS(root.left)
            right, rightc = DFS(root.right)

            total = left + right + root.val
            count = leftc + rightc + 1

            if total//count == root.val:
                ans += 1

            return total, count

        DFS(root)

        return ans

        