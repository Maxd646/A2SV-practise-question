class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxsum = 0

        class Info:
            def __init__(self, _max, _min, isBST, _sum):
                self.max = _max
                self.min = _min
                self.isBST = isBST
                self.sum = _sum

        def dfs(node):
            if not node:
                return Info(float('-inf'), float('inf'), True, 0)

            L = dfs(node.left)
            R = dfs(node.right)

            if L.isBST and R.isBST and L.max < node.val < R.min:
                total = L.sum + R.sum + node.val
                self.maxsum = max(self.maxsum, total)

                return Info(max(node.val, R.max), min(node.val, L.min), True, total)

            return Info(0, 0, False, 0)

        dfs(root)
        return self.maxsum