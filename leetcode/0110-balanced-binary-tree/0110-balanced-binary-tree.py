# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root):

            if not root:
                return 0

            q= deque()
            q.append(root)
            h = 0

            while q:

                h += 1

                for i in range(len(q)):
                    temp = q.popleft()

                    if temp.left:
                        q.append(temp.left)

                    if temp.right:
                        q.append(temp.right)
            return h

        qu = deque()
        qu.append(root)

        while qu:

            node = qu.popleft()
            left = height(node.left)
            right = height(node.right)

            if abs(left-right)>1:
                return False

            if node.left:
                qu.append(node.left)

            if node.right:
                qu.append(node.right)
        return True

        