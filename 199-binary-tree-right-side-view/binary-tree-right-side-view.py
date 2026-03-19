# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        stack=deque()
        stack.append(root)
        while stack:
            for i in range(len(stack)):
                m= stack.popleft()
                if m.left:
                    stack.append(m.left)
                if m.right:
                    stack.append(m.right)
            ans.append(m.val)
        return ans
        
        