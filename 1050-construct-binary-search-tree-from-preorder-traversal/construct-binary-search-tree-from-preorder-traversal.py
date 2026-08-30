class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0

        def dfs(bound):
            nonlocal i

            if i == len(preorder) or preorder[i] > bound:
                return None

            root = TreeNode(preorder[i])
            i += 1

            root.left = dfs(root.val)
            root.right = dfs(bound)

            return root

        return dfs(float('inf'))
